### python 2.7.* code
import csv      #import csv
import os.path  #import path
data={}         #declare empty dictionary 1
data1={}        #declare empty dictionary 2
# check if a string is a number
def isNumber(num):
    try:
        int(num)
        return True
    except:
        return False
#split a line into word
def getSplit(value):
    s = []
    for x in value:
        if (s == []):
            s = x.split()
        else:
            s = s + [','] + x.split()
    return s
#print search result
def printResult(key, value):
    text=''
    for v in value:
        text = text + ' ' + v
    print key,'            ',text  #key=ETEXT no. text=book details
#remove non-breaking space UTF-8 character from a string
def removeUniSpace(s):
    for x in range(len(s)):
        if ('\xc2' in s[x] or '\xa0' in s[x] ):
            while '\xc2' in s[x]:
                if (s[-1].startswith('\xc2')):
                    s[x] = s[x].replace('\xc2', '')
                else:
                    s[x]=s[x].replace('\xc2', ' ')
            while '\xa0' in s[x]:
                if (s[-1].startswith('\xa0')):
                    s[x] = s[x].replace('\xa0', '')
                else:
                    s[x]=s[x].replace('\xa0', ' ')
    return s
# get search result from dictionary 2
def search(searchKey):
    result = {}      #declare empty dictionary 3
    searchValue = []
    key = ''

    print 'Search Result::\n'
    print 'ETEXT NO.          TITLE and AUTHOR'
# check if searchKey is a ETEXT no
    if(isNumber(searchKey) or searchKey.endswith('C') or searchKey.endswith('B')):
        key=searchKey
        try:
            printResult(key, value=data1[key])    #print result if exist
        except:
            if (key != ''):
                print 'ETEXT not found!!'
    else:   #if searchkey is not a ETEXT no.
        searchValue=searchKey.split()
        #if a match found then the result dictionary will be updated
        for key , value in data1.items():
            count = 0
            for s in  searchValue:
                for v in value:
                    if (s.lower() in v.lower()):
                        count+=1
            if(count == len(searchValue)):
                result[key]=value
        # if a search result exist in the result dictionary then print the output
        if (result != {}):
            for key,value in result.items():
                printResult(key,value)
        else:
            print 'keyword not found!!'
#read the input file and store a line in the dictionary 2 as key=>ETEXT value=>book details
def readFile(inputFile):
    index = 0
    i = 0
    file = open(inputFile,'r')        #open file
    content = csv.reader(file)        #read file data
    for line in content:
        if(line != []):
            i += 1
            data[i] = line            #store the file data into the dictionary 1, line by line

    for key , value in data.items():
        s=getSplit(value)             #get the word list of the line in dictionary 1 value
        s= removeUniSpace(s)          #remove UTF-8 char. from a word

#push dict. 1 value in dict. 2 as ETEXT as key and book details as value
        if( value[0].startswith(' ') or s[0].startswith(' ')):
            tem=data1[index]
            data1[index] =tem + s

        elif (isNumber(s[-1]) == True or s[-1].endswith('C') or s[-1].endswith('B') ):
            index = s[-1]
            data1[index] =  s[:-1]

        else:
            f = s[-1].split()
            if (isNumber(f[-1]) == True or f[-1].endswith('C') or f[-1].endswith('B')):
                index = f[-1]
                data1[index] = s[:-1] + f[:-1]
            elif('by' in s):
                tem = data1[index]
                data1[index] = tem + s
            else:
                printResult('ignored  ## ',s)         #print scrape data, are ignored by the dictionary 2

##############################################

inputFile='GUTINDEX.ALL'   #input file name

if os.path.isfile(inputFile):  #check if file exist
    readFile(inputFile)        #read input file

    print '\n\nType a \'ETEXT No.\' or a \'Book Title\' or \'The Author Name\' To Search a Book.'
    print 'Example:\nETEXT No             TITLE and AUTHOR'
    example = '56900'
    printResult(example, value=data1[example])  # print example output

    while True:
        # read user input
        searchKey = raw_input("\nType Search Keyword: or \'cancle\' to Exit\n")
        if (searchKey.lower() == 'cancle'):
            break
        else:
            search(searchKey)  # get search result for the input
else:
    print "No such file or directory: " + inputFile

