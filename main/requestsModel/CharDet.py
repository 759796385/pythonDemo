#乱码如何反推出正式编码？  使用chardet
import chardet
print(chardet.detect(b'Hello, world!'))
#{'encoding': 'ascii', 'confidence': 1.0, 'language': ''} 100%猜测是ascii

data = '离离原上草，一岁一枯荣'.encode('gbk')
print(chardet.detect(data)) 