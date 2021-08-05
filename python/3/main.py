from validate_pwd import isValid

password = 'cadence@!23'
requirements = [('LEN','=',11),('SPECIALS','>',1),('LETTERS','>',4),('NUMBERS','<',3)]
print('expected to be true')
print (isValid(password,requirements))
print('\n')

requirements = [('SPECIALS','=',1)]
print('expected to be false')
print (isValid(password,requirements))
print('\n')

requirements = [('LEN','=',11),('SPECIALS','>',2),('LETTERS','>',4),('NUMBERS','<',3)]
print('expected to be false')
print (isValid(password,requirements))
print('\n')

requirements = [('LENS','=',11)]
print('expected to thrown exception')
print (isValid(password,requirements))
print('\n')

requirements = [('LETTERS','>=',11)]
print('expected to thrown exception')
print (isValid(password,requirements))
print('\n')

requirements = [('NUMBERS','>',-11)]
print('expected to thrown exception')
print (isValid(password,requirements))