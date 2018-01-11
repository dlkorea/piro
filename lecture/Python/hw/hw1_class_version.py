import random


class UserInterface(object):
    choice_list = ('가위', '바위', '보')

    def get_user_input(self):
        while True:
            """
            str.lower() <- str을 소문자로 변환.
            비슷한 메소드로
            str.upper() <- 대문자로 변환.
            str.title() <- 첫글자만 대문자로 변환.
            """
            input_str = input(self.input_msg).lower()
            if input_str == 'q':
                print('다음에 또 만나요~')
                exit()
            elif input_str in [str(i+1) for i in range(len(self.choice_list))]:
                """
                ** list comprehension **
                [str(i+1) for i in range(len(self.choice_list))] 은 아래와 같다.

                a = []
                for i in enumerate(self.choice_list):
                    a.append(str(i+1))

                아래 for loop보다 위 list comprehension을 통한 리스트 생성이 더 빠르다.
                """
                user_choice = self.choice_list[int(input_str)-1]
                break
            else:
                print('잘못 입력하셨네요. 다시 입력해주세요.')

        return user_choice

    @property
    def input_msg(self):
        input_msg = ''
        """
        enumerate는 Python built-in function 중에 하나로 for loop에서 counter가 필요할
        때 사용한다.

        for i, choice in enumerate(self.choice_list):
            pass

        위 Loop에서 i, choice는 각 Loop에서
        0, self.choice_list[0]
        1, self.choice_list[1]
        ....

        의 값을 갖는다.

        for loop 안에서 배열의 원소 뿐만 아니라 index도 필요한 상황에서 가장 쉽게 떠올릴 수 있는
        코딩 스타일은 아래와 같을 것이다.

        for i in range(len(self.choice_list)):
            print(i, self.choice_list[i])

        이를 enumerate를 사용하여 아래와 같이 사용하면 보다 깔끔하게 작업할 수 있다.

        for i, choice in enumerate(self.choice_list):
            print(i, choice)

        *** 아래는 for i, choice in enumerate(self.choice_list): 에서
        for loop의 제어변수로 2개의 변수 i, choice가 오는 것에 대한 부연 설명 ***

        enumerate(self.choice_list)는 loop마다
        (0, self.choice_list[0])
        (1, self.choice_list[1])
        (2, self.choice_list[2])
        ....

        와 같이 (index, self.choice_list[index]) 형태의 튜플을 제어변수에 할당한다.

        따라서 for t in enumerate(self.choice): 와 같이 제어 변수가 t였다면, 각 Loop에서
        t = (0, self.choice_list[0])
        t = (1, self.choice_list[1])
        와 같이 할당이 되는 형태이다.

        i, j = 1, 2 를 통해 i = 1, j = 2를 할당할 수 있고, 내부적으로는 (i, j) = (1, 2)와
        같이 튜플을 통해 여러 변수를 동시에 할당했던 것과 같은 메커니즘으로

        for i, choice in enumerate(self.choice_list):
            pass

        이렇게 사용할 수 있고, 이는 각 Loop에서
        i, choice = (0, self.choice_list[0])
        i, choice = (1, self.choice_list[1])
        와 같이 할당이 되는 형태라 이해하면 된다.
        """
        for i, choice in enumerate(self.choice_list):
            input_msg += '{0}. {1}'.format(str(i+1), choice)
            if i != len(self.choice_list) - 1:
                input_msg += ', '
        input_msg += '\n선택하세요(종료=q) : '

        return input_msg


class ScoreManager(object):
    score = {
        'win': 0,
        'lost': 0,
        'draw': 0,
    }
    score_msg = "승: {win}, 패: {lost}, 비김: {draw}"

    def append(self, result):
        """
        result의 입력값은 'win', 'lost', 'draw' 중 하나.

        result == 'win'이었다면
        self.score[result] == self.score['win']
        """
        self.score[result] += 1

    def print(self):
        msg = self.render_msg()
        print(msg)

    def render_msg(self):
        return self.score_msg.format(
            win=self.score['win'],
            lost=self.score['lost'],
            draw=self.score['draw'],
        )


class RSPGame(object):
    intro_msg = "가위 바위 보 게임!!!\n\n반가워요~~"
    choice_list = ('가위', '바위', '보')
    confirm_msg = "'{user}'를 내셨군요! 저는 '{com}'을 냈답니다."

    ui = UserInterface()
    score_manager = ScoreManager()

    def start(self):
        while True:
            self.intro()
            self.user = self.get_user_input()
            self.com = random.randint(0, 2)
            self.calc_result()
            self.print_confirm()
            self.print_result()
            self.score_manager.append(self.result)
            self.score_manager.print()

    def intro(self):
        print(self.intro_msg)

    def get_user_input(self):
        """
        list.index(arg) 는 list의 원소 중 arg의 index를 리턴.
        [1,2,3,0].index(0) == 4
        """
        user_choice = self.ui.get_user_input()
        return self.choice_list.index(user_choice)

    def calc_result(self):
        if self.user == self.com:
            self.result = 'draw'
        elif (self.user - 1) % 3 == self.com % 3:
            self.result = 'win'
        else:
            self.result = 'lost'

    def print_confirm(self):
        msg = self.render_confirm_msg()
        print(msg)

    def render_confirm_msg(self):
        return self.confirm_msg.format(
            user=self.choice_list[self.user],
            com=self.choice_list[self.com]
        )

    def print_result(self):
        if self.result == 'draw':
            print('비겼습니다.')
        elif self.result == 'win':
            print('이겼습니다!!')
        else:
            print('졌어요..')


if __name__ == '__main__':
    game = RSPGame()
    game.start()
