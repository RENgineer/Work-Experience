#!/bin/bash

YEAR=$(date +%Y)
JNUM=$(date +%j)
JDATE=$(date +%Y%j)
NO_ZERO_JNUM=$(date +%-j)
OLD_YEAR="$((YEAR-1))"
LEAST_NUM_DAYS=46
#CUR_YEAR="The current year is ${YEAR}." 
#CUR_JUL="The elapsed number of days since the beginning of the year is ${JNUM}."
CUR_DATE="The current Julian date is "
OLD_DATE="$((JDATE-45))"
#echo $OLD_DATE old date
EPOCH=$(date +%s) #epoch of today
LEN_EPOCH=${#EPOCH}
#echo $LEN_EPOCH LEN_EPOCH
TIME_STAMP=$(date +%H:%M:%S)
TIME_DATE_STAMP=$(date +%c)
CUR_EPOCH="The epoch representation of today's date is ${EPOCH}."
DATE_DIFF="$(((JDATE)-(NO_ZERO_JNUM)))" #this notation subtracts variables from each other
LEAP_YEAR_PAST="$((OLD_YEAR%4))"
LEAP_YEAR_PRESENT="$((YEAR%4))"
DAYS_IN_SECONDS=3888000
#STAT=12284562738
#N=`echo "${STAT:0: $LEN_EPOCH}"|bc -l`
#echo $N N
DAYS_AGO_EPOCH="$((EPOCH-3888000))" #epoch time in seconds of 45 days ago
#PAST_EPOCH=$(date 1587061916 * 1000)
SEVEN=7
YEAR_MAX="$YEAR""366"
#echo $YEAR_MAX
YEAR_MIN="$YEAR""000"



#VAR=`echo ${DAYS_IN_SECONDS: -5}|bc -l` # this can print the last part of a string
#echo $VAR VAR

#echo $PAST_EPOCH
#echo $YEAR YEAR  
#S_SIZE=${#CUR_DATE} #determines the length of a string, including whitespace characters
#echo "$S_SIZE" S_SIZE
#echo $JNUM JNUM 
#echo $NO_ZERO_JNUM NO_ZERO_JNUM
#echo $JDATE JDATE 
#echo $JDATE_DECIMAL JDATE_DECIMAL 
#echo $CUR_YEAR CUR_YEAR
#echo $CUR_JUL CUR_JUL
#echo $CUR_DATE CUR_DATE 
#echo $LEAST_NUM_DAYS LEAST_NUM_DAYS
#echo $EPOCH EPOCH #time since 1/1/1970 in seconds
#echo $DAYS_AGO_EPOCH DAYS_AGO_EPOCH #45 days ago in seconds
#echo $TIME_STAMP TIME_STAMP 
#echo $TIME_DATE_STAMP TIME_DATE_STAMP
#echo $CUR_EPOCH CUR_EPOCH
#echo $DATE_DIFF DATE_DIFF - YYYY000

#echo $OLD_DATE OLD_DATE 
#echo $LEAP_YEAR LEAP_YEAR
#echo $LEAP_YEAR_PRESENT LEAP_YEAR_PRESENT
#if [ "${JDATE:4:6}" -gt "001" ] && [ "${JDATE:4:6}" -lt "150" ]
#then
#    echo Yes, this works
#else
#    echo No, this is incorrect
#fi


#octal numbers begin with "0"; the numbers they represent are not the same as the
#decimal numbers intended. Stripping the zero from the beginning of the number, should
#one exist, is crucial. This must be done separately for numbers 1-9 and 10-99, as the
#former group has representations with two leading zeros while the latter group only has
#one.

#echo "$((NO_ZERO_JNUM-365))"
#echo "$((365-92))"
#echo "$((NO_ZERO_JNUM-1))"
read -p "Enter a file for output. " OUTPUT_FILE

if [ "$NO_ZERO_JNUM" -gt "$LEAST_NUM_DAYS" ] #-gt for accuracy; if 45 days ago in the same yr
then
    echo "${CUR_DATE}${JDATE}." > $OUTPUT_FILE
    NEW_JDATE="$((JDATE-45))"
    echo "The Julian date 45 days ago was ${NEW_JDATE}." >> $OUTPUT_FILE
    #echo $NEW_JDATE NEW_JDATE #, the day 45 days ago

    if [ "$LEAP_YEAR_PRESENT" == "0" ] #if the current year is a leap year...
    then
	
	    if [ "$NEW_JDATE" -gt "$DATE_DIFF" ] #if 45 days ago is in the same year; 20YY001
	    then
		#echo $YEAR
		DAY_LEAP="$((DATE_DIFF+60))" #February 29th, 20YY060
		#echo $DAY_LEAP - this is YYYY060
		#echo "$((DAY_LEAP+1))" - this is YYYY061 
		if [ "${NEW_JDATE:4:6}" -lt "32" ]
		then
		    MONTH="January"
		elif [ "${DAY_LEAP}" -eq "${NEW_JDATE}" ]
		then
		    DAY_SPEC="Since this is a leap year, the date 45 days ago was February 29th, ${YEAR}."
		elif (( $(echo "${NEW_JDATE:4:6} > 31"|bc -l) )) && (( $(echo "${NEW_JDATE} < $((DAY_LEAP+1))"|bc -l) ))
		then
		    MONTH="February"
		elif [ "${NEW_JDATE}" -gt "${DAY_LEAP}" ] && [ "${NEW_JDATE:5:6}" -lt "93" ]
		then
		    MONTH="March"
		elif [ "${NEW_JDATE:4:6}" -gt "92" ] && [ "${NEW_JDATE:5:6}" -lt "123" ]
		then
		    MONTH="April"
		elif [ "${NEW_JDATE:4:6}" -gt "122" ] && [ "${NEW_JDATE:5:6}" -lt "154" ]
		then
		    MONTH="May"
		elif [ "${NEW_JDATE:4:6}" -gt "153" ] && [ "${NEW_JDATE:5:6}" -lt "184" ]
		then
		    MONTH="June"
		elif [ "${NEW_JDATE:4:6}" -gt "183" ] && [ "${NEW_JDATE:5:6}" -lt "215" ] 
		then
		    MONTH="July"
		elif [ "${NEW_JDATE:4:6}" -gt "214" ] && [ "${NEW_JDATE:5:6}" -lt "246" ]
		then
		    MONTH="August"
		elif [ "${NEW_JDATE:4:6}" -gt "245" ] && [ "${NEW_JDATE:5:6}" -lt "286" ]
		then
		    MONTH="September"
		elif [ "${NEW_JDATE:4:6}" -gt "285" ] && [ "${NEW_JDATE:5:6}" -lt "317" ]
		then
		    MONTH="October"
		elif [ "${NEW_JDATE:4:6}" -gt "316" ] && [ "${NEW_JDATE:5:6}" -lt "347" ]
		then
		    MONTH="November"
		elif [ "${NEW_JDATE:4:6}" -gt "346" ]
		then
		    MONTH="December"
	        fi
		
		CALENDAR_MNTH_YR="Since this is a leap year, this day was in ${MONTH} ${YEAR}."
	    fi

	    if [ "$MONTH" != "" ]
	    then
	        echo $CALENDAR_MNTH_YR >> $OUTPUT_FILE
	    else
		echo $DAY_SPEC >> $OUTPUT_FILE
	    fi

    elif [ "$LEAP_YEAR_PRESENT" != "0" ] #if the current year isn't a leap year..
    then
	echo $YEAR
	DAY_NO_LEAP="$((DATE_DIFF+60))" #March 1st, 20YY060
	echo $DAY_NO_LEAP
        CALENDAR_DATE="Since this is not a leap year, this day was in ${MONTH} ${YEAR}."
    fi



    echo "Similarly, the epoch representation of this date is ${DAYS_AGO_EPOCH}." >> $OUTPUT_FILE
#program the above to say "or DD/MM/YYYY"?

#elif [ "$((OLD_YEAR%4))" == "0" ] #if the previous year was a leap year...
#then
#    echo $CUR_DATE$OLD_YEAR"$((366+(NO_ZERO_JNUM)-45))"
#else
#    echo $CUR_DATE$OLD_YEAR"$((365+(NO_ZERO_JNUM)-45))"
fi

#variables only exist after they have been declared and passed through EITHER
#locally or globally, as shown below:

#echo "The Julian date is ${OLD_YEAR}${JNUM}" #line 37
#echo "${((JNUM-045))}"
#echo "$((JDATE-45))"

#45 days or more prior to a specified date (based on user input):

#read -p "Would you like to find a date 45 days ago from a date other than today? Answer y/n" ANSWER

#    case "$(ANSWER)" in
#	[yY]|[yY] [eE] [sS]) 
#	    read -p "Enter a new date in the form MM/DD/YYYY." NEW_DATE
#	    case NEW_DATE[0]=0)
#	        echo "The month is neither October, November, nor December."
#	         NEW_DATE[0]=1)
#	        echo "The month is either October, November, or December."
      
#	*)
	    
#    case
#	[nN]|[nN] [oO])
#	read -p "Exit program? Answer y/n" ANSWER2
#	case "$(ANSWER2)" in
#	    [yY]|[yY][eE][sS])
#		$(C-x-C-c)
#    *)
#    esac

DONE=0

while [ $DONE -lt 1 ]
do

read -p "Would you like to compare instances with a date other than today? \n Answer 'y' for 'yes' or 'n' for 'no'. " RESPONSE

SEVEN=7
YEAR_MAX="$YEAR""366"
#echo $YEAR_MAX
YEAR_MIN="$YEAR""000"

case "$RESPONSE" in
    [yY] | [yY][eE][sS])                                                           
    
    
