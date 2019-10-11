import time


def get_time():
    return "200 OK",[('Server','APP1.0')], time.ctime()


def index():
    with open("./template/index.html","r") as file:
        html_data = file.read()
    data_from_mysql = "<tr>" + "<td>数据</td>"*9 + "</tr>"
    html_data = html_data.replace("{%content%}", data_from_mysql)
    return "200 OK",[('Server','APP1.0')], html_data


def center():
    with open("./template/center.html","r") as file:
        html_data = file.read()
    data_from_mysql = "<tr>" + "<td>数据</td>"*9 + "</tr>"
    html_data = html_data.replace("{%content%}", data_from_mysql)
    return "200 OK",[('Server','APP1.0')], html_data


urls = [
    ("/gettime.html", get_time),
    ("/index.html", index),
    ("/index.html", center),
]


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
        return "404 NOT FOUND",[('Server','APP1.0')],"404 NOT FOUND"

