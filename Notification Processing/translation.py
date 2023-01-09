#!/usr/bin/env python3
import collections
from read_student_data import*


filePath2= "TranslationControlFile.csv"
collection_translating=[] # this hold the interpreting file for N O P
Translation= collections.namedtuple('Translation',['type','test_locator','content','link','link2'])
Html_output = collections.namedtuple('Html_output',['entity','school_id','student_id','teacher_id','H_output','O_output','N_output','P_output'])


collection_html_output=[]


def OUTPUTTING():
    # here is generating a templet for the general describtion for html file
    x=0
   # print(len(collection_list))
    while x <len(collection_list):

        # here is putting the info been process by read_studentdata into the general templet

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
        #print(collection_list[x].O)
        # because the translation file has some extra stuff we want to remove it to make it cleaner
        
        #print(collection_list[x].O[a].text_locator)
        
        while a< len(collection_list[x].O):
            print_list.append(collection_list[x].O[a].text_locator.replace("B",""))
            a=a+1
    
        a=0

        # here is trying to match the sentence and we and put the info into it
        while a< len(print_list):
            b=0
            while b< len(collection_translating):
                #print(collection_translating[b].test_locator)
                if print_list[a]==collection_translating[b].test_locator and collection_translating[b].type=="B":
                    #print("found")
                    print_list[a]=collection_translating[b].content
                    #print(collection_translating[b].content)
                    break
                b=b+1
            a=a+1
        #print(len(print_list)) 
        
        #print(collection_list[x].O[0].info)
        a=0

        
        while a< len(print_list):
            b=0
            # here is just replacing the &1 and &2 in the O (H O N P) sentences
            
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
        # below is just while loop associated with the code_html.py file, it will put the thumbs up and down link into collection
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
        
        # now we have a general information, we are just putting them into the named tuple and into an array
        # now the collection_html_output has all the html information
        out = Html_output(collection_list[x].E.entity_id,collection_list[x].E.school_id,collection_list[x].E.student_id,collection_list[x].E.teacher_id,H_out,O_out,N_out,P_out)
        collection_html_output.append(out)

        x=x+1




def Translate(array):
    T_array = array
    
    # here is for all the nudges, and we need to have a general format 
    if len(T_array)==5 and T_array[0]=="N":
        T_list = Translation(T_array[0],T_array[1],T_array[2],T_array[3],T_array[4])

    elif len(T_array)==4 and T_array[0]!="N":
        T_list = Translation(T_array[0],T_array[1],T_array[2]+T_array[3],0,0)
    else:
        T_list = Translation(T_array[0],T_array[1],T_array[2],0,0)

    return T_list



def translation():
    print("Translating the file content now\n")
    try:
        fp=open(filePath2,'r')

    except IOError:
        print("The file does not exist, check your file")
        exit(1)
    for line in fp:
        array=line.split(",")
        print(array)
        # collecting all the transalting in the format of named tuple for easy access
        collection_translating.append(Translate(array))


    print(collection_translating)
    print("-------------------------------------------------------------------")
    print("\n\n")
    OUTPUTTING()

    return collection_html_output
