x, y = raw_input().split()
y = int(y) + 1
sum = 0
for i in range(1, y):
    sum = sum + int(x * i)
print sum
