#!/bin/bash

cat "data.csv"
echo "all data shows"

echo "Find by Year?"
grep -w "2016" data.csv

echo "Find by Cause?"
grep -w "Accidnets" data.csv

echo "Find by State?"
grep -w "Alaska" data.csv

echo "Find by Deaths?"
grep -w "2880" data.csv

echo "Find by Age?"
grep -w "32" data.csv

exit

