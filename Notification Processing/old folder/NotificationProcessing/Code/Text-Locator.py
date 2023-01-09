#!/usr/bin/env python3
import os
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


filePath = "studentData.csv"
filePath2= "TranslationControlFile.csv"

header = collections.namedtuple('header',['entity_id','school_id','student_id','teacher_id','record_date','record_type','location_id','date'])

H_record = collections.namedtuple('H_record',['student_name','school_name','grade','enrolldate','withdrawal_date'])
O_record = collections.namedtuple('O_record',['type','text_locator','info'])
N_record = collections.namedtuple('N_record',['type','text_locator'])
P_record = collections.namedtuple('P_record',['type','link'])

H_O_N_P=collections.namedtuple('H_O_N_P',['E','H','O','N','P'])

Translation= collections.namedtuple('Translation',['type','test_locator','content','link','link2'])

Html_output = collections.namedtuple('Html_output',['entity','school_id','student_id','teacher_id','H_output','O_output','N_output','P_output'])

Email_handling = collections.namedtuple('Email_handling',['entity','school_id','student_id','teacher_id','weekly_email','last_processed','notification_sent','emails'])

Global_email = collections.namedtuple('Global_email',['entity','school_id','student_id','teacher_id','message'])

collection_list=[]# this will collect all collect that contains H O N P
collection_translating=[] # this hold the interpreting file for N O P
collection_html_output=[]
gmail_user="zhicheng012@gmail.com"
p=open("password.txt",'r')
gmail_password=p.read()
p.close()

global_html=[]
global_emails=[]


def size_check():
    i=0
    fp=open("Error_report.txt",'w')
    no_bugs=0
    while i< len(collection_list):
        b=0
        found_issue=False
        
        if len(collection_list[i].E.entity_id)>10:
            fp.write("Entity id is more than 10 digits\n")
            fp.write(collection_list[i].E.entity_id)
            fp.write("\n")
            found_issue=True
            no_bugs=1
        if len(collection_list[i].E.school_id)>10:
            fp.write("School id is more than 10 digits\n")
            fp.write(collection_list[i].E.school_id)
            fp.write("\n")
            found_issue=True
            no_bugs=1
        if len(collection_list[i].E.student_id)>10:
            fp.write("Student id is more than 10 digits\n")
            fp.write(collection_list[i].E.student_id)
            fp.write("\n")
            found_issue=True
            no_bugs=1
        if len(collection_list[i].E.teacher_id)>10:
            fp.write("Teacher id is more than 10 digits\n")
            fp.write(collection_list[i].E.teacher_id)
            fp.write("\n")
            found_issue=True
            no_bugs=1
        if collection_list[i].E.record_type!="H":
            fp.write("Reason: Record type is not in match\n")
            fp.write("ISSUE: "+collection_list[i].E.record_type)
            fp.write("\n")
            found_issue=True
            no_bugs=1
        while b<len(collection_list[i].O):
            if collection_list[i].O[b].type!="O":
                fp.write("Reason: Record type is not in match\n")
                fp.write("ISSUE: "+collection_list[i].O[b].type+"\n")
                fp.write(str(collection_list[i].O[b]))
                fp.write("\n")
                found_issue=True
                no_bugs=1
            b=b+1
        b=0
        while b<len(collection_list[i].N):
            if collection_list[i].N[b].type!="N":
                fp.write("Reason: Record type is not in match\n")
                fp.write("ISSUE: "+collection_list[i].N[b].type+"\n")
                fp.write(str(collection_list[i].N[b]))
                fp.write("\n")
                found_issue=True      
                no_bugs=1
            b=b+1
        b=0
        while b<len(collection_list[i].P):
            if collection_list[i].P[b].type!="P":
                fp.write("Reason: Record type is not in match\n")
                fp.write("ISSUE: "+collection_list[i].P[b].type+"\n")
                fp.write(str(collection_list[i].P[b]))
                fp.write("\n")
                found_issue=True
                no_bugs=1
            b=b+1

        if len(collection_list[i].E.location_id)>6:
            fp.write("Location id is more than 6 digits\n")
            fp.write(collection_list[i].E.location_id)
            fp.write("\n")
            found_issue=True
            no_bugs=1
        if found_issue==True:
            fp.write(str(collection_list[i].E))
            fp.write("\n\n\n")
            no_bugs=1
        i=i+1
    
    if no_bugs==0:
        fp.write("No bugs in the input file")
    fp.close()    
    fp =open("Error_report.txt",'r')
    
    fix_file=0
    for line in fp:
        fix_file=fix_file+1
    fp.close()
    if fix_file>1:
        print("\nRead the Error_report.txt file first")
        exit(1) 

