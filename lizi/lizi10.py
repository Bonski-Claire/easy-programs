string = "www.gziscas.com.cn"
print(string.split('.'))
print(string.split('.', 1))
print(string.split('.', 2))
print(string.split('.', 2)[0])
print(string.split('.', 2)[1])
print(string.split('.', 2)[2])

string1, string2, string3 = string.split('.', 2)
print(string1)
print(string2)
print(string3)

