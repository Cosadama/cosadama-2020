'''
# 과제1 - 내가 내려고 한 문제의 의도와는 다름...

print("%7s" % "HONG")
print("%4s" % 273)
print("%9.7s%%" % 153.288)
'''

# 과제2
import random
score_dict = {}

while True:
    for j in range(5):
        score_list = []
        for i in range(3):
            score = random.randint(1, 100)
            score_list.append(score)
        sum = score_list[0] + score_list[1] + score_list[2]
        score_list.append(sum)
        aver = int((score_list[3] / 3) * 100) / 100
        score_list.append(aver)
        score_dict[j] = score_list
    break
