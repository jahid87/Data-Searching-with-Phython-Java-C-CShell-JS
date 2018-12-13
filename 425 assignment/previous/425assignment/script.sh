#!/bin/bash

inputFile=GUTINDEX.ALL             #input file name

if [[ -e $inputFile ]]; then       #check if the file exist
	echo
	echo "Search Using TITLE or AUTHOR or ETEXT NO."
	echo 
	read -p "Enter Search Keyword: " search         #read & set the user input to $search

	result=$(grep -irn "$search" $inputFile | cut -f1 -d:)   #get line numbers of matched keyword 
													#grep -irn => i:--ignore-case; r:--recursive; n:--line-number
													#cut function cut the lines numbers from grep output
else
	echo "File not Found!!"
	exit 1
fi

if [[ -z $result ]]                        #check if $result is empty
then
 	echo "!! sorry no results found :-(" 
else
	echo "** result found in line no:" $result     #print lines nubmer
 	while IFS=' ' read -ra lineResult; do          #lines number split by ' ' & $lineResult is the array of line number
    	for lineNo in "${lineResult[@]}"; do       #loop for every line in $lineResult array
 			line=$(awk "FNR==$lineNo" $inputFile)  #get the line from the input file
 			if [[ $line = *"~ ~ ~ ~"* ]]; then     #if the line contains '~ ~' then continue the loop
 				continue
 			else
 				echo "$line"					   #print the line
 			fi
			while [[ $addline -le 3 ]]; do        #next 3 line loop
				addLine=$(( addLine+1 ))
 				line=$(awk "FNR==$lineNo+$addLine" $inputFile)      #get a line from the input
 				word=$(echo $line | awk '{ print $NF }')            #get last word of the line
 				if echo $word | egrep -q '^[0-9]+$'; then           #if the word is a number then break the loop
 					break
 				elif [[ $line = *"TITLE"* ]] ; then                 #if the line has 'TITLE' word then break the loop
 					break
 				elif [[ $line = "" ]]; then                         #if the line is empty then break the loop
 					break
 				else
 					echo "$line"                                    #print the line
 				fi
			done 			
      	done
 	done <<< "$result"
fi
