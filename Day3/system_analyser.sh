info_count=0
error_count=0
warn_count=0


#Function to analyse log time
analyze_log(){

	line=$1

	if echo "$line" | grep -q "INFO"
	then
		((info_count++))
	elif echo "$line" | grep -q "WARNING"
	then
		((warn_count++))
	else
		((error_count++))
	fi
}
check_status(){
	status=""
if [[ $error_count -gt 10 ]]
then
	status="Critical"

elif [[ $error_count -gt 0 ]];
then
	status="Warning"
else
	status="Healthy"
fi
}



#Read file
echo "Enter log file"
read logfile

if [[ ! -f $logfile ]]
then
	echo "File not exist"
	exit
fi

#LOOP through the file
while read line
do

analyze_log "$line"
done <$logfile


#Detemine status
check_status


#Generate report
{
echo "System Log Analyzer Report"
echo "=========================="
echo "Info count: $info_count"
echo "Warning count: $warn_count"
echo "Error count: $error_count"
echo 
echo "System status: $status"
} > report.txt

echo "Report Generated: report.txt"
