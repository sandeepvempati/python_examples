n = int(raw_input("enter a number"))
score_dict = {}
for i in range(n):
    x = raw_input().split(" ")
    name, scores = x[0], x[1:]
    scores = map(float,scores)
    score_dict[name] = scores
query = raw_input()

a = score_dict.get(query)
avg_score = sum(a)/len(a)
print "%.2f" %avg_score

# n = int(raw_input())
# student_marks = {}
# for _ in range(n):
#     line = raw_input().split()
#     name, scores = line[0], line[1:]
#     scores = map(float, scores)
#     student_marks[name] = scores
# query_name = raw_input()
#
# x = student_marks.get(query_name)
# print "%.2f " %round(sum(x)/len(x),2)