'''
<도어락>
-비밀번호4자리입력,
-비밀번호 일치하면 열리고 불일치하면 경고옴.다시시도가능
-4번불일치하는경우,1분간 재시도 불가능
3.프로세스
    0)비밀번호설정
    1) 비밀번호 입력 대기
	2) 비밀번호 입력
	3) 비밀번호 일치 여부 확인
	    3-1) 일치 시 - 4)로 진행
	    3-2) 불일치 시
	        3-2-1) 3번 이하 일 때 1)로 돌아간다
	        3-2-2) 4번 이상 일 때 1분간 잠금상태가 된 후 1로 돌아간다
	        이때 시간얼마나 남았는지 표시해야함
	4) 문이 열린다 :문이열렸습니다.
	5) 절차 반복
'''

import time

# 변수 설정
password = ['0', '0', '0', '0']     # 비밀번호 0000으로 초기화
max_count = 4                       # 최대 입력 시도 횟수
locktime = 60                       # 시도 횟수 초과 시 잠김 시간


def numinput(str):
    # 번호를 입력받아 반환하는 함수
    # 지역 변수 numbers로 번호를 입력받고 전역 변수 password와 동일한 형식으로 변환한다.
    # 입력받은 값이 모두 숫자이고 password와 길이가 일치하면 numbers를 반환한다.
    # 입력 실패 시 False를 반환한다.
    # 인자 str은 함수 input을 통해 입력받을 때 출력되는 메세지이다.
    # 비밀번호 길이(자리수) 조건에 len(password)를 사용한 이유는 password의 길이를 변경해도 대응하기 위함이다.

    global password  # 전역 변수 password 선언

    numbers = input(str)
    numbers = numbers.replace(' ', '')   # 입력받은 string의 공백 제거

    if numbers.isdecimal() and len(numbers) == len(password):
        numbers = list(numbers)     # ['1234']를 ['1', '2', '3', '4']로 변환
        return numbers
    else:
        return False


def pwset():
    # 비밀번호 설정함수
    # 함수 numinput을 통해 비밀번호를 입력한다.
    # 비밀번호 변경 성공시 True, 실패시 False를 반환한다.

    global password  # 전역 변수 password 선언
    pwinput = numinput('설정할 비밀번호 %d자리를 입력하세요.\n -> ' % len(password))
    if pwinput:
        password = pwinput
        return True
    else:
        return False


def keyinput():
    # 키 입력 함수
    # 함수 numinput을 통해 키를 입력한다.
    # 비밀번호 일치시 True, 불일치 또는 실패시 False를 반환한다.

    global password  # 전역 변수 password 선언
    key = numinput('비밀번호를 입력하세요.\n -> ')

    if key == password:
        return True
    else:
        return False


def securityalert(locktime):
    # 도어락 잠김 함수
    # 경고와 함께 time 시간 동안 잠김 상태가 된다.
    print('! ! ! ! ! ! ! !\n'
          '!   경    고   !\n'
          '! ! ! ! ! ! ! !\n')

    left_time = locktime
    print('입력 시도 횟수가 초과하여 도어락 잠김 상태가 되었습니다.')
    while left_time:
        print('%02d 초 동안 입력이 불가능합니다' % left_time)
        time.sleep(1)
        left_time -= 1


# ===============================================================
# Main function

# 비밀번호 설정
while pwset() == False:
    print('잘못 입력하셨습니다.')

door_closed = True      # 문 닫힘: True / 문 열림: False
count = 0               # 시도 횟수

# 도어락 실행
while True:
    while door_closed:
        if keyinput():
            door_closed = False
        else:
            count += 1
            print('잘못 입력하셨습니다.\n'
                  '남은 시도 횟수 : %d회' % (max_count - count))
            if count == max_count:
                securityalert(locktime)
                count = 0

    print('문이 열렸습니다.')
    time.sleep(3)
    print('문이 닫혔습니다.')
    count = 0; door_closed = True;      # 문이 닫히고 시도 횟수가 0이 된다.(초기화)
