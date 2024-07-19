
calender = {
    '1': 'January',
    '2': 'February',
    '3': 'March',
    '4': 'April',
    '5': 'May',
    '6': 'June',
    '7': 'July',
    '8': 'August',
    '9': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December',

}



def readAndPrint(fileName: str):
    file = open(fileName, 'r+')
    for line in file:
        year, month, co2 = (line.strip().split(','))
        if year.isnumeric():
            print(f'The CO2 emmision for {calender[month]} {year} is {co2}')


# readAndPrint('./csv_data/climate_change_co2 (1).csv')


def readAsDict(fileName: str):
    file = open(fileName, 'r+')

    records = {}

    for line in file:
        year, month, co2 = (line.strip().split(','))
        if year.isnumeric():
            records[f'{year}-{month}'] = co2

    return records


# print(readAsDict('./csv_data/climate_change_co2 (1).csv'))
