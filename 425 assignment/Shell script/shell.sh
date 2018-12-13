#!/bin/bash


echo "This app lets you search and view the weather condition over the past few years"
echo "File Path(Enter data.csv)"
read location
echo "Enter day(yyyy-mm-dd) or month(yyyy-mm) or year(yyyy)"
read query
grep "$query" $location
