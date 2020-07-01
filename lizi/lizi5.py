def mult_by_five(x):
    return 5 * x


def call(fn, arg):
    """Call fn on arg"""
    return fn(arg)


def squared_call(fn, arg):
    """Call fn on the result of the calling fn on arg"""
    return fn(fn(arg))


def squared_squared_call(fn, arg):
    """Call fn on the result of the calling fn on arg"""
    return fn(fn(fn(arg)))


print(
    call(mult_by_five, 2),
    squared_call(mult_by_five, call(mult_by_five, 2)),
    squared_squared_call(mult_by_five, 2),
    sep='\n',  # '\n'是换行符号，每个结果都新起一行
)
