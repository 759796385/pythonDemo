import re

# 正则字符串用r前缀，无需转移
s = r'ABC\-001'
rex = r'^\d{3}\-\d{3,8}$'
# 匹配成功返回match对象 ，否则返回None
if re.match(rex, '0101-12345'):
    print('ok')
else:
    print('no match')




#预编译正则
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
re_telephone.match('010-12345').groups()