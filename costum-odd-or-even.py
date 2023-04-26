type1 = input("Odd or Even: ")

if type1 == "odd":
    x_num = int(input("How many Odd numbers do you need form 1? "))
    previous_num = 0
    for i in range(1, x_num):
        num = previous_num + i
        print("Odd number is: ", num)
        previous_num = i
elif type1 == "even":
    x_num = int(input("How many Even numbers do you need from 0? "))
    previous_num = -1
    for i in range(1, x_num):
        num = previous_num + i
        print("Even number is: ", num)
        previous_num = i - 1