def read_all_email():
    fp=open("teacher_control.csv",'r')
    array=[]
    for line in fp:
        array=line.split(",")
        emails=Email_handling(array[0],array[1],array[2],array[3],array[4],array[5],array[6],array[7])
        global_emails.append(emails)
        
    print(global_emails)
    fp.close()
    


def head(array):
    time1 = datetime.today()
    time1 = time1.strftime("%m-%d-%Y")
    E_array=array
    E_list = header(E_array[0],E_array[1],E_array[2],E_array[3],E_array[4],E_array[5],E_array[6],time1)
    return E_list
    

def H_field(array):

    H_array=array
    #print(H_array)
    #print(len(H_array))

    if len(H_array)<13:
        H_list = H_record(H_array[7],H_array[8],H_array[9],H_array[10],"NA")
    else:
        H_list = H_record(H_array[7],H_array[8],H_array[9],H_array[10],H_array[11])
    return H_list

def O_field(array):
    O_array=array
    info_array=[]
    x=7
    while x<len(O_array):
        info_array.append(O_array[x])
        x=x+1
    O_list = O_record(O_array[5],O_array[6],info_array)
    return O_list

def N_field(array):
    N_array=array
    N_list = N_record(array[5],array[6])
    return N_list

def P_field(array):
    P_list = P_record(array[5],array[6])
    return P_list

def Translate(array):
    T_array = array
    
    if len(T_array)==5 and T_array[0]=="N":
        T_list = Translation(T_array[0],T_array[1],T_array[2],T_array[3],T_array[4])
        
    elif len(T_array)==5 and T_array[0]!="N":
        T_list = Translation(T_array[0],T_array[1],T_array[2]+T_array[3],0,0)
    else:
        T_list = Translation(T_array[0],T_array[1],T_array[2],0,0)

    return T_list

def OUTPUTTING():
    x=0
   # print(len(collection_list))
    while x <len(collection_list):
        H_out ="Student: "+collection_list[x].H.student_name.replace("\"","")+"\nSchool: "+collection_list[x].H.school_name+"\nClass Standing: "+collection_list[x].H.grade+"\nEnroll Date: "+collection_list[x].H.enrolldate.replace("\"","")
        if collection_list[x].H.withdrawal_date=="N\A":
            H_out=H_out+"Withdrawl Date: "+collection_list[x].H.withdrawal_date.replace("\"","")
        else:
            H_out=H_out+"\nWithdrawl Date: "+collection_list[x].H.withdrawal_date.replace("\"","")
             
        #print(H_out)

#---------------------------------------------------------------------
        print_list=[]
        a=0
    
        O_out=""

        while a< len(collection_list[x].O):
            print_list.append(collection_list[x].O[a].text_locator.replace("B",""))
            a=a+1
    
        a=0
        while a< len(print_list):
            b=0
            while b< len(collection_translating):
                #print(collection_translating[b].test_locator)
                if print_list[a]==collection_translating[b].test_locator and collection_translating[b].type=="B":
                    #print("found")
                    print_list[a]=collection_translating[b].content    
                    break
                b=b+1
            a=a+1
        #print(len(print_list)) 
        
        #print(collection_list[x].O[0].info)
        a=0
        while a< len(print_list):
            b=0
            while b< len(collection_list[x].O[a].info):
                if b==0:
                    print_list[a]=print_list[a].replace("&1",collection_list[x].O[a].info[b].replace("\n",""))
                else:
                    print_list[a]=print_list[a].replace("&2",collection_list[x].O[a].info[b].replace("\n",""))
                b=b+1
            a=a+1

    

        #print(print_list)
        a=0
        while a<len(print_list):
            O_out=O_out+print_list[a].replace("\n"," ")
            a=a+1

        O_out=O_out.replace("\"","")
        
        #print(O_out)
        
    
