weight = int(input('What is the weight of the parcel? '))
location = str(input('Local (L) or International (I)'))

if location == 'I':
    if weight < 5:
        print('That will be £40')
    else:
        print('Overweight')
else:
    if weight < 5:
        print('Local charge ')
    else:
        excess =(weight) - 5
        cost = 20 + excess
        print(cost)


