myDict = dict({'victor': 'Computer Science',
              'victor': 'Business Administration',
               "stick-man": 'Electrical Engineering',
               "Emphaty": 'Computer Science',
               "Skikka": "Mechanical Engineering"
               })

print('victor' in myDict)
print(myDict.values())

def checkKey(myDict, key):
    return key in myDict

def checkValue(dict, value):
    return value in dict.values()

print(checkKey(myDict, 'victor'))
print(checkValue(myDict, 'Electrical Engineering'))
