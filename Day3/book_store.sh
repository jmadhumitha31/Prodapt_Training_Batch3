file="books.txt"

############################
######VIEW ALL THE BOOKS####
############################
view_books(){
	echo "=================BOOKS==============="

	cat "$file"
}

##########################
#####Search for a book####
##########################
search_book(){
	echo "Enter Book Name:"
	read bname


	if grep -i "$bname" "$file"
	then
		echo "Book found"
	else
		echo "Book not found."
	fi

##########################################
#######Count books that are Out Of Stock###
###########################################

count_OutOfStock(){
	count=$(grep -c "OutOfStock" "$file")

	echo "OutOfStock :$count"
}

update_stock(){
	echo "Enter book Id"
	read id
	sed -i "/^$id,/ s/OutOfStock/Available/" 

;;

2)
search_employee
;;

3)
count_absent
;;

4)
update_attendance
;;

5)
calculate_salary
;;

6)
department_records
;;

7)
highest_salary
;;

8)
echo "Thank You"
break
;;

*)
echo "Invalid Choice"

esac

done


