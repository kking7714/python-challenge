

import os
import re


file_1 = 'paragraph_1.txt'
file_2 = 'paragraph_2.txt'

def paragraph(file): 
    file = user 

    text_path = os.path.join('files', file)

    open_text = open(text_path, "r")

    words_cnt = 0
    sent_cnt = 0


    for words in open_text:
        words_cnt = words.split()
        sent_cnt = words.split(".")

    words_cnt = len(words_cnt)
    sent_cnt = len(sent_cnt) - 1
    avg_snt_lngth = round(words_cnt / sent_cnt,2)
    avg_ltr_cnt = round(avg_snt_lngth/sent_cnt,2)

    output = "\nParagraph Analysis\n-----------------\nApproximate Word Count: " + str(words_cnt) + "\nApproximate Sentence Count: " + str(sent_cnt) + "\nAverage Letter Count: " + str(avg_ltr_cnt) + "\nAverage Sentence Length: " + str(avg_snt_lngth) + "\n" 

    print(output)

    if file == file_1:
        file = file_1.replace(".txt","")
    else:
        file = file_2.replace(".txt","")
    f = open('PyParagraph_Output' + '_' + file + '.txt','w')
    f.write(output)
    f.close()


user = input("Analyze file_1 (1) or file_2 (2)? ")

if user == "1":
    user = file_1
    paragraph(user)
    
elif user == "2":
    user = file_2
    paragraph(user)    




