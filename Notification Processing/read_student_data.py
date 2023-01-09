#!/usr/bin/env python3
import os
import os.path
import collections
from os.path import basename
from datetime import datetime

filePath = "studentData.csv"

header = collections.namedtuple('header',['entity_id','school_id','student_id','teacher_id','record_date','record_type','location_id','date'])

H_record = collections.namedtuple('H_record',['student_name','school_name','grade','enrolldate','withdrawal_date'])
O_record = collections.namedtuple('O_record',['type','text_locator','info'])
N_record = collections.namedtuple('N_record',['type','text_locator'])
P_record = collections.namedtuple('P_record',['type','link'])

H_O_N_P=collections.namedtuple('H_O_N_P',['E','H','O','N','P'])
collection_list=[]# this will collect all collect that contains H O N P


def size_check():
    i=0
    fp=open("Error_report.txt",'w')
    no_bugs=0
    # here is just checking the file content size, because some fields has digit limits so we want make sure
    # the input file does not excess the limit, and sometimes the type is not in match we need solve it too
    # all the information about the file will be writting into Error_report.txt, and user must fix them before
    # they can move on

    while i< len(collection_list):
        b=0
        found_issue=False
                                                                                                        
        if len(collection_list[i].E.entity_id)>10:
            fp.write("Entity id is more than 10 digits\n")  # making sure it doesn't exceed the length
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
        while b<len(collection_list[i].O): # here is writing what is the issue and from where
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
        #print(collection_list[i].E.location_id)
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


def head(array):
    time1 = datetime.today() # getting time of the day, so we can see when is the file been processed
    time1 = time1.strftime("%m-%d-%Y")
    E_array=array

    # look at named tuple for the header info
    E_list = header(E_array[0],E_array[1],E_array[2],E_array[3],E_array[4],E_array[5],E_array[6],time1)
    return E_list
    

def H_field(array):

    H_array=array
    #print(H_array)
    #print(len(H_array))

    # sometimes student does not have withdraw day, so I need to set the H_list to be flexible
    if len(H_array)<13:
        H_list = H_record(H_array[7],H_array[8],H_array[9],H_array[10],"NA")
    else:
        H_list = H_record(H_array[7],H_array[8],H_array[9],H_array[10],H_array[11])
    return H_list

def O_field(array):
    O_array=array
    info_array=[]
    x=7
    while x<len(O_array):  # process all the contents for O, look at named tuple for detailed info on what
                            # is the meaning of the contents
        info_array.append(O_array[x])
        x=x+1
    O_list = O_record(O_array[5],O_array[6],info_array)
    return O_list

def N_field(array):
    # storing the information for nudges
    N_array=array
    N_list = N_record(array[5],array[6])
    return N_list

def P_field(array):
    # just storing the links 
    P_list = P_record(array[5],array[6])
    return P_list





def student_data():
    array=[]
    try:
        fp=open(filePath,'r') # here is opening up the studentData.csv file, and check the contents
                             # because if we process the information, the data will be deleted and we want user
                            # to input new data into it
        c=0
        for line in fp:
                                       
            c=c+1
        fp.close()
        # Here is the error checking, for testing purpose, disable it
        if c==1:
            fp1=open("Error_report.txt",'w')
            fp1.write("enter your new data !!!, if no data just make it blank")  # telling user to input new data
            
            fp1.close()
            print("\nRead the Error_report.txt file first")
            exit(1)
        fp=open(filePath,'r')

        # here is just initializing array and namedtuple for futuer easy access
        H=H_field("0,0,0,0,0,0,0,0,0,0,0,0,0")
        E=head("0,0,0,0,0,0,0,0")
        P=[] 
        O=[]
        N=[]

    except IOError:
        print("The file does not exist, check your file")
        exit(1)
    i=0 
    # Here is just check if we process all H O N P or not
    H_did= False
    O_did = False
    N_did= False
    P_did = False
    
    for line in fp:
        
        array=line.split(",")
            
        #print(array) 
        if array[5].count("H")==1:
            if H_did==True and O_did==True and N_did==True and P_did==True:
                collect=H_O_N_P(E,H,O,N,P)  # we pass the data over to create H O N P array
                collection_list.append(collect) # here will have entire information about student
                
                # reset all the conditions, otherwise loop will not work
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
            
         # here is checking if we process O N P or not   

        elif array[5].count("O")==1:
            O.append(O_field(array))
            O_did= True

        elif array[5].count("N")==1:
            N.append(N_field(array))
            N_did= True

        elif array[5].count("P")==1 :
            P.append(P_field(array))
            P_did =True
    
    # if we process O N P then we can add it into the list
    # the reason why do it again is because for the last student info, it will not process it so i need force it
    if H_did==True and O_did==True and N_did==True and P_did==True:
                collect=H_O_N_P(E,H,O,N,P)
                collection_list.append(collect)
                # re-set all the variable for next loop
                O=[]
                N=[]
                P=[]

                H_did= False
                O_did = False
                N_did= False
                P_did = False
                    

    fp.close()
    size_check()  # checking if the file we just process has right information or not
    #x=0
    #while x<len(collection_list):
    #    print(collection_list[x])
    #    print("\n\n\n")
    #    x=x+1
    return collection_list

