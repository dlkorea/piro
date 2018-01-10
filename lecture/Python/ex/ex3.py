user_input = int(input('별을 몇개까지? : '))
if user_input % 2 == 0:
    user_input -= 1

row_count = (user_input + 1) // 2


for i in range(row_count):
    blank = row_count - (i+1)
    star = 2*(i+1) - 1

    print(' ' * blank + '*' * star)

for i in range(row_count - 2, -1, -1):
    blank = row_count - (i+1)
    star = 2*(i+1) - 1

    print(' ' * blank + '*' * star)
