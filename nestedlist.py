x = []
n = int(raw_input())
for i in range(n):
    name = raw_input()
    score = float(raw_input())
    y = [name,score]
    x.append(y)

print x

for i in x:
    print i[1]

