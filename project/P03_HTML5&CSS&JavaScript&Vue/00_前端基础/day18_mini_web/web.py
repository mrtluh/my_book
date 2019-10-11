import socket

#  1.0 当接收到用户请求时 返回响应报文< helloworld作为响应体>
#  2.0 当接收到用户请求时 返回响应报文<固定图片作为响应体>
#  3.0 根据用户的具体资源路径请求 返回相应报文<指定资源作为响应体>
#  4.0 多线程实现　　　　作业用协程实现  handler处理者　　处理逻辑
import threading
import time

import sys


class HTTPServer(object):
    def __init__(self, port=80):
        # 1 创建监听套接字 设置套接字重用选项  绑定监听
        listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listen_socket.bind(('', port))
        listen_socket.listen(128)
        self.listen_socket = listen_socket

    def start(self):
        while True:
            # 2 接受用户的连接请求
            server_client_socket, client_address = self.listen_socket.accept()
            print("接受到了来自%s的连接请求" % str(client_address))
            # 把所有跟用户请求处理相关的逻辑放到client_request_handler函数中 子线程运行
            # 一旦有新用户连接到服务器 我们就为这个用户创建一个线程处理逻辑
            thd = threading.Thread(target=self.client_request_handler, args=(server_client_socket,))
            thd.start()

    # 处理客户端请求的函数
    @staticmethod
    def client_request_handler(server_client_socket):
        # 3 接收用户的HTTP请求报文数据  解析处理 获取用户的目的 一定要接收
        # 3.1 接收请求报文
        http_request_data = server_client_socket.recv(4096)
        # 3.2 如果数据为空 意味着浏览器中途关闭了
        if not http_request_data:
            print("客户端已经关闭了")
            server_client_socket.close()
            return
        # 3.3 从请求报文中解析出请求行的  用户的资源路径
        path_info = http_request_data.decode().split("\r\n")[0].split(" ")[1]
        print("接收到了用户的请求 %s" % path_info)

        # 3.4 如果用户请求路径是　/  －－－－－－－－> 指定到主页
        if path_info == '/':
            path_info = '/grand.html'

        # ２０１９．９．１这是调用框架新增的代码
        # 3.5 判断用户资源的后缀　判定是静态还是动态　.html
        if path_info.endswith(".html"):
            # 3.6 如果是动态资源请求　调用框架处理　　否则执行后续代码即可
            env = {
                "PATH_INFO": path_info
            }
            import Application
            import app_flask
            import app_django
            # 接收框架处理的结果　　按照HTTP响应报文格式拼接
            # status, headers, body = app_flask.app(env)
            status, headers, body = Application.app(env)

            response_data = "HTTP/1.1 %s\r\n" % status

            for header in headers:
                response_data += "%s: %s\r\n" % header
            response_data += "\r\n"
            response_data += body

            server_client_socket.send(response_data.encode())
            server_client_socket.close()
        else:
            # 4 准备数据  以HTTP响应报文格式发送给浏览器
            # 响应体中可以放任意类型的数据　　发给浏览器
            try:
                # 可能会抛出异常的代码
                # 4.1 准备响应报文
                # http_response_data = 'HTTP/1.1 200 OK\r\nServer: PWS1.0\r\n\r\nhello world'
                http_response_data = 'HTTP/1.1 200 OK\r\nServer: PWS1.0\r\n\r\n'
                # 4.2 从用户指定的文件读取出对应的　资源数据
                # with open("static/xjj.jpg", "rb") as file:
                with open("static" + path_info, "rb") as file:
                    response_body = file.read()  # 读出来就是字节数据  rb
            except Exception as e:
                # 如果有异常执行这里的代码
                print("%s" % str(e))
                http_response_data = 'HTTP/1.1 404 Not Found\r\nServer: PWS1.0\r\n\r\n'
                with open("static/404.html", "rb") as file:
                    response_body = file.read()  # 读出来就是字节数据  rb
            else:
                # 如果没有发生异常就会执行这里
                pass
            finally:
                # 不管有没有发生异常都会执行这里
                # 4.3 将报文拼接完成发送给浏览器
                server_client_socket.send(http_response_data.encode() + response_body)

                # 5 关闭套接字
                server_client_socket.close()


def main():
    # xxx.py 8080
    # print(sys.argv)  # 获取当前程序启动时的命令行参数 的列表 每个元素都是字符串
    # print("获取当前程序的端口好", sys.argv[1])
    # 如果当前的参数数量不是２个　　或者　第一个参数不是由数字构成
    if len(sys.argv) !=2 or not sys.argv[1].isdigit(): #　判断当前参数的和数量
        print("参数使用错误　python3 web.py 8080")
        return

    port = int(sys.argv[1])

    http_server = HTTPServer(port)
    http_server.start()
    # 实例对象http_server 类对象HTTPServer
if __name__ == '__main__':
    main()
    # 功能      类和对象(封装功能和属性)
    # 吃(狗,翔) 狗.吃(翔)