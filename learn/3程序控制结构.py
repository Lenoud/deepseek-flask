def two_swer():
    number = input("请输入一个整数！\n>")
    if number.isdigit():
        int_num = int(number)
        if int_num % 2 == 0 and int_num % 3 == 0:
            print(int_num, "能被二和三整除")
        else:
            print(int_num, "不能被二和三整除")
    else:
        print("请输入纯数字！！")


def Air_quality():
    pm25 = input("请输入pm2.5的值\n>")
    if pm25.isdigit():
        int_pm25 = int(pm25)
        if int_pm25 < 35:
            print("空气质量为优")
        elif int_pm25 < 75:
            print("空气质量为良")
        else:
            print("空气质量为污染")
    else:
        print("请输入整数")


#two_swer()
print()
Air_quality()
