from stdlib_python import stdio
import sys

n = int(sys.argv[1])
ruler = '1'
for i in range(2, n + 1):
    ruler = ruler + ' ' + str(i) + ' ' + ruler
    stdio.writeln(ruler)
