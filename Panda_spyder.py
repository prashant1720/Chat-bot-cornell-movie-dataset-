import numpy as np
import tensorflow as tf
import re
import time
lines = open(r'C:\Users\Prashant\Desktop\Panda\datasets\cornell_movie_dialog\movie_lines.txt',encoding='utf-8', errors='ignore').read().split('\n')
conversations = open(r'C:\Users\Prashant\Desktop\Panda\datasets\cornell_movie_dialog\movie_conversations.txt',encoding='utf-8', errors='ignore').read().split('\n')

id2line = {}
for line in lines:
    _line = line.split(' +++$+++ ')
    if len(_line)==5:
        id2line[_line[0]] = _line[4]
        
        
conversations_ids = []
for conversation in conversations[:-1]:
    _conversation = conversation.split(' +++$+++ ')[-1][1:-1].replace("'","").replace(" ","")  
    conversations_ids.append(_conversation.split(','))
    
#Getting seperately the questions and the answers
questions = []
answers   = []
for conversation in conversations_ids:
    for i in range(len(conversation)-1):
        questions.append(id2line[conversation[i]])
        answers.append(id2line[conversation[i+1]])
        
        
#making a function to perform cleaning
    
def clean_text(text):
    text = text.lower() #converting text to lowercase
    text = re.sub(r"i'm", "i am",text)
    text = re.sub(r"he's","he is",text)
    text = re.sub(r"she's", "she is",text)
    text = re.sub(r"that's","that is",text)
    text = re.sub(r"I'm","I am",text)
    text = re.sub(r"[-()\-#/@;:<>{}+=|.?,]","",text)
    return text


#cleaning the questions

clean_questions = []
for question in questions:
    clean_questions.append(clean_text(question))
    
# cleaning the answers

clean_answers = []
for answer in answers:
    clean_answers.append(clean_text(answer))
    