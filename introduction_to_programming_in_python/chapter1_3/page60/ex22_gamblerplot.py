import random
import sys

# 初始筹码
stake = int(sys.argv[1])
# 目标金额
goal = int(sys.argv[2])
# 模拟次数
trials = int(sys.argv[3])
# 下注次数
bets = 0
# 赢的局数
wins = 0
for t in range(trials):
    cash = stake  # 手中的现金
    while (cash > 0) and (cash < goal):
        bets += 1
        if random.randrange(0, 2) == 0:
            cash += 1
        else:
            cash -= 1
        print('*' * cash)
    if cash == goal:
        wins += 1

print(str(100 * wins // trials) + '% 赢的概率')
print('平均下注次数' + str(bets // trials))
