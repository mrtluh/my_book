import time

# 存放所有的　路径以及对应函数代码  django框架[urls.py]中 添加路由的方式
# 如果前面路径有请求　　就会执行对应的函数代码
import pymysql

url_list = [
    # ("/gettime.html", get_time),
    # ("/index.html", index),
    # ("/center.html", center)
]
def route(path):
    def warpper(func):
        # 将路径及其对应的函数添加到列表中
        url_list.append((path, func))
        def inner():
            pass
        return inner
    return warpper

# get_time = route("/getimme.html")(gettime)
@route('/gettime.html')
def get_time():
    return "200 OK",[('Server','APP1.0')],time.ctime()


@route('/index.html')
def index():
    # 1 读取出模板文件数据
    with open("./template/index.html", "r") as file:
        html_data = file.read()

    # 模板页面加　页面数据一起发送给用户　　前后端不分离
    # 2 从数据库中读取数据
    # data_from_mysql = '<tr>' + "<td>test</td>"*9 + "</tr>"
    data_from_mysql = ""
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='mysql',
                    db='stock_db', charset='utf8')
    cur = conn.cursor()
    sql = "select * from info;"
    cur.execute(sql)

    # data_from_mysql = str(cur.fetchall())
    for line in cur.fetchall():
        data_from_mysql += '''<tr>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td><input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="000007"></td>
                   </tr>''' % line

    # 3 模板替换　　{%content%}替换为用户所需的网页数据
    html_data = html_data.replace("{%content%}", data_from_mysql)
    #　render_template('index.html', content=data_from_mysql) 替换模板
    return "200 OK", [('Server', 'APP1.0')], html_data


@route('/center.html')
def center():
    # 1 读取出模板文件数据
    with open("./template/center.html", "r") as file:
        html_data = file.read()

    # 2 从数据库中读取数据
    data_from_mysql = '<tr>' + "<td>test</td>"*9 + "</tr>"

    # 3 模板替换　　{%content%}替换为用户所需的网页数据
    html_data = html_data.replace("{%content%}", data_from_mysql)
    #　render_template('index.html', content=data_from_mysql) 替换模板
    return "200 OK", [('Server', 'APP1.0')], html_data

def app(env):
    # 从字典取出ｗｅｂ服务器传过来的资源请求路径
    path_info = env['PATH_INFO']

    print("收到用户的请求路径是%s" % path_info)
    for url, func in url_list:
        if path_info == url:
            return func()
    #　正在努力处理动态资源　读数据库
    # 1 如果用户请求的路径是　　/gettime.html  就返回当前的系统时间
    # if path_info == '/gettime.html':
    #     return get_time()
    # # 2 如果用户请求的路径是　　/index.html  就返回index.html模板夹对应数据
    # elif path_info == '/index.html':
    #     return index()
    # elif path_info == '/center.html':
    #     return  center()
    else:
        # 规定返回　状态,头,体
        return "404 Not Found",[('Server','APP1.0')],"hello world from app"