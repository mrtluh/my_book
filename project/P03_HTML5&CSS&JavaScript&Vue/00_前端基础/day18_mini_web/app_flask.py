import pymysql
import time
urls = []


def route(path):
    def warper(fun):
        urls.append((path, fun))

        def inner():
            pass
        return inner
    return warper


@route("/gettime.html")
def get_time():
    return "200 OK",[('Server','APP1.0')],time.ctime()


@route("/index.html")
def index():
    data_from_mysql = ''
    conn = pymysql.connect(host='localhost',port=3306,user='root',password='mysql',db='stock_db',charset='utf8')
    cur = conn.cursor()
    cur.execute("select * from info;")
    for line in cur.fetchall():
        data_from_mysql += "<tr>" \
                          "<td>%s</td>" \
                          "<td>%s</td>" \
                          "<td>%s</td>" \
                          "<td>%s</td>" \
                          "<td>%s</td>" \
                          "<td>%s</td>" \
                          "<td>%s</td>" \
                          "<td>%s</td>" \
                          "</tr>" % line
    with open("./template/index.html","r") as file:
        html_data = file.read()

    html_data = html_data.replace("{%content%}", data_from_mysql)
    return "200 OK",[('Server','APP1.0')], html_data


@route("/center.html")
def center():
    with open("./template/center.html","r") as file:
        html_data = file.read()
    data_from_mysql = "<tr>" + "<td>数据</td>"*9 + "</tr>"
    html_data = html_data.replace("{%content%}", data_from_mysql)
    return "200 OK",[('Server','APP1.0')], html_data


def app(env):
    path_info = env["PATH_INFO"]
    print("收到用户的请求路径市 %s" % path_info)
    # if path_info == "./gettime.html":
    #     return get_time()
    # elif path_info == "./index.html":
    #     return index()
    for path, fun in urls:
        if path_info == path:
            return fun()

    else:
        # 规定返回　状态,头,体
        return "404 NOT FOUND",[('Server','APP1.0')], "hello world from app"

