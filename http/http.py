#!/usr/bin/env python
# coding: utf-8

"""
写一个简单的http服务器用python, 基于socket

"""


import socket

def handle_request(client):
	#recv大于 10240 bufsize的去除
	buf = client.recv(10240)
	print buf
	client.send("HTTP/1.1 200 OK\r\n\r\n")
	client.send("hello world")

def main():
	#创建一个TCP/IP的套接字；AF_INED用于IPv4寻址`  SOCK_STREAM对应传输控制协议（即transmission control protocol, TCP） SOCK_DGRAM(用户数据报协议) user datagram protocol, 即UDP
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#绑定地址(ip、端口)到套接字
	sock.bind(('localhost', 8080))
	#开始TCP监听, 1代表同时最大连接数
	sock.listen(1)

	while True:
		#sock.accept 接受数据
		connection, address = sock.accept()
		handle_request(connection)
		#关闭连接
		connection.close()

if __name__ == '__main__':
	main()
