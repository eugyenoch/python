#Python Flowchart depicting a flow control(conditional) statement
#This material was used for educational purposes only
#Many thanks to Al Swegart

name = input("What is your name? ")
age = int(input("How old are you? "))
if name == 'Alice':
    print('Hi, Alice.') 
elif age < 12:
    print('You are not Alice, kiddo.')
