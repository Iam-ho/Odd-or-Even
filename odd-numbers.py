print("Odd Numbers form 1 to 100")
previous_num = 0

for i in range(1,51):
    x_num = previous_num + i
    print("Odd Number is: ", x_num)
    previous_num = i