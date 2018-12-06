import pandas as pd

df = pd.read_csv('data.csv')

month_dict = {
    'january': '01',
    'february': '02',
    'march': '03',
    'april': '04',
    'may': '05',
    'june': '06',
    'july': '07',
    'august': '08',
    'september': '09',
    'october': '10',
    'november': '11',
    'december': '12'
}


def search_by_city(data_frame):
    city_name = input("Please enter the name of a city: ")
    print(data_frame[data_frame['city'] == city_name])


def search_by_year(data_frame):
    year = input("Please enter a year: ")
    print(data_frame[data_frame['timestamp'].str.contains(year)])


def search_by_month(data_frame):
    month = input("Please enter a month: ").lower()
    print(data_frame[data_frame['timestamp'].str.split('T') == month_dict[month]])


def search_by_specific_date(data_frame):
    date = input("Please enter a specific date: ")
    print(data_frame[data_frame['timestamp'].str.contains(date)])


def search_by_date_and_city(data_frame):
    city_name = input("Please enter the name of a city: ")
    date = input("Please enter a specific date (Example: 2015-01-07): ")
    print(data_frame[data_frame['timestamp'].str.contains(date) & data_frame['city'].str.contains(city_name)])


user_choice = int(input("Please choose an option: \n1. Search by city name\n2. Search by date\n3. Search by both city "
                        "and date\n"))

if user_choice == 1:
    search_by_city(df)
elif user_choice == 2:
    type_of_date = int(input("Please choose 1 from below: \n1. By year\n2. By month\n3. A specific day ("
                             "Example: 2015-01-07)\n"))
    if type_of_date == 1:
        search_by_year(df)
    elif type_of_date == 2:
        search_by_month(df)
    else:
        search_by_specific_date(df)
elif user_choice == 3:
    search_by_date_and_city(df)
