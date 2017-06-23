# def mutate_string(string, position, character):
#     x = list(string)
#
#     #x = x[0:position] + character + x[position:]
#     return x
#
# print mutate_string(raw_input(),raw_input(),raw_input())

def mutate_string(string, position, character):
    x  = list(string)
    temp = x[0:int(position)] + list(character) + x[int(position)+1:]
    x = "".join(temp)
    return x
string = raw_input()
position, character = raw_input().split(" ")
print mutate_string(string,position,character)