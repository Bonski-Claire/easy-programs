import os

print(os.path.split('/Users/wy lenovo/PycharmProjects/'))
print(os.path.split('/Users/wy lenovo/PycharmProjects'))

string = "hello girl < [www.baidu.com] > byebye"
print(string.split("[")[1].split("]")[0])
c = """say
hello
baby"""
print(c)
print(c.split('\n'))
