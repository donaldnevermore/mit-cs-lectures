import random

def conflict(state,nextX):
    '''检查皇后能否被吃'''
    nextY=len(state)
    for  i in range(nextY):
        if abs(state[i]-nextX) in (0,nextY-i):
            return True
    return  False

def queens(num=8,state=()):
    '''只剩一个皇后没放，穷举她的位置，递归太多影响性能'''
    for pos in range(num):
        if not conflict(state,pos):
            if len(state)==num-1:               
                    yield (pos,)
            else:
                for  result in  queens(num,state+(pos,)):
                    yield (pos,)+result  

def  prettyPrint(solution):
    '''美化输出'''
    def line(pos,length=len(solution)):
        return '. '*(pos)+'X '+'. '*(length-pos-1)
    for pos in solution:
        print(line(pos))

def main():
    answer=random.choice(list(queens(10)))
    prettyPrint(answer)

if __name__=='__main__':
    main()