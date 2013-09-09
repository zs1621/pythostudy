#!/usr/bin/env python 
#coding: utf-8

"""
zlib 库是压缩字符串
想把文件压缩为 .gz .zip 就需要用 gzip zip模块
解压.gz .zip拿出里面的文件 一样

如果想 在内存中  解压 .gz文件的流数据 .可以用zlib模块 
这是因为 大部分的gzip或多或少基于zlib压缩，除了一些格式信息。使用zlib做点改变就可以搞定
"""

"""
下面的例子,先用 gzip 模块压缩一个.json文件, 再将压缩过的文件读到内存， 进行解压
"""

import zlib
import gzip

#将ko.json 压缩为 ko.gz
f_in = open('/home/ko.json', 'rb')
f_out = gzip.open('/home/ko.gz', 'wb')
f_out.writelines(f_in)
f_out.close()
f_in.close()


#现在从ko.gz 解压出 ko.json
filecontent = open('/home/ko.gz', 'rb')
dst = open('/home/ok.json', 'wb')
decompress = zlib.decompressobj(16+zlib.MAX_WBITS) #这里的解压对象 参数就是 trick 的地方 
data = filecontent.read(1024) #为了不让内存溢出，每次从文件读出1024字节
while data:
	dst.write(decompress.decompress(data))
	data = filecontent.read()
#解压完  可以看到 ok.json 与 ko.json的内容是一样的
"""
如果觉得文件很小 就不需要在读的时候设置缓存
就去掉 1024 , 如下就好

"""
data = filecontent.read()
dst.write(decompress.decompress(data))
