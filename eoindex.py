# n = int(raw_input())
# x = []
# for i in range(n):
#     y = raw_input()
#     x.append(y)
# print x
#
# for i in range(0,len(x),3):
#     print x[i+1]
# y = ["sandee","abcdfgr"]
# for x in y:
#     for i in range(0,len(x),2):
#         print i,
#
# for i in range(10):
#     print "%d" %(i)

for n in range(int(raw_input())):
    x = raw_input()
    print x[::2],x[1::2]

#
# for i in range(1):
#     x = "dasfsfds"
#     print x[2::2]
