print("My name is {0} and I am in {1}.".format("hiekay", 703))
# 将format后面的内容以此填充
print("My website is {web}.".format(web="hiekay.github.io"))
# {}里面那个相当于一个变量了吧

for num in range(1, 101):
    if num % 7 == 0 or num % 10 == 7:
        continue
    else:
        print(num)
