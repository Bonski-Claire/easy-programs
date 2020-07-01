#Demo
#This is a game of jumping 7.
for num in range(1, 101):
    if num % 7 == 0 or num % 10 == 7:
        continue
    else:
        print(num)
