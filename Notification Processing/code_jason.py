#!/usr/bin/env python3
import collections

id_counter=0

def update():
    global id_counter
    id_counter=id_counter+1
    # was going to update the id section, but it is quite useless, so this function is not even used

def write(entire_jason_code,txt_file_name):
    # writing entire jason code into a file, then users can just manually copy and paste it over to microsoft actionable message designer, then use power automate to sent emails. 
    fp = open(txt_file_name,'w')
    fp.write(entire_jason_code)
    fp.close()

def code_jason(collection_html_output,p):
    # ---------------------------------------------------------------------------------------------
    # if you want, only replace the image link as I showed in the code, do not try to modify
    # any jason code, because it is really sensitive, 1 { or } will mess up entire code
    # make sure you have a copy of this, then try to modify it, otherwise don't touch any jason code
    #--------------------------------------------------------------------------------------------
    x=p

    #print(collection_html_output[x])
    #print(collection_html_output[x].student_id)
    id_information=collection_html_output[x].entity+"|"+collection_html_output[x].school_id+"|"+collection_html_output[x].student_id+"|"+collection_html_output[x].teacher_id
    print(id_information)
    #This id information will be used in the submit button to help track which it belongs to 

    H_array=collection_html_output[x].H_output.split("\n")
    N_array=collection_html_output[x].N_output.split("\n")
    print("--------------------\n")
   # print(N_array)
    
    # fix url in the head 
    url_head_img="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiXD5NTptfSn-UBeBWZhH3HvvSt2dhVOTagT5LDZ2Nm01HWmtJkG5qbfRBX3qBtxkI6iA-TF6DtmD8xO-JlcpynMQvfojCEJd-HaQJhKyxrTQPUsD-aYp2C4RcrRHGhwxTn7RbEZF-5udPmTaZQqznb8OYQ2BFunxAZXjYQTPx4d56abj8XAF6TFJu3eA/w583-h97/Capture.JPG"
    # just in case the image is broken, we can easily replace it 

    head= "{\"$schema\": \"http://adaptivecards.io/schemas/adaptive-card.json\",\"type\": \"AdaptiveCard\",\"version\": \"1.0\",\"body\": [{\"type\": \"ColumnSet\",\"id\": \"ec67a69b-b519-9795-33fc-7609acb69b52\",\"columns\": [{\"type\": \"Column\",\"id\": \"b903c04a-8ad1-dc48-18c0-6e67f9b0de18\",\"padding\": \"None\",\"width\": \"auto\",\"items\": [{\"type\": \"Image\",\"id\": \"43e6dead-ca8b-6f65-cb10-e23b825f5a3d\",\"url\": \""+url_head_img+"\",\"width\": \"580px\",\"horizontalAlignment\": \"Left\",\"height\": \"84px\"}]},{\"type\": \"Column\",\"id\": \"577e23e8-0c90-5ea9-0df8-9d7889159ea9\",\"padding\": \"None\",\"width\": \"auto\",\"items\": [{\"type\": \"TextBlock\",\"id\": \"studentInfo1\",\"text\": \""
    a=0
    head=head+H_array[a]+"         \\n"
    a=1
    while a< len(H_array):
        if a+1<len(H_array):
            head=head+H_array[a]+"  \\n"
        else:
            head=head+H_array[a]+"\","
        a=a+1
    head=head+"\"wrap\": true,\"size\": \"Small\"}],\"horizontalAlignment\": \"Left\",\"verticalContentAlignment\": \"Center\"}],\"padding\": \"Small\",\"horizontalAlignment\": \"Center\",\"style\": \"default\"}"

    #],\"padding\": \"None\",\"@type\": \"AdaptiveCard\",\"@context\": \"http://schema.org/extensions\"}"
    #---------------------------------------------------------------------------------------------------
    #above is the head, known as H
    
    body1=",{\"type\": \"Container\",\"id\": \"60343c22-b6c7-9337-561f-17cef4c6d977\",\"padding\": \"None\",\"items\": [{\"type\": \"ColumnSet\",\"columns\": [{\"type\": \"Column\",\"id\": \"6dca8e70-d9ea-7b25-c71e-f4f361a228b8\",\"padding\": {\"top\": \"Medium\",\"bottom\": \"Default\",\"left\": \"ExtraLarge\",\"right\": \"ExtraLarge\"},\"width\": \"auto\",\"items\": [{\"type\": \"TextBlock\",\"id\": \"studentInfo2\",\"text\": \""        
    body1=body1+collection_html_output[x].O_output+"\","
    body1=body1+"\"wrap\": true}]}],\"padding\": \"None\"}],\"separator\": true}"

    #],\"padding\": \"None\",\"@type\": \"AdaptiveCard\",\"@context\": \"http://schema.org/extensions\"}"
    #above is the body1, which is O
    
    body2=",{\"type\": \"Container\",\"id\": \"802af8dc-f6d8-57e4-b5d3-b3e3b9853ac6\",\"padding\": \"None\",\"items\": [{\"type\": \"ColumnSet\",\"columns\": [{\"type\": \"Column\",\"id\": \"93d1ac08-0a30-aa05-d17b-69b9e79599ca\",\"padding\": {\"top\": \"Medium\",\"bottom\": \"None\",\"left\": \"None\",\"right\": \"None\"},\"width\": \"stretch\",\"items\": [{\"type\": \"TextBlock\",\"id\": \"fae6382c-5385-6be7-5681-ac5ec4d4c053\",\"text\": \"NUDGES\",\"wrap\": true,\"weight\": \"Bolder\",\"color\": \"Attention\",\"horizontalAlignment\": \"Center\"},{\"type\": \"ColumnSet\",\"columns\": [{\"type\": \"Column\",\"id\": \"99dfb5be-07dc-4250-1e61-aac29a22f3ab\",\"padding\": \"None\",\"width\": \"auto\",\"items\": [{\"type\": \"TextBlock\",\"id\": \"f60c390c-db09-6672-e122-c7d7fdf695f8\",\"text\": \""
    body2=body2+N_array[0]+"\","
    body2=body2+"\"wrap\": true}]}],\"padding\": {\"top\": \"None\",\"bottom\": \"None\",\"left\": \"Medium\",\"right\": \"None\"}},"

    #above is the nudge title stuff, we have not touched the tips yet
    
    # here are just images , you can replace it if you want,otherwise don't touch it
    up_symbol= "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi04RZWEFEtaK-5MxM8SPLmhgyJGPa9RfVACn9mopni0Jr6r0lthd2LYz8akn-Sj4W-2273tS5hGXuVILiKIb405VQZxzp-5Tuv6dgiOj_AFDgm4js_L9y7TOYGIRUuer4hE0npvm_BTEqfqk8ceFuSqQheUMTwCqMv43pM1xBft56Sr6PR1sxtNNrtYQ/s1600/Thumbs%20Up.png"
    down_symbol="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEif9F92FAB2wpM6FpEafrC7cA6PrcjUplezHaTl-xzYUralIsyqZlQgOx4pkg6ka6JEWgPuUXWc_hZ238qvmsrzNteTM0vfNcGyolhZQHi_3r2K_hvBojO2QuAQ8GKx3G5IXELBSlgSGirhX7bZd26H6ZWOaWKtqqvAzOXums7ei3BK3Nur-gxjbU212w/s1600/Thumbs%20Down.png"
    comment_symbol="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgC_jrSXfv8YW7PJ9BBcl95wmLcWfmluYqvCKCAMm_MFCcvzqcP-_GZvtN-x8Zd9-sIFpBJa_HQKHFGuQ59T1ifBP6t9LdgV89RpPogAVe9Gs-IN2Dcrc5RgSxb-v7t_mOF9mxdLsXfMJSDDTs1TwS6OOWiN1WP37hGqpWNxrMmfYo3o3NbnEZ99wI0uw/s1600/Feedback.png"

    # here is the server for getting the feedback from users, 
    server_url="https://prod-32.westus.logic.azure.com:443/workflows/fb723784d65743a6a9b400190c66431b/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=8GauDcZvsxa1UxOaKt3IJ03xmLZfRG8ZO5N9LlSZsXg"
    
    a=1
    Nudge_body=""
    

    while a< len(N_array)-2:
        nudge_up_link=N_array[a+1]
        nudge_down_link=N_array[a+2]

        body3="{\"type\": \"ColumnSet\",\"columns\": [{\"type\": \"Column\",\"id\": \"5f00340f-647e-fa5b-e522-cd997e206f70\",\"padding\": \"None\",\"width\": \"auto\",\"items\": [{\"type\": \"TextBlock\",\"id\": \"149b4a46-5de0-8345-cc97-87aacd88816f\",\"text\": \""+N_array[a]+"\","    
    
        body3= body3+"\"wrap\": true},{\"type\": \"ColumnSet\",\"columns\": [{\"type\": \"Column\",\"id\": \"477f6b2b-29e8-a009-c024-faa3f6040fd5\",\"padding\": \"None\",\"width\": \"auto\",\"items\": [{\"type\": \"Image\",\"id\": \"fab232d6-5241-1282-8ca9-8fca5dbdec25\",\"url\": \""+up_symbol+"\",\"size\": \"Stretch\",\"width\": \"20px\",\"horizontalAlignment\": \"Left\",\"selectAction\": {\"type\": \"Action.Http\",\"method\": \"POST\",\"url\": \"https://prod-32.westus.logic.azure.com:443/workflows/fb723784d65743a6a9b400190c66431b/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=8GauDcZvsxa1UxOaKt3IJ03xmLZfRG8ZO5N9LlSZsXg\"},\"height\": \"20px\"}]},{\"type\": \"Column\",\"id\": \"4bc66a73-694d-bc76-f39e-381bc72a5e6b\",\"padding\": \"None\",\"width\": \"auto\",\"items\": [{\"type\": \"Image\",\"id\": \"1dfc22ff-b043-8599-02b9-1cf8f6136d25\","
    # above is for the first thumbs up
    
        body3 = body3 +"\"url\": \""+down_symbol+"\",\"size\": \"Stretch\",\"width\": \"20px\",\"height\": \"20px\"}]},{\"type\": \"Column\",\"id\": \"0f315ffa-9979-97e0-0a1f-9e9815e0bde2\",\"padding\": \"None\",\"width\": \"auto\",\"items\": [{\"type\": \"Image\",\"id\": \"14147ef9-02cd-e70a-01ff-c0f1683ec393\",\"url\": \""
    # above is the thumbs down symbol
        
        body3= body3 +comment_symbol+"\",\"width\": \"25px\",\"selectAction\": {\"type\": \"Action.ToggleVisibility\",\"targetElements\": [\"commentBox1\"]},\"height\": \"25px\"},{\"type\": \"ColumnSet\",\"columns\": [{\"type\": \"Column\",\"id\": \"816902f4-cf6f-b7cf-cbbc-c7f43a86bfc0\",\"padding\": \"None\",\"width\": \"auto\",\"items\": [{\"type\": \"Input.Text\",\"id\": \"inputComment1\",\"placeholder\": \"Enter text here\",\"isMultiline\": true},{\"type\": \"ActionSet\",\"id\": \"4c128d5a-c314-a31d-8b8d-ed50c67f0a72\",\"actions\": [{\"type\": \"Action.Http\",\"id\": \""+id_information+"\",\"title\": \"Submit\",\"url\": \""

        body3=body3+server_url+"\",\"method\": \"POST\","+r'"body": "{\"'+id_information+r'\": \"{{inputComment1.value}}\"}",'

        body3=body3+"\"headers\": [{\"name\": \"Authorization\"},{\"name\": \"Content-Type\",\"value\": \"application/json\"}]}]}]}],\"padding\": \"None\",\"isVisible\": false,\"id\": \"commentBox1\"}]}],\"padding\": {\"top\": \"None\",\"bottom\": \"None\",\"left\": \"ExtraLarge\",\"right\": \"None\"}}]}],\"padding\": {\"top\": \"None\",\"bottom\": \"None\",\"left\": \"Medium\",\"right\": \"None\"}}"
        a=a+3
        
        if a< len(N_array)-2:
            Nudge_body=Nudge_body+body3+","
        else:
            Nudge_body=Nudge_body+body3

    ending="]}],\"padding\": \"None\"}],\"separator\": true}],\"padding\": \"None\",\"@type\": \"AdaptiveCard\",\"@context\": \"http://schema.org/extensions\"}"

        
    #print(N_array)
    #print(body3)
    
    # here we are doing the tips

    tips_head="]},{\"type\": \"Column\",\"id\": \"b16e640c-6bdb-7387-036d-066074a6534f\",\"padding\": {\"top\": \"Medium\",\"bottom\": \"Default\",\"left\": \"Default\",\"right\": \"Default\"},\"width\": \"stretch\",\"items\": [{\"type\": \"TextBlock\",\"id\": \"7f6751b8-33b8-aa26-6663-b3e6f3296c2c\",\"text\": \"PROFESSIONAL DEVELOPMENT\",\"wrap\": true,\"weight\": \"Bolder\",\"color\": \"Attention\",\"horizontalAlignment\": \"Center\"},"
    
    a=0
    professional_development=""
    # you can change the image link below
    video_image_link = "https://cdn3.iconfinder.com/data/icons/unicons-vector-icons-pack/32/youtube-512.png"
    video_name= "How to help students just testing:"
     

    while a<len(collection_html_output[x].P_output):
        tips_body="{\"type\": \"ColumnSet\",\"columns\": [{\"type\": \"Column\",\"id\": \"173469f4-1db5-3a78-36cb-3f5b4a2aa7ae\",\"padding\": \"None\",\"width\": \"auto\",\"items\": [{\"type\": \"TextBlock\",\"id\": \"127a91b9-d847-0dad-6e84-2aa95d54faf6\",\"text\": \"Video: "+video_name+"\",\"wrap\": true}]},{\"type\": \"Column\",\"id\": \"d07d6fc0-81e1-6a55-30bc-4c9b057e0cef\",\"padding\": {\"top\": \"None\",\"bottom\": \"None\",\"left\": \"None\",\"right\": \"ExtraLarge\"},\"width\": \"auto\",\"items\": [{\"type\": \"Image\",\"id\": \"8b323ef4-24c7-aca6-8bdb-4effbccd5188\",\"url\": \""
     
        tips_body=tips_body+video_image_link+"\",\"size\": \"Medium\",\"width\": \"60px\",\"selectAction\": {\"type\": \"Action.OpenUrl\",\"url\": \""+collection_html_output[x].P_output[a].replace("\n","")+"\""
        
        tips_body=tips_body+"},\"height\": \"60px\"}]}],\"padding\": \"None\"}" 
        
        a=a+1
        if a<len(collection_html_output[x].P_output):
            professional_development=professional_development+tips_body+","
        else:
            professional_development=professional_development+tips_body


   # print(collection_html_output[x].P_output)
    head=head+body1+body2+Nudge_body+tips_head+professional_development+ending

    #print(head)
    name= collection_html_output[x].entity+"_"+collection_html_output[x].school_id+"_"+collection_html_output[x].student_id+"_"+collection_html_output[x].teacher_id+".txt"
    write(head,name)

