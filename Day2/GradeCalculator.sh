#input
echo "Enter student name:"
read name

echo "Enter subject1 mark:"
read mark1

echo "Enter subject2 mark"
read mark2

echo "Enter subject3 mark"
read mark3
 
echo "Enter subject4 mark"
read  mark4

echo "Enter subject5 mark"
read  mark5


#total mark
total=$((mark1+mark2+mark3+mark4+mark5))
echo  "Total Mark: $total"

#Average of the student
avg=$((total/5))
echo "Average Mark of the Student: $avg"


#Grade for the Average
if [[ $avg -ge 90 ]]; then
   echo "Grade: A"
elif [[ $avg -le 89 ]] &&
     [[ $avg -ge 75 ]]
then
     echo "Grade: B"
elif [[ $avg -ge 60 ]]
then
     echo "Grade: C"
elif [[ $avg -ge 50 ]]
then
    echo "Grade: D"
else
    echo "Fail"
fi
