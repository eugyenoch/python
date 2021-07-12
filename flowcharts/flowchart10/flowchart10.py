#Python Flowchart depicting a flow control(conditional) statement
#This material was used for educational purposes only
#Many thanks to Al Swegart
name="Joe"  #optional
while True:
    print('Who are you?')
    name = input()
    if name != name:
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
else:
    print('Access granted.')
