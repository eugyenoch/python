class Calculation():
    #choice = 1
    def start():
        print('Choose Menu: ')
        print('1. Addition')
        print('2. Substraction')
        print('3. Exit')
        
        #choice = int(input('Choose: '))
      
    def add():
        a = input('Enter first number: ')
        b = input('Enter second number: ')
        
        addSum = float(a) + float(b)
        print('Addition of ', a, 'and ', b, ' = ', addSum)
    
    def sub():
        a = input('Enter first number: ')
        b = input('Enter second number: ')
        
        addSub = float(a) - float(b)
        print('Substraction of ', a, 'and ', b, ' = ', addSub)
        