import re

fh = open(r"test_email.txt","r").read()
print()
for line in fh.split("\n"):
    print(line)

#re 库正则匹配
# 匹配From行
# 匹配From行中的名称
# 匹配From行中的邮件

match = re.findall("From:.*",fh)
