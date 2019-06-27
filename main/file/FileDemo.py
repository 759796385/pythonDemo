# r表示读 rb读取二进制  支持第三个参数字符编码
try:
    f = open('/Users/bianlifeng/java_error_in_idea_243.log','r')

    str=f.read()
    #print(str)
finally:
    f.close()


# 写的太繁琐 有语法糖 with
with open('/Users/bianlifeng/java_error_in_idea_243.log','r') as f:
    #readLine 读取一行
    for line in f.readlines():
        print(line.strip()) # 删末尾的换行符
    # print(f.read())  read读取全部内容 太占内存

# 写文件
#with open('/Users/bianlifeng/test.txt', 'w') as f:
#    f.write('Hello, world!')


