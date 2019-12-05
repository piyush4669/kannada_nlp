# -*- coding: utf-8 -*-
import pandas as pd
dataset = []
with open('data.txt', 'r', encoding='utf-8') as df:
    line = df.readlines()
    # temp = l.split("\\s")
    for l in line:
        temp = l.split(" ") 
        dataset.append(temp)

emo_dataset = pd.read_excel("dataset.xlsx")
# pos_emo_dataset = emo_dataset[emo_dataset["Tag"] == 1]
# neg_emo_dataset = emo_dataset[emo_dataset["Tag"] == -1]

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
    total_score.append(sum(row_score))

print(total_score)    