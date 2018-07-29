import sys
from stdlib_python import stdio

n = int(sys.argv[1])

for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            stdio.write('* ')
        else:
            if j == n - 1:
                break
            stdio.write(' *')
    stdio.writeln()
