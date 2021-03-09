from random import randint

for i in range(20):
    dice1=randint(1,6)
    dice2=randint(1,6)
    print('第一个{}，第二个{}，合计{}'.format(dice1,dice2,dice1+dice2))