#---------------------------------------------------------------------------

        print_list=[] 
        print_list2=[]
        N_out="Each of the following Nudges may help "+collection_list[x].H.student_name.replace("\"","")+" achievement.\n"
        a=0
        while a< len(collection_list[x].N):
            print_list.append(collection_list[x].N[a].text_locator.replace("N",""))
            a=a+1
        
        a=0
        while a< len(print_list):
            b=0
            while b< len(collection_translating):
                #print(collection_translating[b].test_locator)
                if print_list[a]==collection_translating[b].test_locator and collection_translating[b].type=="N":
                    #print("found")
                   
                    print_list[a]=collection_translating[b].content
                    print_list2.append(collection_translating[b].link)
                    print_list2.append(collection_translating[b].link2)
                    break
                b=b+1
            a=a+1
        #print(print_list2)
    
        a=0
        b=0
        while a< len(print_list):
            N_out=N_out+print_list[a]+"\n"    
        
            if b<len(print_list2):
                
                N_out=N_out+print_list2[b]+"\n" 
                N_out=N_out+print_list2[b+1]
                b=b+2
            a=a+1
            
        
       # print(N_out)
        
        P_out=[]
        a=0
        #print(collection_list[x].P[0].link)
        #print(collection_list[x].P)
        while a< len(collection_list[x].P):
            #print(collection_list[x].P[0].link)
            b=0
            while b < len(collection_translating):
                if collection_list[x].P[a].link.replace("P","")==collection_translating[b].test_locator and collection_translating[b].type=="P":
                    P_out.append(collection_translating[b].content)
                    break
                b=b+1
            a=a+1
       # print(P_out)

        out = Html_output(collection_list[x].E.entity_id,collection_list[x].E.school_id,collection_list[x].E.student_id,collection_list[x].E.teacher_id,H_out,O_out,N_out,P_out)
        collection_html_output.append(out)

        x=x+1


