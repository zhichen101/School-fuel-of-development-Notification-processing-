#!/usr/bin/env python3
import collections

#Global_email = collections.namedtuple('Global_email',['entity','school_id','student_id','teacher_id','message'])

#global_html=[]

def code_html(collection_html_output):
    

    # here is just throwing everything we did from translation.py into this html format 


    # print(collection_html_output)
    x =0
    #print(collection_html_output[x])
    while x<len(collection_html_output):
        
        #print(collection_html_output[x].H_output)
        H_array=collection_html_output[x].H_output.split("\n")
        #this step is going to split all the H section

        #print(collection_html_output[x].N_output)
        N_array=collection_html_output[x].N_output.split("\n")
        # this step is going to split all the nudge section 


        #print(collection_html_output[x].N_output)
        #print(len(N_array))
        #print(N_array)

        #in case the img is broken, just replace this one
        image_address="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiXD5NTptfSn-UBeBWZhH3HvvSt2dhVOTagT5LDZ2Nm01HWmtJkG5qbfRBX3qBtxkI6iA-TF6DtmD8xO-JlcpynMQvfojCEJd-HaQJhKyxrTQPUsD-aYp2C4RcrRHGhwxTn7RbEZF-5udPmTaZQqznb8OYQ2BFunxAZXjYQTPx4d56abj8XAF6TFJu3eA/w583-h97/Capture.JPG"
        
        #write a file that associate with all types of id
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
       
        # here is getting the O section, on the upper right corner
        detailed_resut="<div class=\"row\"><div class=\"col\"></div><div class=\"col-7\"><p style=\"text-align: left;\"><br>"+collection_html_output[x].O_output+"<br><br></p></div><div class=\"col\"></div></div><br><div class=\"row\"><div class=\"col\"></div><hr style=\"width:65%;height: 3px;color: gray;\"><div class=\"col\"></div></div><br>"

       
        nudges = "<div class=\"row\"><div class=\"col\"></div><div class=\"col-4\"><div style=\"text-align: center;\"><strong style=\"text-align: center;color: red;\">NUDGES</strong></div><br><p>"
        nudges=nudges+N_array[0]+"</p><ol>"
        

        
        nudge_link_comment="https://i0.wp.com/insidetimeshare.com/wp-content/uploads/2016/08/no-availability.jpg?fit=283%2C178&ssl=1"



        nudge_style="width=30x\"" 

        # There are just 3 different image, in case they are broken, just replace them
        nudge_up_symbol="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi04RZWEFEtaK-5MxM8SPLmhgyJGPa9RfVACn9mopni0Jr6r0lthd2LYz8akn-Sj4W-2273tS5hGXuVILiKIb405VQZxzp-5Tuv6dgiOj_AFDgm4js_L9y7TOYGIRUuer4hE0npvm_BTEqfqk8ceFuSqQheUMTwCqMv43pM1xBft56Sr6PR1sxtNNrtYQ/s1600/Thumbs%20Up.png"
        nudge_down_symbol="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEif9F92FAB2wpM6FpEafrC7cA6PrcjUplezHaTl-xzYUralIsyqZlQgOx4pkg6ka6JEWgPuUXWc_hZ238qvmsrzNteTM0vfNcGyolhZQHi_3r2K_hvBojO2QuAQ8GKx3G5IXELBSlgSGirhX7bZd26H6ZWOaWKtqqvAzOXums7ei3BK3Nur-gxjbU212w/s1600/Thumbs%20Down.png"
        nudge_comment_symbol="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgC_jrSXfv8YW7PJ9BBcl95wmLcWfmluYqvCKCAMm_MFCcvzqcP-_GZvtN-x8Zd9-sIFpBJa_HQKHFGuQ59T1ifBP6t9LdgV89RpPogAVe9Gs-IN2Dcrc5RgSxb-v7t_mOF9mxdLsXfMJSDDTs1TwS6OOWiN1WP37hGqpWNxrMmfYo3o3NbnEZ99wI0uw/s1600/Feedback.png"



        a=1
        #print(N_array)
        #print("separate")

        # below is creating a loop and keep getting all the useful tips, don't try to modify them unless you have to 
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
        
        # here is a loop for getting all the vidoes and image associate with it
        while a<len(collection_html_output[x].P_output):
            professional_development=professional_development+column+"<div class=\"row\"><p><a style=\"color: black;\" href=\""+collection_html_output[x].P_output[a]+"\"target=_blank>Video</a>:"+video_info_to_be_putted+"</p></div>"
            
            professional_development=professional_development+"<div class=\"col-3\"><iframe  style=\"width:"+width+";height: "+height+";\" class=\"embed-responsiveitem\"src=\""+collection_html_output[x].P_output[a]+"\"title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen></iframe> </div> "
            a=a+1
        
        #print(professional_development)
        
        end = "</div><div class=\"col\"></div></div><br><div class=\"row\"><div class=\"col\"></div><hr style=\"width:65%;height: 3px;color: gray;\"><div class=\"col\"></div></div></div>"
        message = head +body+student_info+detailed_resut+nudges+professional_development+end
        
        #email=Global_email(collection_html_output[x].entity,collection_html_output[x].school_id,collection_html_output[x].student_id,collection_html_output[x].teacher_id,message)
        #global_html.append(email)
        
        
        fp.write(message)
                 
        #    os.remove(collection_html_output[x].school_id+".html")
        # if sent, then it will be removed
        fp.close()
        x=x+1


