ruler = '1'
print(ruler)
n = 6

for i in range(2, n + 1):
    ruler = ruler + ' ' + str(i) + ' ' + ruler
    print(ruler)
