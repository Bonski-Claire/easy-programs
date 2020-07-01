for day in range(1, 3):
    print('你走后的第%d天'% day, 'I miss u.')
    print('Day{},i miss u.'.format(day))
print('如果山还在，请输入1；不在，请输入0')
day=1
shang = int(input('Day{},山在吗？'.format(day)))
while shang == 1:
    print('Day{},panta!'.format(day))
    day +=1
    if day % 100 == 0 :
        print('第{}天了,如果山还在，请输入1；不在，请输入0'.format(day))
        shang = int(input('Day{},山还在吗？'.format(day)))
        if shang == 0:
            print('移了{}天了,终于移走了！哈哈哈哈哈哈!'.format(day - 1))
        else:
            print('都{}天了，山还在!'.format(day))
            print('第{}天,还没移完,今天休息.'.format(day))
            day += 1