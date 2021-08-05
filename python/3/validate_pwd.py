#defines functions for conditions
def length(string):
    return len(string)

def letters(string):
    counter = 0
    for char in string:
        if char.isalpha():
            counter += 1
    return counter

def numbers(string):
    counter = 0
    for char in string:
        if char.isdecimal():
            counter += 1
    return counter

def specials(string):
    counter = 0
    for char in string:
        if not char.isalnum():
            counter += 1
    return counter

#defines functions for operators
def equals(x,y):
    return x==y

def greater(x,y):
    return x>y

def lesser(x,y):
    return x<y

def isValid(password,requirements):
    #create dict using functions above
    conditionDict = {'LEN':length,'LETTERS':letters,'NUMBERS':numbers,'SPECIALS':specials}
    operatorDict = {'=':equals,'>':greater,'<':lesser}

    everythingOk = True

    for requirement in requirements:
        (condition,operator,number) = requirement
        #verify if number is valid
        try:
            if(number<0):
                raise Exception()
        except Exception:
            print('Error! Only whole numbers accepted ')
            return 0

        condFunction = conditionDict.get(condition,'invalid')

        #verify if a valid condition was received
        try:
            if(condFunction=='invalid'):
                raise Exception()
        except Exception:
            print('Error! invalid condition. Use LEN, LETTERS, NUMBERS or SPECIALS')
            return 0

        numberChars = condFunction(password)
        logicFunction = operatorDict.get(operator,'invalid')

        #verify if a valid operator was received
        try:
            if(logicFunction=='invalid'):
                raise Exception()
        except Exception:
            print('Error! invalid operator. Use <,> or =')
            return 0

        logicalOperation = logicFunction(numberChars,number)
        if not logicalOperation:
            everythingOk = False
    return(everythingOk)

        