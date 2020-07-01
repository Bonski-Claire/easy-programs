# 所有数字都被认为是True，除了0
print(bool(1))
print(bool(0))
# 所有字符串都被认为是True，除了字符串“”
print(bool("asd"))
# 通常空的序列（字符串，列表和我们尚未看到的其他类型，如元组）是“假的”，其余的是“真实的”）
print(bool(""))

def f(x):
    if x>0:
        print("Only printed when x is positive; x =", x)
        print("Also only printed when x is positive; x = ", x)
    print("Always printed, regardless of x's value; x =", x)
n1 = int(input("n1 = "))
n2 = int(input("n2 = "))
f(n1)
f(n2)

