
echo "For any particular query you have to choose any options from below:  "
echo "1 for City-wise Search"
echo "2 for Light"
echo "3 for Air Quality"
echo "4 for Sound"
echo "5 for Humidity"
echo "6 for Dust"
echo "7 for Day/Month/Year wise"
echo " "
read -p "Enter any option: " option

if [ $option -eq 1 ]
then
    read -p "Enter the city name: " key
    echo "Enter 7 for all data set related to your choosen city"
    echo " "
    read -p "with chosen data set: " x
    grep -w "$key" data.csv | csvcut -c 1,2,3,4,5,6,$x

elif [ $option -eq 2 ]
  then
      awk -F "," '{print $2"           "$4}' data.csv
elif [ $option -eq 3 ]
  then
      awk -F "," '{print $2"           "$5}' data.csv

elif [ $option -eq 4 ]
  then
      awk -F "," '{print $2"           "$6}' data.csv

elif [ $option -eq 5 ]
  then
      awk -F "," '{print $2"           "$7}' data.csv

elif [ $option -eq 6 ]
  then
      awk -F "," '{print $2"           "$8}' data.csv
elif [ $option -eq 7 ]
then
    read -p "Enter your Date(Day/month/Year): " key
    echo "Enter 6 to get all data set related to your Date/Year/Month"
    
    echo " "
    read -p "with chosen data set: " x
    grep -w "$key" data.csv | csvcut -c 1,2,3,4,5,6,$x

else
    echo "Data not found"
fi
