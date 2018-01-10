import random


def play_game():
    while True:
        print_intro()
        user = get_user_input()
        com = random.randint(1, 3)
        result = calc_result(user, com)
        print_result(result)


def print_intro():
    intro_msg = "가위 바위 보 게임!!!\n\n반가워요~~"
    print(intro_msg)


def get_user_input():
    input_msg = '1. 가위, 2. 바위, 3. 보\n선택하세요(종료=q) : '

    while True:
        input_str = input(input_msg)
        if input_str in ['1', '2', '3', 'q', 'Q']:
            if input_str in ['q', 'Q']:
                print('다음에 또 만나요~')
                exit()
            else:
                user = int(input_str)
                break
        else:
            print('잘못 입력하셨네요. 다시 입력해주세요.')

    return user


def calc_result(user, com):
    if user == com:
        result = 'draw'
    elif (user + 1) % 3 == com % 3:
        result = 'lost'
    elif (user - 1) % 3 == com % 3:
        result = 'win'

    return result


def print_result(result):
    if result == 'win':
        print('이겼습니다!!\n\n')
    elif result == 'draw':
        print('비겼습니다!\n\n')
    elif result == 'lost':
        print('졌어요..\n\n')


if __name__ == '__main__':
    play_game()
