Email: Zlin85@asu.edu or  Zhicheng.lin1361@gmail.com if you have issues with the code

Here I will give explanations for the codes, how to run them, how to use bash script, and what can you touch in the program

If you want to modify the program, make sure you back up everything first, especially with jason program, one extra { or } or , will cause the entire program to fail


Given files with 
1.studentData.csv
2.TranslationControlFile.csv
3.teacher_control.csv


Overview of all the program
1.main.py   		   	# this one holds all the functions of other program
2.read_student_data.py		# this one will analyze studentData.csv into namedtuple structure
3.translation.py		# this one will convert all the data from TranslationControlFile.csv into namedtuple structure 
4.code_jason.py			# this one will use the namedtuple structure from read_student_data.py and translation.py to code jason and write it into a file

The two program here is currently disabled, because these programs are used for gmails, and now it is using outlook
5.code_html.py			# this program will analyze all the student's data and translation section to generate an html file
6.send_email.py 		# this one will sent the html file as email body


-------------------------------------------------------------------------------------------------------------------------------
To change value in the studentData.csv

For the id section, only modify the first line which is H section, the program will assume all the id will be identical until next H is found.
As for the withdraw date, it follows this format in the H section start from " in the first line, 
-------------------------------------------------------------------------
| 'student_name','school_name','grade','enrolldate','withdrawal_date'	|
-------------------------------------------------------------------------
to add an withdraw date,   here is an example

70465000,70465101,1216,AL79522,3/1/2022,H,000000,"Tom,Littleton School District,8th,08/01/2020,withdraw"
just replace withdraw to be a date, and that would reflect to the program. 


For the O section, here is an exmpale

70465000,70465101,1216,AL79522,3/1/2022,O,B12345,"Tom,math"

to replace the contents for this line, you need to make sure B12345 matches the TranslationControlFile.csv file, also you must keep that B
Because the program will use that B to determine what type it is, then will cut it and only leave the numbers/ words left, then it will 
try to match it in the translated file, once it is found, it will add the sentence over, then will use the extra 2 paramter over. Here it is Tom and math.

Here is an example of the TranslationControlFile.csv

B,12345,&1 is doing well in &2.

here will look it is B type, then look at the id,  then it will use &1 and &2 to be replaced by Tom and math. 
Here it is using comma ,  as an separator 

but what if the sentence has comma , in there? 

example: 
B,32331,"Over the past &1,they have missed &2 days of school."

Using this format, it will be able to separate the sentence correctly, also do not try to put &3, &4.... into the sentence, the program will not recognize it
It will only take &1 and &2.  or just &1 by itself

example:
70465000,70465101,1216,AL79522,3/1/2022,O,B32340,"art"

from translated : 
B,32340,That is the reason why failing &1 class.



For the N section
just simply replace the number and match it in the TranslationControlFile.csv file

example: 
70465000,70465101,1216,AL79522,3/1/2022,N,N00001,

from translated:
N,00001,Do a quick 10 minute behavior check.,https://www.youtube.com/watch?v=Qcb3iC8ZVb8,https://www.youtube.com/watch?v=E_AhudFZnM0

make sure you keep that N, because it will be used to identify what type it is, and just replace the number will be good. 
Also it is using comma , as separator . For the 2 link after the sentence, it was using in the code_html.py section, just keep it in case later you want to sent gmail with 3rd party link
if you don't want use the link, just replace it by 1. It must have something in there, otherwise the array in the program will have issue. 


For the P section, the process is same for the N 

example:
70465000,70465107,1321,AM58078,3/1/2022,P,Pworld_history_Captain_Cook,

translated:
P,world_history_Captain_Cook,https://www.youtube.com/watch?v=2yXNrLTddME&list=PLBDA2E52FB1EF80C9&index=27

you must keep the P in the example, and add whatever you want after it. If you remove P in Pworld_history_Captain_Cook, and becomes world_history_Captain_Cook, the program will not be able to undertand it
it must be Pworld_history_Captain_Cook, then program can use that P to match type and find link for it. 



---------------------------------------------------------------------------------------------------------------------------------------
For the TranslationControlFile.csv section
make sure the file does not have an empty line in the end, if it has an empty line, it may cause some weird issues. 

For the teacher_control.csv
Currently it is not used, because now it is doing outlook and not gmail
for gmails, it will check the week limits and how many has sent already, if exceed the limit, it will stop sending, and will update accordingly



For the password.txt file, you only use it if you are doing gmail, otherwise you can ignore it.
It is used in the send_email.py section, you will need to replace the example@gmail.com to be you gmail, and put password into the password.txt file
Because google is making gmails more secure, you need to go to security in you gmail account setting, and enable app password, so you can just use the code generated as a password and login to the account.


--------------------------------------------------------------------------------------------------------------------------------
Explaning the bash script and Makefile


Makefile is simply making python files to be executable and treat them as a whole program. 
Do not try to modify the Makefile, it is also sensitive, because space and tab can cause it to fail, make sure backup first.

For the bash script, it is basically running linux command but in a file. The extension for bash file ends with sh.
Every bash script must have 
#!/bin/bash
in the first line

to comment thing out in bash file, use #

for the auto.sh
it is basically calling Makefile to set all files to be executable, then it will run the program and clean up the files, otherwise your directory will have too many files all at once.
It can also calling other bash script, just like 
bash recover.sh 

To execute bash file you just do 

bash auto.sh



Because we are not using gmail anymore, and send_emails and code_html is not used, you can comment out the bash recover.sh in the auto.sh
in the recover.sh, it is basically copy over the backup file into the current direcotry, it is because in previous gmail setting, once html code
is generated, it will wipe out all data in the studentData.csv and update teacher_control.csv, which is not good for testing purpose.

The recover is just making it easy to recover all the files


rm means remove file
cp means copy a file over to a destination

you can do 
man cp
or
man rm  
to read more details about them

the ~ is just mean the root directory, you can just check you file path and then replace the existing directory path


---------------------------------------------------------------------------------------------------------------------------------------
You can pretty much touch everything in the main.py and just use functions from other program
You should not try to modify anything in the 
read_student_data.py	
translation.py

unless there is some bugs in there and need to be fixed. Make sure you backup everything first then modify them

Both program is using namedtuple with nested array, so read the whole program first, and look carefully about the commented out print statement
it will give you a good idea on how to access the data. Also the program will prints out all the collected data in the array, so make sure
you read the terminal first then look at the code. 

Make sure you understand the nametuple names and which section they corresponds to. 



As for the code_jason.py, only replace the image or server link which I put some comments in the code. Do not try to modify jason codes in there, 
because it is really sensitive, one extra {, }, or comma, period, will cause the entire program to fail, and debugging will be a pain.

you can use zezhao_jason_code.txt to create your own jason 


The old html folder is just display what it looks like after using code_html.py and sent email functions
The backup folder has the program of all functions, but in a big file. You don't need to worry about it.



















