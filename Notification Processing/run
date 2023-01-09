#!/usr/bin/env python3
import glob
from read_student_data import*
from translation import*
from code_html import*
from send_email import*
from code_jason import*



def main():
# In the main it has a total of 4 subclasses, and main is calling the functions in them to accomplish the 
# goal, most of the variables are declares global so it gives quite a lot freedom


    student_info =student_data()# this one will read all the student's data and check if there is any issue in the
                                # file, if so, it will force user to check Error.txt and user won't be able to 
                                # move forward until issue has been resolved.
    print("--------------------------------")    
    print(student_info)    

    print("------------------------- End of student info----------------\n")

    translated_data=translation() # this one is looking at the TranslationControlFile.csv and perform tranlation 
                                  #  for the html file
    read_all_email()           # this one is from send_email.py class, it basically just read all the emails from 
                               # from teacher_control.csv file and start analyzing them for sending email purpose 

    
    #code_html(translated_data)# this one is just a bunch html code, and I am just passing the translated word 
                              #frame into it then the function can start writing an html code
    
    x=0
    while x< len(translated_data):
        code_jason(translated_data,x)
        x=x+1

    #Sent_email()   # sending emails and update student and teacher file, and check if the time or number of emails
                    # exceeded or not
    

    print("\nBelow are the files not sent")
    for file in glob.glob("*.html"):
        print(file)


main()
