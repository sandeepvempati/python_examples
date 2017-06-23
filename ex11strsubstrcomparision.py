def count_substring(string, sub_string):
    count = 0
    for i in range(len(sub_string),len(string)+1):
        if(string[i-len(sub_string):i] == sub_string):
            count += 1
    return count


# x = 'ABCDCDC'
# print x.split('CDC')
#
print count_substring('ABCDCDC','CDC')

# test = "ABCDCDCDCD"
# print test.lower()
# print test.upper()
# print test.capitalize()
# print test.find("y")
# print test.find('3')
# print len(test)
# print test[1:4]
# print test.split("CDC")