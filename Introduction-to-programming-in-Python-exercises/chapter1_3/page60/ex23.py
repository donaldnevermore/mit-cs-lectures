import random
import sys

# 初始筹码
stake = int(sys.argv[1])
# 目标金额
goal = int(sys.argv[2])
# 模拟次数
trials = int(sys.argv[3])
# 每局赢的概率
chance = float(sys.argv[4])
assert 1 > chance >= 0, '请输入正确的概率'
# 下注次数
bets = 0
# 赢的局数
wins = 0


def win_rate(c: float):
    r = random.random()
    if r < c:
        return 0
    else:
        return 1


for t in range(trials):
    cash = stake  # 手中的现金
    while (cash > 0) and (cash < goal):
        bets += 1
        if win_rate(chance) == 0:
            cash += 1
        else:
            cash -= 1
    if cash == goal:
        wins += 1

print(str(100 * wins // trials) + '% 赢的概率')
print('平均下注次数' + str(bets // trials))
