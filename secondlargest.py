n = raw_input()
arr = map(int,raw_input().split())
x = set(arr)
x.remove(max(x))
print x
print max(x)
# arr.sort()
# b = set(arr)
# a = list(b)
#
# if len(a)>2:
#     print a[-2]
# else:
#     print a[-1]

