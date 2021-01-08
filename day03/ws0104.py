import random

def error():
    print('wrong input... try again\n')

def game(num1,num2):
    """
    ===== Number Guess Game ======
    # 1. 두 자리의 숫자 2개를 입력받는다. (ex, 10 90)
    # 2. 두 수 사이의 랜덤한 숫자를 발생시킨다
    # 3. 넘버 게임을 시작 한다.
    # 4. 숫자를 입력 받아 2번에서 만들어진 숫자를 기준으로 3가지의 조건을 출력한다.
         크다, 작다, 맞다
         2번에서 만들어진 숫자보다 낮은 숫자를 입력하면 Up, 높은 숫자를 입력하면 Down을 출력한다
    # 5. 게임 한 횟수를 화면에 출력한다. (게임 횟수 제한을 둔다. 횟수는 10회)
    # 6. 숫자가 맞으면 새로운 게임을 다시 만들어 시작할 수 있다.
    """
    print('Game start!\n')
    num = random.randint(min(num1,num2),max(num1,num2))
    chance = 10
    while chance > 0:
        print('--- Left chance : %s ---' % format(chance, '02'))
        guess = input('Guess the number : ')
        if guess.isdecimal():
            guess = int(guess)
            if guess == num:
                print('Exact! You Win!\n')
                break
            elif guess < num:
                print('Up!\n')
                chance += -1
            else:
                print('Down!\n')
                chance += -1
        else:
            error()
    if chance == 0:
        print('You Lose... The number is %d\n===== Game Over =====\n' % num)
    return chance

## main function
# print menu
help(game)
while True:
    inputnum = input('input 2 numbers (q : quit, h : help) ')

    if inputnum.lower() == 'q':
        break
    if inputnum.lower() == 'h':
        help(game)
        continue

    inputnum = inputnum.split(' ')
    if len(inputnum) == 2:
        if inputnum[0].isdecimal() and inputnum[1].isdecimal():
            num1 = int(inputnum[0])
            num2 = int(inputnum[1])
            if num1 >= 10 and num1 < 100 and \
                num2 >= 10 and num2 < 100:
                if game(num1,num2) != 0:
                    continue
                else:
                    break
    error()