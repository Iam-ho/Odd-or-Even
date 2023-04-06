type1 = input("Odd or Even? ")

if type1 == "odd":
    previous_num = 0
    for i in range(1,51):
        x_num = previous_num + i
        print("Odd Number is: ", x_num)
        previous_num = i
elif type1 == "even":
    previous_num = -1
    for i in range(1,52):
        y_num = previous_num + i
        print("Even Number is: ", y_num)
        previous_num = i - 1