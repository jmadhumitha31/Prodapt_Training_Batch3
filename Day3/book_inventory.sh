#!/bin/bash
 
# Store Inventory Management
 
# View all the books
viewall_books(){
        echo "List of all books"
        cat books.txt
}
 
 
# Search for a book
search_book(){
        echo "Enter book id:"
        read bookid
 
        if grep -q "^$bookid," books.txt
        then
                echo "Book found"
                grep "^$bookid," books.txt
        else
                echo "Book not found"
        fi
}
 
 
# Count books out of stock
count_out_of_stock(){
        count=$(awk -F',' '$4=="OutOfStock" {count++} END {print count}' books.txt)
        echo "Out of Stock count: $count"
}
 
 
# Update the stock status
update_stock(){
        echo "Enter book id:"
        read id
 
        echo "Enter new status (Available/OutOfStock):"
        read status
 
        awk -F',' -v id="$id" -v status="$status" 'BEGIN{OFS=","}
        {
                if($1==id)
                        $4=status
                print
        }' books.txt > temp.txt
 
        mv temp.txt books.txt
 
        echo "Stock updated"
}
 
 
# Calculate the total inventory value
total_inventory(){
        total=$(awk -F',' '$4=="Available" {sum+=$5} END {print sum}' books.txt)
        echo "Total Inventory Value: Rs.$total"
}
 
 
# Display books by category
display_book_by_category(){
        echo "Enter category:"
        read category
 
        echo "Books in category: $category"
 
        awk -F',' -v cat="$category" '$3==cat {print}' books.txt
}
 
 
# Find costliest book
costly_book(){
        echo "Costliest Book:"
 
        awk -F',' 'BEGIN{max=0}
        {
                if($5>max)
                {
                        max=$5
                        book=$0
                }
        }
        END{
                print book
        }' books.txt
}
 
 
# Main Menu
while true
do
 
echo
echo "====================================="
echo "     Store Inventory Management"
echo "====================================="
echo "1. View All Books"
echo "2. Search for a Book"
echo "3. Count books that OutOfStock"
echo "4. Update Stock"
echo "5. Calculate the total inventory value"
echo "6. Display books by category"
echo "7. Find Costliest Book"
echo "8. Exit"
 
echo "Enter Choice:"
read choice
 
case $choice in
 
1)
        viewall_books
        ;;
 
2)
        search_book
        ;;
 
3)
        count_out_of_stock
        ;;
 
4)
        update_stock
        ;;
 
5)
        total_inventory
        ;;
 
6)
        display_book_by_category
        ;;
 
7)
        costly_book
        ;;
 
8)
        echo "Thank You"
        exit
        ;;
 
*)
        echo "Invalid Choice"
        ;;
 
esac
 
done 
 
