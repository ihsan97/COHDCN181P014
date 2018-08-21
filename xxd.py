from sys import argv

text_list=[]

script, file=argv
fo=open(file,"r")                               #Open the given file in command line
textin=fo.read()
fo.close()


def func(text):                                 #Convert ASCII strings to hex values
        string=""
        for i in str(text):
                h=str(hex(ord(i)))[2:]
                string+=h
                
        count=0
        string2=""
        for j in str(string):   
                count+=1
                string2+=j
                if count%4==0:
                        string2+=" "
        return string2

def replace_line(word):
        new_word=""
        for i in str(word):
                if i=="\n" or i==" ":           #Replace Enter and Space with dot
                        new_word+="."
                else:
                        new_word+=i
        
        return new_word

def line(val):                                  #Setting Couter values
        return "0"*(7-len(str(hex(val))[2:]))+str(hex(val))[2:]+"0"

        
text=""
count=0
for i in str(textin):                           #Break lines after 16 characters
        text+=i
        count+=1
        if count == 16:       
                text_list.append(text)
                count=0
                text=""
                
else:
        text_list.append(text)
        text=""


for i in range(len(text_list)):                 #print those defined functions to get the output
        print(line(i),func(text_list[i]),str(replace_line(text_list[i])))
