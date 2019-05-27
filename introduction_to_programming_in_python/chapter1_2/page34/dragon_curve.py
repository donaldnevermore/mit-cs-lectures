def dragon_curve(level: int):
    if level == 0:
        return 'F'
    else:
        prev_pattern = dragon_curve(level - 1)
        next_pattern = ''
        for i in reversed(prev_pattern):
            if i == 'L':
                next_pattern += 'R'
            elif i == 'R':
                next_pattern += 'L'
            else:
                next_pattern += i
        return prev_pattern + 'L' + next_pattern
