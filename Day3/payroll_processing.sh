file="employee.txt"
report="payroll_report.txt"
 
# Create report file with heading
echo "EMPLOYEE PAYROLL REPORT" > "$report"
echo "=======================" >> "$report"
 
tax_calculation() {
 
    if [[ $salary -le 30000 ]]; then
        tax=$((salary * 5 / 100))
 
    elif [[ $salary -ge 30001 && $salary -le 60000 ]]; then
        tax=$((salary * 10 / 100))
 
    else
        tax=$((salary * 15 / 100))
    fi
 
    aftertax_salary=$((salary - tax))
}
 
after_adding_bonus() {
 
    if [[ $salary -le 50000 ]]; then
        bonus=2000
    else
        bonus=5000
    fi
 
    afterbonus_salary=$((aftertax_salary + bonus))
}
 
net_salary() {
    total_salary=$afterbonus_salary
}
 
# Read employee details
while read id name salary
do
    tax_calculation
    after_adding_bonus
    net_salary
 
    echo "ID: $id  Name: $name  Salary: $salary  Tax: $tax  Bonus: $bonus  Net Salary: $total_salary" >> "$report"
 
done < "$file"
 
echo "Payroll report generated in $report"
