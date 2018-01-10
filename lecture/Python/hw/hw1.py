import random

intro_msg = """가위 바위 보 게임!!!

반가워요~~
"""
input_msg = '1. 가위, 2. 바위, 3. 보\n선택하세요(종료=q) : '
confirm_msg = "'{user}'를 내셨군요! 저는 '{com}'을 냈답니다."
score_msg = "승: {win}, 패: {lost}, 비김: {draw}"

rsp_set = ['가위', '바위', '보']
score = {
    'win': 0,
    'lost': 0,
    'draw': 0,
}


if __name__ == '__main__':
    # 게임 영역
    while True:
        print(intro_msg)

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

        com = random.randint(1, 3)

        print(confirm_msg.format(
            user=rsp_set[user-1],
            com=rsp_set[com-1],
        ))

        if user == com:
            score['draw'] += 1
            print('비겼습니다!\n\n')
        elif (user + 1) % 3 == com % 3:
            score['lost'] += 1
            print('졌어요..\n\n')
        elif (user - 1) % 3 == com % 3:
            score['win'] += 1
            print('이겼습니다!!\n\n')

        print(score_msg.format(
            win=score['win'],
            lost=score['lost'],
            draw=score['draw'],
        ))
