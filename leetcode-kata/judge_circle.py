class Solution:
    
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        for i in moves:
            self.move(i)
        if (self.x,self.y)==(0,0):
            return True
        else:
            return False
    def __init__(self):
        self.x=0
        self.y=0
    def move(self,direction):
        if direction=='U':
            self.y+=1
        elif direction=='D':
            self.y-=1
        elif direction=='L':
            self.x-=1
        elif direction=='R':
            self.x+=1
        else:
            print('invalid direction')


a=Solution()
print(a.judgeCircle('LL'))