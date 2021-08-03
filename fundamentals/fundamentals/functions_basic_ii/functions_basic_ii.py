#1. Countdown
def countdown(num):
    countdown_list = []
    for x in range(num, -1, -1):
        countdown_list.append(x)
    return countdown_list

#2. Print and Return
def print_and_return(list):
    print(list[0])
    return(list[1])

#3. First Plus Length
def first_plus_length(list):
    first_value = list[0]
    length = len(list)
    return first_value + length

#4. Values Greater than Second
def values_greater_than_second(list):
    count = 0 
    new_list = []
    for num in list:
        if len(list) < 2:
            return False
        elif num > list[1]:
            count +=1
            new_list.append(num)
    print(count)
    return new_list

#5. This Length, That Value
def length_and_value(size,value):
    empty = []
    empty.append(value) 
    new = empty * size
    return new