check_odd_even(){
	if [[ $(($1%2)) -ne 0 ]]
	then
		echo "$1 is Odd"
	else
		echo "$1 is Even"
	fi
}

echo "Enter the number"
read number
check_odd_even number

reverse_string(){
	str=$1
	rev_str=""
	#echo "$str" | rev
	for (( i=${#str}-1;i>=0;i-- ))
	do
		rev_str="$rev_str${str:$i:1}"
	done
	echo $rev_str
  
}
reverse_string Linux
