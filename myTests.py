import maths
#addOp = maths.Calculation.sub()
print('\t\t\t Welcome to Base Calculator')
print('-----------------------------------------')
maths.Calculation.start()
choice = int(input('Choose: '))

while (choice != 3):
    if (choice == 1):
        addOp = maths.Calculation.add()
        maths.Calculation.start()
        choice = int(input('Choose: '))
        
    elif(choice == 2):
        addOp = maths.Calculation.sub()
        maths.Calculation.start()
        choice = int(input('Choose: '))
        
    else:
        print('Thank you for using Base Calculator!')

#Loop ends here

print('Thank you for using Base Calculator!')
