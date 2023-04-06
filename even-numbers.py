print("Even Numbers from 1 to 100")
previous_num = -1

for i in range(1,52):
    x_num = previous_num + i
    print("Even number is: ", x_num)
    previous_num = i - 1