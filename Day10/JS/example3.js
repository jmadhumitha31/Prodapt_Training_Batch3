
let marks=[85,42,76,91,38,67,55,29,80,49];
var passcount=0;
var failcount=0;
var highest=marks[0];
var lowest=marks[0];
for(var i=0;i<marks.length;i++){
    if(highest<=marks[i]){
        highest=marks[i];
    }
    if(lowest>=marks[i]){
        lowest=marks[i];
    }
    if(marks[i]>=50){
      passcount+=1;
      console.log("Student",(i+1),":",marks[i],"- Pass");
    }
    else{
        failcount+=1;
        console.log("Student",(i+1),":",marks[i],"- Fail");
    }
}
console.log("Total passed:",passcount);
console.log("Total Failed:",failcount);
console.log("Highest Mark:",highest);
console.log("Lowest Mark:",lowest);

