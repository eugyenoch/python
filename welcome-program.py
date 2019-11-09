#REM Program to welcome a guest to this computer

screen = 'Welcome to this computer'
print(screen)

_name = 'Type your name and press the enter key'
print(_name)

name = input()
if not name:
  print 'Please enter your name in the space above'
 elif name:
  print ('Welcome', name, 'to this computer')
 print()
 
location_name='Hi, howdy; could you let us know your current location in the next line!'
print(location_name)
location=input()
print('Thank you, your entered location is,' location_name)
print()

age_declaration='What is your age?'
print(age_declaration)
age=input()
print('thank you, your entered age is,' age)
print()

print('Your name is,' name, 'Your location is,' location, 'and your age is,' str(age).
'You will be' str(int(age)+1, 'in one year have fun!!!')
