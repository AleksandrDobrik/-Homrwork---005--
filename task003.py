# Реализуйте RLE алгоритм: реализуйте модуль сжатия  и восстановления данных.
# Входные и выходные данные хранятся  в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc

f = open('text.txt', 'r')
my_string = ''
for line in f:
    my_string = my_string + line
f.close
print(my_string)
def compresses(my_string):
    count = 1
    new_string = ''
    for i in range(0,len(my_string)-1):   
        if my_string[i] == my_string[i + 1] and i == len(my_string)-2:
            count +=1
            new_string  = new_string + str(count) + my_string[i]
        elif my_string[i] == my_string[i + 1]:
            count += 1
        else:
            new_string  = new_string + str(count) + my_string[i]
            count = 1
    return new_string
        
def unclenches(my_string):         
    new_string = ''
    count = ''
    numbers = '0123456789'
    for i in range(0,len(my_string)):
        if numbers.find(my_string[i]) != -1:
            count += my_string[i]
        else:
            new_string += (my_string [i] * int(count))
            count = ''
    return new_string

numbers = '0123456789'
if numbers.find(my_string[0]) == -1:
    new_string = compresses(my_string)
else:
    new_string = unclenches(my_string)


print(new_string)


f = open('end.txt', 'w')
f.write(new_string )
f.close
