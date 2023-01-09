#!/usr/bin/env python3
from datetime import datetime
import os
import os.path
import collections
import smtplib, ssl
import glob
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase


global_emails=[]
Email_handling = collections.namedtuple('Email_handling',['entity','school_id','student_id','teacher_id','weekly_email','last_processed','notification_sent','emails'])




#-------------------------------------------------------------------
# if users want to use a different account, just change this, the password file is just for hiding purpose
gmail_user="example@gmail.com"
p=open("password.txt",'r')
gmail_password=p.read()
p.close()
#-------------------------------------------------------


def update_teacher_file():
    fp=open("teacher_control.csv",'w')
    x=0
    # here is updating the teacher_file, specifically updating the emails been sent and time of last processed

    while x< len(global_emails):
        fp.write(global_emails[x].entity+","+global_emails[x].school_id+","+global_emails[x].student_id+","+global_emails[x].teacher_id+","+global_emails[x].weekly_email+","+global_emails[x].last_processed+","+global_emails[x].notification_sent+","+global_emails[x].emails)
        
        x=x+1
    fp.close()
    print("Updated the teacher file\n")

    # Here will clear out all the student's data
    fp=open("studentData.csv",'w')
    fp.write("enter your new data, or change it to blank if u have no more data")
    fp.close()


def time_check( x):
    
    #splitting time into digestable pieces

    array=global_emails[x].last_processed.split("-")
    month=int(array[0])
    date=int(array[1])
    year=int(array[2])
    
    # getting current time, and splitting into digestable pieces
    time1=datetime.today()
    time1=time1.strftime("%m-%d-%Y")
    array=time1.split("-")
    new_month=int(array[0])
    new_date=int(array[1])
    new_year=int(array[2])

    # perform time calculation, check if the time has come or not
    year_difference=new_year-year
    month_difference=new_month-month
    date_difference=new_date-date

    total_dates= year_difference*365 +month_difference*30 +date_difference    
    #print(total_dates)
    
    # because we are sending emails weekly, so we use 7
    if total_dates>=7:
        i=0
        while i< len(global_emails):
            print(i)
            
            # matching the email address, updating time, and reset the emails been sent
            # global_emails contains list of Email_handling, and we can access it by use global_emails[x]. something
            if global_emails[x].emails== global_emails[i].emails:
                global_emails[i]=Email_handling(global_emails[i].entity,global_emails[i].school_id,global_emails[i].student_id,global_emails[i].teacher_id,global_emails[i].weekly_email,time1,"0",global_emails[i].emails)
            i=i+1

        return True
    else:
        print("at line "+str(x+1)+" the time has not come yet")
         
        return False





def read_all_email():
    fp=open("teacher_control.csv",'r')
    array=[]

    # here is reading the teacher file, and we are trying to collect all for easy access later on
    # details of Email_handling check on the named tuple above

    for line in fp:
        array=line.split(",")
        emails=Email_handling(array[0],array[1],array[2],array[3],array[4],array[5],array[6],array[7])
        global_emails.append(emails)

    print(global_emails)
    fp.close()



def Sent_email():
    try:

        smtp_server='smtp.gmail.com'
        smtp_port=587

        #trying to find the file first and get email
        os.chdir("/home/z/cse485")
        x=0
        while x<len(global_emails):
            good =False
            
            # here is checking the time is good or not, if not good, that means we have to wait until next week
            if int(global_emails[x].notification_sent)>=int(global_emails[x].weekly_email):

                good=time_check(x)
            else:

                good=True

            if good==True:
                message =MIMEMultipart('mixed')
                message['From']='CSE485 project testing<{sender}>'.format(sender=gmail_user)
                message['Subject']='Report of student'


                attachment=""
                for file in glob.glob(global_emails[x].entity+"_"+global_emails[x].school_id+"_"+global_emails[x].student_id+"_"+global_emails[x].teacher_id+".html"):
                    message['To']=global_emails[x].emails
                    attachment=file
                    body="Below are the report of the student information, if you cannot access the video, just click \"video\" "
                    message.attach(MIMEText(body,'plain'))


                if os.path.exists(attachment):
                    # we are opening the html file and read them, otherwise it will be sent as attachment instead
                    # emails
                    fp =open(attachment)
                    data = fp.read(999999)
                    HTML_section=MIMEText(data,'html')
                    message.attach(HTML_section)
                    fp.close()
                    # this is entire html code stuff, be careful
                    print(data+"\n")
                        
                    with smtplib.SMTP(smtp_server,smtp_port) as server:
                        server.ehlo()
                        server.starttls()
                        server.ehlo()
                        #here is actually login
                       
                        #server.login(gmail_user,gmail_password)
                        #server.send_message(message)
                       
                        server.quit()
                        print("\nsuccessful on sending email")
                        print("recipient   ",global_emails[x].emails.replace("\n",""))
                        
                        # here is checking what html content have we sent and we want remove the local
                        # html file after been sent
                        print(attachment)
                        os.remove(attachment)
                        
                    # updating the contents for the teacher file

                    a=str(int(global_emails[x].notification_sent)+1)
                    time1=datetime.today()
                    time1=time1.strftime("%m-%d-%Y")
                    print(time1)
                    i=0
                    # here is updating the array we have, just because previous we have modified it, and we need to make it to be consistent. 
                    while i< len(global_emails):

                        if global_emails[x].emails==global_emails[i].emails:
                            global_emails[i]=Email_handling(global_emails[i].entity,global_emails[i].school_id,global_emails[i].student_id,global_emails[i].teacher_id,global_emails[i].weekly_email,time1,a,global_emails[i].emails)
                            i=i+1
                        else:
                            i=i+1

                    update_teacher_file()
            x=x+1

    except Exception as ex:
        print("issues",ex)

