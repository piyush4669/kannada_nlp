# -*- coding: utf-8 -*-
import pandas as pd
label=pd.read_table('data_label.txt',delim_whitespace=False,names=['label'])
dataset = []
with open('data.txt', 'r', encoding='utf-8') as df:
    line = df.readlines()
    # temp = l.split("\\s")
    for l in line:
        temp = l.split(" ") 
        dataset.append(temp)

emo_dataset = pd.read_excel("dataset.xlsx")

total_score = []
for row in dataset:
    row_score = []
    for i in row:
        n_input = str(i)
        temp = emo_dataset[(emo_dataset == n_input).any(1)].stack()[lambda x: x != n_input].unique()
        if(len(temp) == 0):
            row_score.append(0)
        else:
            row_score.append(temp[0])
    total = sum(row_score)        
    if(total > 0):
        total_score.append(1)
    elif(total == 0):
        total_score.append(0)
    else:
        total_score.append(-1)    

accuracy = 0
for i,j in zip(total_score,label.values.tolist()):
    print(i,int(j[0]))
    if(i == int(j[0])):
        accuracy = accuracy + 1

print((accuracy/len(label))*100)
