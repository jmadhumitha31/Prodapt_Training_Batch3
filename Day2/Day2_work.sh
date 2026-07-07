
#Creating a directory structure
mkdir case_study1
cd case_study1
echo "Directory Created"


#create required files
touch file1.txt
touch file2.txt
echo "hello this is the case study for Linux"> file1.txt
echo "File created successfully"  

#copying the file1 content ti file2
cp file1.txt file2.txt
echo  "File1 is copied succesfullly to file2"

#Rename the  filename
mv file1.txt file1_renamed.txt

#search for files
find . -name "file2.txt"

#set permission on the script
chmod +x file2.txt

#list of files
ls  -l

#compress the project into a .tar.gz archive
mkdir tarfolder
cd tarfolder
touch demo1.txt demo2.txt
cd ..
tar -cvf tarfolder.tar tarfolder

#Extract it into new Location
mkdir recovery
tar -xvf tarfolder.tar -C recovery

#verify the location
ls -l
