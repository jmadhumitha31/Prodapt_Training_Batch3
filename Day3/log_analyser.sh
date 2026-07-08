#function to count the ERRORS
count_errors(){
        echo "Number of error messages: "
        grep -c "ERROR" server.log
}
 
#function to display WARNING messages
show_warning(){
        echo "WARNING messages: "
        grep "WARNING" server.log
}
 
#function to replace ERROR  with CRITICAL
replace_error(){
        echo "Replacing ERROR with CRITICAL..."
        sed 's/ERROR/CRITICAL/g' server.log
}
 
echo "======================================="
echo "           Log File Analyser           "
echo "======================================="
 
count_errors
echo
show_warning
echo
replace_error
