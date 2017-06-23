def split_and_join(line):
    temp = line.split(" ")
    temp = "-".join(temp)
    return temp

print split_and_join(raw_input())

