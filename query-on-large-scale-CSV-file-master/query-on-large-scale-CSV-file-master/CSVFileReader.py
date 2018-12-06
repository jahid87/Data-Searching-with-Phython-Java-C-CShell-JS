import csv
#timestamp,city,temperature,light,airquality_raw,sound,humidity,dust
with open('data.csv', 'r') as file_reader:
    data_reader = csv.DictReader(file_reader)

    headers = data_reader.fieldnames
    print("Data of different cities")
    print("1 = city")
    print("2 = Day/Month/Year")
    n = input("For searching City-wise data enter 1 and for Day/Month/Year wise enter 2: ")
    print("\n")

    if int(n) == 1:
        user_input = input("Enter the city name")
        flines = file_reader.readline()
        print(flines.rstrip())
        search = file_reader.readlines()

        for i, sline in enumerate(search):
            if user_input.upper() in sline.upper():
                print(sline)



    elif int(n) == 2:
        user_input = input("Search day, month, year")
        flines = file_reader.readline()
        print(flines.rstrip())
        search = file_reader.readlines()

        for i, sline in enumerate(search):
          if user_input.upper() in sline.upper():
            print(sline)



