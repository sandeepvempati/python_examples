def is_leap(year):
    leap = False
    if(year%100 == 0):
        if(year%400 == 0 and year%4 ==0):
            return True
    elif(year%4 == 0):
        return True
    return leap

year = int(raw_input())
print is_leap(year)