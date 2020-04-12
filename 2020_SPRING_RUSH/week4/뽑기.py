# 두번째 트랙 대표 뽑기!
# 룡주가 만든 코드 ^0^

import random
track2 = ['현', '규리', '다은', '유진']
a = random.randint(0, 3)
for i in range(4):
    if i == a:
        print(track2[i], 'Congratz! Now you are the lead of track2!')
