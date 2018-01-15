## 가상환경 구축 방법
virtualenv 와 virtualenvwrapper 가 모두 설치된 상황에서,

```
만들기 : mkvirtualenv 가상환경명
만들어둔 가상환경 진입하기 : workon 가상환경명
가상환경 나오기 : deactivate
```

커맨드라인 젤 왼쪽 끝에 (가상환경 명) 이 뜨면 해당 가상환경에 진입한 상태.

## 가상환경 환경변수 세팅 관련

* ### windows

먼저 c:\dev 에서 Envs라는 디렉토리를 만든 후
(ex. c:\dev에서 mkdir Envs)

```
setx WORKON_HOME c:\dev\Envs
```

c:\dev\Envs는 다른 폴더로 변경하여도 무방.
단 경로 상에 한글 폴더가 있을 경우 에러 발생하니 주의해야함.

* ### mac

mkdir을 이용하여 ~/dev/.envs 와 같은 폴더를 만든 후
(ex. ~/dev에서 mkdir .envs)

```
echo export WORKON_HOME=~/dev/.virtualenvs >> ~/.bash_profile
echo export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3 >> ~/.bash_profile
echo source /usr/local/bin/virtualenvwrapper.sh >> ~/.bash_profile

source ~/.bash_profile
```

먼저 echo와 뒤의 >> ~/.bash_profile 은 ~/.bash_profile에 echo 와 >> 사이에 위치한 내용을 넣으라는 뜻임.

첫줄에서 ~/dev/.envs 가 아닌 다른 경로로 설정하여도 무방.
단, 경로 상에 한글 폴더가 없도록 할 것.

두번째 줄에서 = 뒤의 '/usr/local/bin/python3'는 virtualenvwrapper에서 default로 사용할 python이 설치된 경로.
brew 등을 이용해 python을 새로 설치하였고, 설치된 특정 버전의 파이썬을 사용하고 싶을 경우 원하는 파이썬 경로를 구하여 바꿔주어야 함. 위 명시된 경로는 맥에서 기본적으로 python3가 설치된 경로이니 대부분 이대로 진행해도 무방함.

세번째 줄에서 'source /usr/local/bin/virtualenvwrapper.sh' 부분은 설치한 virtualenvwrapper 관련 설정이 담긴 script를 실행하도록 하는 부분. 이 세번째 줄을 생략할 경우 mkvirtualenv, workon 등의 virtualenvwrapper 명령어들을 실행 시 찾을 수 없는 명령어라 뜸. 따라서 꼭 설정해주어야 함.

네번째 줄은 ~/.bash_profile 을 재 실행 해주는 것.
지금까지 'echo xxx >> ~/.bash_profile' 을 통해 ~/.bash_profile 에 명령들을 추가하였으니 재 실행하여 추가한 명령들이 실행되도록 하기 위함.


* ### 공통
virtualenvwrapper 는 시스템 환경변수에 **WORKON_HOME**이 지정되어 있을 경우 해당 경로에 가상환경을 구축함.
우리가 workon 가상환경이름 으로 접근할 때 **WORKON_HOME**에 지정된 경로에서 가상환경을 검색함.
**WORKON_HOME**을 설정한 후

```
mkvirtualenv 가상환경명
```

으로 가상환경을 구축 시 **WORKON_HOME**에 지정된 경로에 가상환경 이름으로 된 디렉토리를 볼 수 있음.

