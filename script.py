q = input("Enter your Keyword ")
datafile = open('data.csv')
found = []
for line in datafile:
    if q in line:
        found.append(line)
        qs = ""
        break
    else:
        qs = "Not"
if qs == "Not":
    print(q+" is Not Found ")
else:
    print(found)