VALID_DATES=0
    while [ "$VALID_DATES" = "0" ]
    do
	read -p "Enter the first date in Julian format (YYYYDDD). " DATE_ONE
	read -p "Enter the second date in Julian format (YYYYDDD). " DATE_TWO
        LEN_DATE_ONE=${#DATE_ONE}
        #echo $LEN_DATE_ONE date one length
	LEN_DATE_TWO=${#DATE_TWO}
        #echo $LEN_DATE_TWO date two length
	if [ "$LEN_DATE_ONE" != 7 ] || [ "$LEN_DATE_TWO" != 7 ]
	then
	    echo "Either one or both of the dates entered is not in the proper format. Please re-enter these fields."
	elif [ "$DATE_ONE" -gt "$YEAR_MAX" ] || [ "$DATE_TWO" -gt "$YEAR_MAX" ]
	then

            echo "Either one or both of the days entered do not exist. Please re-enter the Julian dates."

    elif [ "$DATE_ONE" -lt "$YEAR_MIN" ] || [ "$DATE_TWO" -lt "$YEAR_MIN" ]
    then
        echo "Either one or both of the days entered do not exist. Please re-enter the Julian dates."
    elif [ "$DATE_ONE" -gt "$JDATE" ] || [ "$DATE_TWO" -gt "$JDATE" ]
    then
        echo "Either one or both of the days has not occurred yet. Please enter valid dates."
	else
	    ((VALID_DATES++))
	fi	
    done 
                                                                            
    VALID_FILE=0
    FILE_EXT=`echo ${OUTPUT_FILE: -4}`
#    echo $OUTPUT_FILE
#    echo $FILE_EXT
#   "bc -l" extension only works with numbers
   
    while [ "$VALID_FILE" == "0" ]
    do 
	if [ "$FILE_EXT" != ".txt" ] && [ "$NEW_FILE_EXT" != ".txt" ] 
	then

	    read -p "Please enter a valid text file with the '.txt' extension. " NEW_OUTPUT_FILE
	    NEW_FILE_EXT=`echo ${NEW_OUTPUT_FILE: -4}`
	    unset OUTPUT_FILE
            OUTPUT_FILE=$NEW_OUTPUT_FILE
#            echo $OUTPUT_FILE OUTPUT_FILE
	else
	    ((VALID_FILE++))
	fi
    done

#    if [ "$OUTPUT_FILE" = "" ]
#    then
#	unset $OUTPUT_FILE
#	$OUTPUT_FILE=$NEW_OUTPUT_FILE
#	echo $OUTPUT_FILE OUTPUT_FILE
#    fi

    #echo $DATE_ONE
    #echo $DATE_TWO
    #echo ${DATE_ONE:0:4}
    #declare -i YEAR_SEP_ONE
    YEAR_SEP_ONE=`echo ${DATE_ONE:0:4}-1970|bc -l` #years since 1970 for DATE_ONE
    #echo $YEAR_SEP_ONE YEAR_SEP_ONE
    YEAR_SEP_TWO=`echo ${DATE_TWO:0:4}-1970|bc -l` #years since 1970 for DATE_TWO
    #echo $YEAR_SEP_TWO YEAR_SEP_TWO
    FIRST_EPOCH_LEAP_YEARS=`echo ${YEAR_SEP_ONE}/4|bc -l` #leap years since 1970 for DATE_ONE
    #echo $FIRST_EPOCH_LEAP_YEARS FIRST_EPOCH_LEAP_YEARS
    SEC_EPOCH_LEAP_YEARS=`echo ${YEAR_SEP_TWO}/4|bc -l` #leap years since 1970 for DATE_TWO
    #echo $SEC_EPOCH_LEAP_YEARS SEC_EPOCH_LEAP_YEARS
    FIRST_MOD=`echo $YEAR_SEP_ONE%4|bc` #captures remainder for years for the first date, if any
    #echo $FIRST_MOD FIRST_MOD
    SEC_MOD=`echo ${YEAR_SEP_TWO}%4|bc` #captures remainder for the second date, if any
    #echo $SEC_MOD SEC_MOD
    FIRST_OVER_FOUR=`echo ${FIRST_MOD}/4|bc -l`
    #echo $FIRST_OVER_FOUR FIRST_OVER_FOUR
    SEC_OVER_FOUR=`echo ${SEC_MOD}/4|bc -l`
    #echo $SEC_OVER_FOUR SEC_OVER_FOUR
    #INT_LP_YRS_ONE=`echo ${FIRST_EPOCH_LEAP_YEARS-FIRST_MOD_OVER_FOUR}|bc -l` #total leap years for date one as a whole integer
    #echo $INT_LP_YRS_ONE INT_LP_YRS_ONE
    #INT_LP_YRS_TWO=`echo ${SEC_EPOCH_LEAP_YEARS-SECOND_MOD_OVER_FOUR}|bc -l` #total leap years for date two as a whole integer
    #echo $INT_LP_YRS_TWO INT_LP_YRS_TWO
    FIRST_DIFF=`echo ${FIRST_EPOCH_LEAP_YEARS}-${FIRST_OVER_FOUR}|bc -l` #total leap years for date one as a whole integer
    #echo $FIRST_DIFF FIRST_DIFF
    SEC_DIFF=`echo ${SEC_EPOCH_LEAP_YEARS}-${SEC_OVER_FOUR}|bc -l` #total leap years for date two as a whole integer
    #echo $SEC_DIFF SEC_DIFF
    SEC_PER_YEAR=31556952
    SEC_PER_LEAP_YEAR=31643352
    SEC_PER_DAY=86400
    REG_YEAR_SEC_ONE=`echo ${YEAR_SEP_ONE}*${SEC_PER_YEAR}|bc -l` #total seconds for all regular years for date one
    #echo $REG_YEAR_SEC_ONE REG_YEAR_SEC_ONE
    REG_YEAR_SEC_TWO=`echo ${YEAR_SEP_TWO}*${SEC_PER_YEAR}|bc -l` #total seconds for all regular years for date two
    #echo $REG_YEAR_SEC_TWO REG_YEAR_SEC_TWO
    LP_YEAR_SEC_ONE=`echo ${FIRST_DIFF}*${SEC_PER_DAY}|bc` #total seconds for extra days in leap years for date one
    #echo $LP_YEAR_SEC_ONE LP_YEAR_SEC_ONE
    LP_YEAR_SEC_TWO=`echo ${SEC_DIFF}*${SEC_PER_DAY}|bc` #total seconds for extra days in leap years for date two
    #echo $LP_YEAR_SEC_TWO LP_YEAR_SEC_TWO
    NEW_YEAR_SEP_ONE_SEC=`echo ${REG_YEAR_SEC_ONE}+${LP_YEAR_SEC_ONE}|bc` #total seconds for all years since 1970 for date one
    #echo $NEW_YEAR_SEP_ONE_SEC NEW_YEAR_SEP_ONE_SEC
    NEW_YEAR_SEP_TWO_SEC=`echo ${REG_YEAR_SEC_TWO}+${LP_YEAR_SEC_TWO}|bc` #total seconds for all years since 1970 for date two
    #echo $NEW_YEAR_SEP_TWO_SEC NEW_YEAR_SEP_TWO_SEC
    
    DAY_SEP_ONE=`echo ${DATE_ONE:4:6}|bc -l`
    DAY_SEP_TWO=`echo ${DATE_TWO:4:6}|bc -l`
    DAYS_IN_SEC_ONE=`echo ${DAY_SEP_ONE}*${SEC_PER_DAY}|bc -l` #total seconds for all days for the first date
    #echo $DAYS_IN_SEC_ONE DAYS_IN_SEC_ONE
    DAYS_IN_SEC_TWO=`echo ${DAY_SEP_TWO}*${SEC_PER_DAY}|bc -l` #total seconds for all days for the second date
    #echo $DAYS_IN_SEC_TWO DAYS_IN_SEC_TWO

    #echo STOP
    #NEWNUM=`echo $DAY_SEP_ONE+3|bc -l` #this works without having the leading zeros
    #echo $NEWNUM
    NEW_DAY_ONE=`echo ${DAY_SEP_ONE}*${SEC_PER_DAY}|bc -l`
    #echo $NEW_DAY_ONE First days IN SECONDS
    NEW_DAY_TWO=`echo ${DAY_SEP_TWO}*${SEC_PER_DAY}|bc -l`
    #echo $NEW_DAY_TWO SECOND DAYS IN SECONDS

    NEW_DATE_ONE=`echo ${NEW_YEAR_SEP_ONE_SEC}+${DAYS_IN_SEC_ONE}|bc -l` #total seconds for DATE_ONE
    #echo $NEW_DATE_ONE NEW_DATE_ONE
    NEW_DATE_TWO=`echo ${NEW_YEAR_SEP_TWO_SEC}+${DAYS_IN_SEC_TWO}|bc -l` #total seconds for DATE_TWO
    #echo $NEW_DATE_TWO NEW_DATE_TWO
    
    
        if (( $(echo "$DATE_ONE<$OLD_DATE"|bc -l) )); #OLD_DATE = 45 days ago
	then
	    echo -n "The first date entered, " >> $OUTPUT_FILE
	    echo -n "$DATE_ONE" >> $OUTPUT_FILE
	    echo ", was more than 45 days ago." >> $OUTPUT_FILE  
	    #output to file
	else
	    echo -n "The first date entered, " >> $OUTPUT_FILE
            echo -n "$DATE_ONE" >> $OUTPUT_FILE
            echo ", was fewer than 45 days ago." >> $OUTPUT_FILE
	    #output to file
	fi

	if (( $(echo "$DATE_TWO<$OLD_DATE"|bc -l) ));
	then
	    echo -n "The second date entered, " >> $OUTPUT_FILE
	    echo -n "$DATE_TWO" >> $OUTPUT_FILE
	    echo ", was more than 45 days ago." >> $OUTPUT_FILE
	    #output to file
        else
	    echo -n "The second date entered, " >> $OUTPUT_FILE
            echo -n "$DATE_TWO" >> $OUTPUT_FILE
	    echo ", was fewer than 45 days ago." >> $OUTPUT_FILE
	    #output to file
	fi
	
	if (( $(echo "$NEW_DATE_ONE" > "$DAYS_AGO_EPOCH"|bc -l) ))
        then
	    echo "The first instance is represented as ${NEW_DATE_ONE:0:$LEN_EPOCH} in epoch time. " >> $OUTPUT_FILE
	   # echo "This is older than the epoch 45 days ago. " >> $OUTPUT_FILE
	    #echo "${DATE_ONE:4:6}"
            #echo "${DATE_TWO:4:6}"
	else
	    echo "The first instance is represented as ${NEW_DATE_ONE:0:$LEN_EPOCH} in epoch time. " >> $OUTPUT_FILE
           # echo "This means that it was less than the epoch 45 days ago. " >> $OUTPUT_FILE

        fi

	if (( $(echo "$NEW_DATE_TWO" > "$DAYS_AGO_EPOCH"|bc -l) ))
	then
	    echo "The second instance is represented as ${NEW_DATE_TWO:0:$LEN_EPOCH} in epoch time. " >> $OUTPUT_FILE
	    #echo "This is older than the epoch 45 days ago. " >> $OUTPUT_FILE

	else

	    echo "The second instance is represented as ${NEW_DATE_TWO:0:$LEN_EPOCH} in epoch time. " >> $OUTPUT_FILE
	    #echo "This means that it was less than the epoch 45 days ago. " >> $OUTPUT_FILE
	fi

EPOCH_DIFF_ONE=`echo ${NEW_DATE_ONE}-${NEW_DATE_TWO}|bc`
#echo $EPOCH_DIFF_ONE EPOCH_DIFF_ONE
EPOCH_DIFF_ONE_ALT=`echo ${NEW_DATE_TWO}-${NEW_DATE_ONE}|bc`
#echo $EPOCH_DIFF_ONE_ALT EPOCH_DIFF_ONE_ALT

	if (( $(echo "$EPOCH_DIFF_ONE" > "$DAYS_IN_SECONDS"|bc -l) )) || (( $(echo "$EPOCH_DIFF_ONE_ALT" > "$DAYS_IN_SECONDS"|bc -l) ))
	then
	    echo "These epochs are more than 45 days apart." >> $OUTPUT_FILE
	else
	    echo "These epochs are fewer than 45 days apart." >> $OUTPUT_FILE
	fi


#    if [ "$DATE_ONE" -gt "$YEAR_MAX" ] || [ "$DATE_TWO" -gt "$YEAR_MAX" ]
#    then

#	echo "Either one or both of the days entered do not exist. Please re-enter the Julian dates."

#    elif [ "$DATE_ONE" -lt "$YEAR_MIN" ] || [ "$DATE_TWO" -lt "$YEAR_MIN" ]
#    then
#	echo "Either one or both of the days entered do not exist. Exiting program."
#        exit
#    elif [ "$DATE_ONE" -gt "$JDATE" ] || [ "$DATE_TWO" -gt "$JDATE" ]
#    then

#	echo "Either one or both of the days has not occurred yet. Exiting program."
#    else
	    
	#echo "One or both of the numbers entered is not in the appropriate format."
#	echo "Run the program again to achieve results."
	#exit
	echo "Process complete. Exiting program."
	((DONE++))
#    fi
    ;;

    [nN] | [nN][oO])

    read "Process complete. Exiting program."
    ((DONE++))
    exit
    ;;

    *)

    read "Please select a valid response."

    ;;
esac

done
