'''
작성자: 박하람
'''

# 1. 랜덤 숫자 맞추기

import random
number = random.randint(1, 20)
count = 0

while True:
    user = int(input('내가 생각한 숫자를 맞추세요. '))
    if user > number:
        print('숫자가 작아요. 큰 숫자를 다시 넣으세요.')
    elif user < number:
        print('숫자가 커요. 작은 숫자를 다시 넣으세요.')
    else:
        print('정답!')
        break
    count += 1

count += 1
print(count, '회 만에 맞았습니다.', number, '이에요.')

'''
작성자: 김문희
'''

# 1


def guessing():
    import random
    round = 0
    my_number = random.randint(1, 20)
    while True:
        round = round + 1
        n = int(input("내가 생각한 숫자를 맞추세요."))
        if n == my_number:
            print(round, "회만에 맞았습니다.", my_number, "에요")
            break
        elif n > my_number:
            print("숫자가 커요. 작은 숫자를 다시 넣으세요.")
        else:
            print("숫자가 작아요. 큰 숫자를 다시 넣으세요.")


# 2
for i in range(1, 7):
    for j in range(1, i):
        print(" ", end="")
    print("*")

# 3
for i in range(2, 10):
    for j in rnage(2, 10):
        print(i, "*", j, "=", i*j)

# 4
number = []
for i in range(1, 101):
    number.append(3*i)

# 5
bmi_calculator():
h = float(input("당신의 키는(cm)? "))
w = float(input("당신의 몸무게는? "))
bmi = w/((h/100)*(h/100))
print("당신의 BMI 지수는", bmi)
if bmi <= 18.5:
    print("저체중입니다.")
elif bmi > 18.5 and bmi <= 23:
    print("정상입니다.")
elif bmi > 23 and bim <= 25:
    print("과체중입니다.")
elif bmi > 25 and bmi <= 30:
    print("비만입니다.")
elif bmi > 30 and bmi <= 35:
    print("고도비만입니다.")
else:
    print("초고도비만입니다.")
