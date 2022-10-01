import socket


def post_data(a):
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    print(a)
    print(host)
    print(ip)
    print('post_data')


def post_data_interval(a):
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    print(a)
    print(host)
    print(ip)
    print('post_data_interval')
