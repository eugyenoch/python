#Python Flowchart depicting a flow control(conditional) statement
#This material was used for educational purposes only
#Many thanks to Al Swegart

rain = input("Is it raining? ")
if rain == 'Yes':
    umbrella = input("Do you have an umbrella? ")
    if umbrella == 'No':
        print('Wait, awhile')
    elif umbrella == 'Yes':
        print('Go outside')
elif rain == 'No':
    print('Go Outside')
else:
    print("Go outside")

