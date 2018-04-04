def dragonCurve(level):
    if level == 0:
        return 'F'
    else:
        prevPattern = dragonCurve(level - 1)
        nextPattern=''
        for i in reversed(prevPattern):
            if i == 'L':
                nextPattern+='R'
            elif i == 'R':
                nextPattern+='L'
            else:
                nextPattern+=i
        return prevPattern+'L'+nextPattern
