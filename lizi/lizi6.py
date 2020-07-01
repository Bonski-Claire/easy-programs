def mod_5(x):
    """Return the ramainder of x after dividing by 5"""
    return x % 5


print(
    'Which number is the biggest?',
    max(100, 51, 14),
    'Which number is the biggest modulo 5?',
    max(100, 51, 14, key=mod_5),
    sep='\n',  # '\n'是换行符号，每个结果都新起一行
)
