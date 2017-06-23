n = int(raw_input())
integer_list = map(int, raw_input().split())
i = tuple(integer_list)

print hash(i)
print integer_list