def code_html():
   # print(collection_html_output)
    x =0
    #print(collection_html_output[x])
    while x<len(collection_html_output):
        H_array=collection_html_output[x].H_output.split("\n")
        
        #print(collection_html_output[x].N_output)
        N_array=collection_html_output[x].N_output.split("\n")
        
        #print(collection_html_output[x].N_output)
        #print(len(N_array))
        #print(N_array)

        image_address="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiXD5NTptfSn-UBeBWZhH3HvvSt2dhVOTagT5LDZ2Nm01HWmtJkG5qbfRBX3qBtxkI6iA-TF6DtmD8xO-JlcpynMQvfojCEJd-HaQJhKyxrTQPUsD-aYp2C4RcrRHGhwxTn7RbEZF-5udPmTaZQqznb8OYQ2BFunxAZXjYQTPx4d56abj8XAF6TFJu3eA/w583-h97/Capture.JPG"

        fp = open(collection_html_output[x].entity+"_"+collection_html_output[x].school_id+"_"+collection_html_output[x].student_id+"_"+collection_html_output[x].teacher_id+".html",'w')
        head ="<!doctype html> <head> <meta charset=\"utf-8\"> <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"> <link href=\"https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css\" rel=\"stylesheet\" integrity=\"sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3\" crossorigin=\"anonymous\"><link rel=\"stylesheet\" href=\"https://cdn.jsdelivr.net/npm/bootstrap-icons@1.3.0/font/bootstrap-icons.css\"> <link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css\"><title>School Fuel</title></head>"
        
        body="<body><div class=\"container\"><div class=\"row\"><br><br></div><div class=\"row\"><div class=\"col-2\"></div><div class=\"col-6\"> <img src=\""+image_address+"\"style=\"height: 140px;width: auto ;\" alt=\"School Fuel image\" ></div>"
    
        #print(len(H_array))
        student_info= "<div class=\"col-3\"><p>"
        a=0
        while a< len(H_array):
            if a+1<len(H_array):
                student_info=student_info+H_array[a]+"<br>"
            else:
                student_info+H_array[a]+"</p></div>"
            a=a+1
        student_info=student_info+"<div class=\"col-2\"></div></div><br><div class=\"row\"><div class=\"col\"></div><hr style=\"width:65%;height: 10px;background-color: red;\"><div class=\"col\"></div></div><br>"
       
        detailed_resut="<div class=\"row\"><div class=\"col\"></div><div class=\"col-7\"><p style=\"text-align: left;\"><br>"+collection_html_output[x].O_output+"<br><br></p></div><div class=\"col\"></div></div><br><div class=\"row\"><div class=\"col\"></div><hr style=\"width:65%;height: 3px;color: gray;\"><div class=\"col\"></div></div><br>"

       
        nudges = "<div class=\"row\"><div class=\"col\"></div><div class=\"col-4\"><div style=\"text-align: center;\"><strong style=\"text-align: center;color: red;\">NUDGES</strong></div><br><p>"
        nudges=nudges+N_array[0]+"</p><ol>"
        


        nudge_link_comment="https://i0.wp.com/insidetimeshare.com/wp-content/uploads/2016/08/no-availability.jpg?fit=283%2C178&ssl=1"



        nudge_style="width=30x\"" 

        
        nudge_up_symbol="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi04RZWEFEtaK-5MxM8SPLmhgyJGPa9RfVACn9mopni0Jr6r0lthd2LYz8akn-Sj4W-2273tS5hGXuVILiKIb405VQZxzp-5Tuv6dgiOj_AFDgm4js_L9y7TOYGIRUuer4hE0npvm_BTEqfqk8ceFuSqQheUMTwCqMv43pM1xBft56Sr6PR1sxtNNrtYQ/s1600/Thumbs%20Up.png"
        nudge_down_symbol="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEif9F92FAB2wpM6FpEafrC7cA6PrcjUplezHaTl-xzYUralIsyqZlQgOx4pkg6ka6JEWgPuUXWc_hZ238qvmsrzNteTM0vfNcGyolhZQHi_3r2K_hvBojO2QuAQ8GKx3G5IXELBSlgSGirhX7bZd26H6ZWOaWKtqqvAzOXums7ei3BK3Nur-gxjbU212w/s1600/Thumbs%20Down.png"
        nudge_comment_symbol="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgC_jrSXfv8YW7PJ9BBcl95wmLcWfmluYqvCKCAMm_MFCcvzqcP-_GZvtN-x8Zd9-sIFpBJa_HQKHFGuQ59T1ifBP6t9LdgV89RpPogAVe9Gs-IN2Dcrc5RgSxb-v7t_mOF9mxdLsXfMJSDDTs1TwS6OOWiN1WP37hGqpWNxrMmfYo3o3NbnEZ99wI0uw/s1600/Feedback.png"



        a=1
        #print(N_array)
        #print("separate")
        while a<len(N_array)-2:
            nudge_link_thumbs_up=N_array[a+1]
            nudge_link_thumbs_down=N_array[a+2]   

            nudges=nudges+"<li>"+N_array[a]+"</li>"+"<a href=\""+nudge_link_thumbs_up+"\"target=_blank ><img src=\""+nudge_up_symbol+"\""+nudge_style+"></i></a>"
            nudges=nudges+"<a href=\""+nudge_link_thumbs_down+"\" target=_blank><img src=\""+nudge_down_symbol+"\""+nudge_style+"></i></a><a href=\""+nudge_link_comment+"\"target=_blank><img src=\""+nudge_comment_symbol+"\""+nudge_style+"></i></a>"
            a=a+3
        nudges=nudges+"</ol></div>"
        #print(nudges)
        
        professional_development= "<div class=\"col-4\"> <div style=\"text-align: center;\"><strong style=\"text-align: center;color: red;\">PROFESSIONAL DEVELOPMENT </strong></div><br>"

        

        video_info_to_be_putted=" lecturing videos or study music"
        
        column ="<div class=\"col-5>"
        width="240px"
        height="150px"


        a=0
        
        while a<len(collection_html_output[x].P_output):
            professional_development=professional_development+column+"<div class=\"row\"><p><a style=\"color: black;\" href=\""+collection_html_output[x].P_output[a]+"\"target=_blank>Video</a>:"+video_info_to_be_putted+"</p></div>"
            
            professional_development=professional_development+"<div class=\"col-3\"><iframe  style=\"width:"+width+";height: "+height+";\" class=\"embed-responsiveitem\"src=\""+collection_html_output[x].P_output[a]+"\"title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen></iframe> </div> "
            a=a+1
        
        #print(professional_development)
        
        end = "</div><div class=\"col\"></div></div><br><div class=\"row\"><div class=\"col\"></div><hr style=\"width:65%;height: 3px;color: gray;\"><div class=\"col\"></div></div></div>"
        message = head +body+student_info+detailed_resut+nudges+professional_development+end
        
        email=Global_email(collection_html_output[x].entity,collection_html_output[x].school_id,collection_html_output[x].student_id,collection_html_output[x].teacher_id,message)
        global_html.append(email)
        
        
        fp.write(message)
                 
        #    os.remove(collection_html_output[x].school_id+".html")
        
        fp.close()
        x=x+1


def update_teacher_file():
    fp=open("teacher_control.csv",'w')
    x=0
    while x< len(global_emails):
        fp.write(global_emails[x].entity+","+global_emails[x].school_id+","+global_emails[x].student_id+","+global_emails[x].teacher_id+","+global_emails[x].weekly_email+","+global_emails[x].last_processed+","+global_emails[x].notification_sent+","+global_emails[x].emails)
        
        x=x+1
    fp.close()
    print("Updated the teacher file")

    fp=open("studentData.csv",'w')
    fp.write("enter your new data, or change it to blank if u have no more data")
    fp.close()

