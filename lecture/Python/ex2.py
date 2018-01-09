user_input = int(input('몇줄을 출력할까요? : '))

for i in range(user_input):
    count = 2 * (i+1) - 1
    print('*' * count)
