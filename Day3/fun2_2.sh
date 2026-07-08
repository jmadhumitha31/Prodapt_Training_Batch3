add_num(){
	sum=$(($1+$2))
	echo "Sum is : $sum"
}

echo "enter num1:"
read num
echo "enter num2:"
read num1

add_num num num1
