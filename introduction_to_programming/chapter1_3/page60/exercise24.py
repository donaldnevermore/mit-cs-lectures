import random
import sys

# 初始筹码
stake = int(sys.argv[1])
# 目标金额
goal = int(sys.argv[2])
# 模拟次数
trials = int(sys.argv[3])
times = int(sys.argv[4])
# 下注次数
bets = 0
# 赢的局数
wins = 0
for _ in range(trials):
    cash = stake  # 手中的现金
    t = times
    while 0 < cash < goal and t > 0:
        bets += 1
        t -= 1
        if random.randrange(0, 2) == 0:
            cash += 1
        else:
            cash -= 1

    if cash == goal:
        wins += 1
        print('赢了')
    elif cash == 0:
        print('输光了')
    else:
        print(f'还剩{cash}赌资')

print(str(100 * wins // trials) + '% 赢的概率')
print('平均下注次数' + str(bets // trials))