def time_check( x):
    
    array=global_emails[x].last_processed.split("-")
    month=int(array[0])
    date=int(array[1])
    year=int(array[2])
    
    time1=datetime.today()
    time1=time1.strftime("%m-%d-%Y")
    array=time1.split("-")
    new_month=int(array[0])
    new_date=int(array[1])
    new_year=int(array[2])

    year_difference=new_year-year
    month_difference=new_month-month
    date_difference=new_date-date

    total_dates= year_difference*365 +month_difference*30 +date_difference    
    #print(total_dates)
    
    if total_dates>=7:
        i=0
        while i< len(global_emails):
            print(i)
            if global_emails[x].emails== global_emails[i].emails:
                global_emails[i]=Email_handling(global_emails[i].entity,global_emails[i].school_id,global_emails[i].student_id,global_emails[i].teacher_id,global_emails[i].weekly_email,time1,"0",global_emails[i].emails)
            i=i+1

        return True
    else:
        print("at line "+str(x+1)+" the time has not come yet")
         
        return False

def Sent_email():
    try:
        smtp_server='smtp.gmail.com'
        smtp_port=587
                
        #trying to find the file first and get email
        os.chdir("/home/z/cse485")
        x=0
        while x<len(global_emails):
            good =False
            
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
                    fp =open(attachment)
                    data = fp.read(999999)
                    HTML_section=MIMEText(data,'html')
                    message.attach(HTML_section)
                    fp.close()
                   # print(data)

                    with smtplib.SMTP(smtp_server,smtp_port) as server:
                        server.ehlo()
                        server.starttls()
                        server.ehlo()
                        #server.login(gmail_user,gmail_password)
                        #server.send_message(message)
                        server.quit()
                        print("\nsuccessful on sending email")
                        print("recipient   ",global_emails[x].emails.replace("\n",""))
                        print(attachment)
                        os.remove(attachment)
                    

                    a=str(int(global_emails[x].notification_sent)+1)
                    time1=datetime.today()
                    time1=time1.strftime("%m-%d-%Y")
                    
                    i=0
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

def main():
    
    array=[]
    try:
        fp=open(filePath,'r')
        c=0
        for line in fp:
                                       
            c=c+1
        fp.close()
        if c==1:
            fp1=open("Error_report.txt",'w')
            fp1.write("enter your new data !!!, if no data just make it blank")
            
            fp1.close()
            print("\nRead the Error_report.txt file first")
            exit(1)
        fp=open(filePath,'r')
        H=H_field("0,0,0,0,0,0,0,0,0,0,0,0,0")
        E=head("0,0,0,0,0,0,0,0")
        P=[] 
        O=[]
        N=[]

    except IOError:
        print("The file does not exist, check your file")
        exit(1)
    i=0 
    H_did= False
    O_did = False
    N_did= False
    P_did = False
    
    for line in fp:
        
        array=line.split(",")
            
        #print(array) 
        if array[5].count("H")==1:
            if H_did==True and O_did==True and N_did==True and P_did==True:
                collect=H_O_N_P(E,H,O,N,P)
                collection_list.append(collect)
                O=[]
                N=[]
                P=[]

                H_did= False
                O_did = False
                N_did= False
                P_did = False

            E = head(array)
            H =H_field(array)
            H_did =True
            
            

        elif array[5].count("O")==1:
            O.append(O_field(array))
            O_did= True

        elif array[5].count("N")==1:
            N.append(N_field(array))
            N_did= True

        elif array[5].count("P")==1 :
            P.append(P_field(array))
            P_did =True
    
    if H_did==True and O_did==True and N_did==True and P_did==True:
                collect=H_O_N_P(E,H,O,N,P)
                collection_list.append(collect)
                O=[]
                N=[]
                P=[]

                H_did= False
                O_did = False
                N_did= False
                P_did = False
                    

    fp.close()
    size_check()
    x=0
    while x<len(collection_list):
        print(collection_list[x])
        print("\n\n\n")
        x=x+1
    
#---------------------------------------------------------
    print("Translating the file content now")
    
    try:
        fp=open(filePath2,'r')

    except IOError:
        print("The file does not exist, check your file")
        exit(1)
    for line in fp:
        array=line.split(",")
        collection_translating.append(Translate(array))
    
    
    print(collection_translating)
    print("\n\n")
    OUTPUTTING()

    read_all_email()
    code_html()
    Sent_email()
    
    print("\nBelow are the files not sent")
    for file in glob.glob("*.html"):
        print(file)

main()



