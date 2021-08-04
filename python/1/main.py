path = 'file.txt'
separator = ' '

def count_odd(file_name):
    f = open(file_name,'r')
    sequence = f.read().split(separator)
    count = 0
    for number in sequence:
        number = int(number)
        if(number%2):
            count+=1
    return count
    
def count_even(file_name):
    f = open(file_name,'r')
    sequence = f.read().split(separator)
    count = 0
    for number in sequence:
        number = int(number)
        if(~number%2):
            count+=1
    return count
    
def count_if(file_name, count_condition):
    return count_even(file_name) if count_condition=='even' else count_odd(file_name)
    
    
print(count_odd(path))
print(count_even(path))
print(count_if(path,'odd'))