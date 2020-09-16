##import numpy as np
##import pandas as pd 
##import re
##import matplotlib.pyplot as plt
##
##data = pd.read_csv("C:\\Users\\talil\\OneDrive\\Documents\\GitHub\\Ts-and-Ls\\ver1.csv")
##print(data.head(10))

cohort_col = {('1', 1): ['Game_C1_Q1_1_1', 'Game_C1_Q1_1_2', 'Game_C1_Q1_1_3', 'Game_C1_Q1_1_4', 'Game_C1_Q1_1_5', 'Game_C1_Q1_1_6', 'Game_C1_Q1_1_7', 'Game_C1_Q1_1_8'],
              ('1', 2): ['Game_C1_Q2_1_1', 'Game_C1_Q2_1_2', 'Game_C1_Q2_1_3', 'Game_C1_Q2_1_4', 'Game_C1_Q2_1_5', 'Game_C1_Q2_1_6', 'Game_C1_Q2_1_7', 'Game_C1_Q2_1_8'],
              ('1', 3): ['Game_C1_Q3_1_1', 'Game_C1_Q3_1_2', 'Game_C1_Q3_1_3', 'Game_C1_Q3_1_4', 'Game_C1_Q3_1_5', 'Game_C1_Q3_1_6', 'Game_C1_Q3_1_7', 'Game_C1_Q3_1_8'],
              ('1', 4): ['Game_C1_Q4_1_1', 'Game_C1_Q4_1_2', 'Game_C1_Q4_1_3', 'Game_C1_Q4_1_4', 'Game_C1_Q4_1_5', 'Game_C1_Q4_1_6', 'Game_C1_Q4_1_7', 'Game_C1_Q4_1_8'],
              ('1', 5): ['Game_C1_Q5_1_1', 'Game_C1_Q5_1_2', 'Game_C1_Q5_1_3', 'Game_C1_Q5_1_4', 'Game_C1_Q5_1_5', 'Game_C1_Q5_1_6', 'Game_C1_Q5_1_7', 'Game_C1_Q5_1_8'],
              ('1', 6): ['Game_C1_Q6_1_1', 'Game_C1_Q6_1_2', 'Game_C1_Q6_1_3', 'Game_C1_Q6_1_4', 'Game_C1_Q6_1_5', 'Game_C1_Q6_1_6', 'Game_C1_Q6_1_7', 'Game_C1_Q6_1_8'],
              ('1', 7): ['Game_C1_Q7_1_1', 'Game_C1_Q7_1_2', 'Game_C1_Q7_1_3', 'Game_C1_Q7_1_4', 'Game_C1_Q7_1_5', 'Game_C1_Q7_1_6', 'Game_C1_Q7_1_7', 'Game_C1_Q7_1_8'],
              ('1', 8): ['Game_C1_Q8_1_1', 'Game_C1_Q8_1_2', 'Game_C1_Q8_1_3', 'Game_C1_Q8_1_4', 'Game_C1_Q8_1_5', 'Game_C1_Q8_1_6', 'Game_C1_Q8_1_7', 'Game_C1_Q8_1_8'],
              ('1', 9): ['Game_C1_Q9_1_1', 'Game_C1_Q9_1_2', 'Game_C1_Q9_1_3', 'Game_C1_Q9_1_4', 'Game_C1_Q9_1_5', 'Game_C1_Q9_1_6', 'Game_C1_Q9_1_7', 'Game_C1_Q9_1_8'],
              ('1', 10): ['Cohort1_Q10_1_1', 'Cohort1_Q10_1_2', 'Cohort1_Q10_1_3', 'Cohort1_Q10_1_4', 'Cohort1_Q10_1_5', 'Cohort1_Q10_1_6', 'Cohort1_Q10_1_7', 'Cohort1_Q10_1_8'],
              ('2', 1): ['Game_C24_Q1_1_1', 'Game_C24_Q1_1_2', 'Game_C24_Q1_1_3', 'Game_C24_Q1_1_4', 'Game_C24_Q1_1_5', 'Game_C24_Q1_1_6', 'Game_C24_Q1_1_7', 'Game_C24_Q1_1_8'],
              ('2', 2): ['Game_C24_Q2_1_1', 'Game_C24_Q2_1_2', 'Game_C24_Q2_1_3', 'Game_C24_Q2_1_4', 'Game_C24_Q2_1_5', 'Game_C24_Q2_1_6', 'Game_C24_Q2_1_7', 'Game_C24_Q2_1_8'],
              ('2', 3): ['Game_C24_Q3_1_1', 'Game_C24_Q3_1_2', 'Game_C24_Q3_1_3', 'Game_C24_Q3_1_4', 'Game_C24_Q3_1_5', 'Game_C24_Q3_1_6', 'Game_C24_Q3_1_7', 'Game_C24_Q3_1_8'],
              ('2', 4): ['Game_C24_Q4_1_1', 'Game_C24_Q4_1_2', 'Game_C24_Q4_1_3', 'Game_C24_Q4_1_4', 'Game_C24_Q4_1_5', 'Game_C24_Q4_1_6', 'Game_C24_Q4_1_7', 'Game_C24_Q4_1_8'],
              ('2', 5): ['Game_C24_Q5_Time_1_1', 'Game_C24_Q5_Time_1_2', 'Game_C24_Q5_Time_1_3', 'Game_C24_Q5_Time_1_4', 'Game_C24_Q5_Time_1_5', 'Game_C24_Q5_Time_1_6', 'Game_C24_Q5_Time_1_7', 'Game_C24_Q5_Time_1_8'],
              ('2', 6): ['Game_C24_Q6_1_1', 'Game_C24_Q6_1_2', 'Game_C24_Q6_1_3', 'Game_C24_Q6_1_4', 'Game_C24_Q6_1_5', 'Game_C24_Q6_1_6', 'Game_C24_Q6_1_7', 'Game_C24_Q6_1_8'],
              ('2', 7): ['Game_C24_Q7_1_1', 'Game_C24_Q7_1_2', 'Game_C24_Q7_1_3', 'Game_C24_Q7_1_4', 'Game_C24_Q7_1_5', 'Game_C24_Q7_1_6', 'Game_C24_Q7_1_7', 'Game_C24_Q7_1_8'],
              ('2', 8): ['Game_C24_Q8_1_1', 'Game_C24_Q8_1_2', 'Game_C24_Q8_1_3', 'Game_C24_Q8_1_4', 'Game_C24_Q8_1_5', 'Game_C24_Q8_1_6', 'Game_C24_Q8_1_7', 'Game_C24_Q8_1_8'],
              ('2', 9): ['Game_C24_Q9_1_1', 'Game_C24_Q9_1_2', 'Game_C24_Q9_1_3', 'Game_C24_Q9_1_4', 'Game_C24_Q9_1_5', 'Game_C24_Q9_1_6', 'Game_C24_Q9_1_7', 'Game_C24_Q9_1_8'],
              ('2', 10): ['Cohort24_Q10_1_1', 'Cohort24_Q10_1_2', 'Cohort24_Q10_1_3', 'Cohort24_Q10_1_4', 'Cohort24_Q10_1_5', 'Cohort24_Q10_1_6', 'Cohort24_Q10_1_7', 'Cohort24_Q10_1_8'],
              ('3', 1): ['Game_C35_Q1_1_1', 'Game_C35_Q1_1_2', 'Game_C35_Q1_1_3', 'Game_C35_Q1_1_4', 'Game_C35_Q1_1_5', 'Game_C35_Q1_1_6', 'Game_C35_Q1_1_7', 'Game_C35_Q1_1_8'],
              ('3', 2): ['Game_C35_Q2_1_1', 'Game_C35_Q2_1_2', 'Game_C35_Q2_1_3', 'Game_C35_Q2_1_4', 'Game_C35_Q2_1_5', 'Game_C35_Q2_1_6', 'Game_C35_Q2_1_7', 'Game_C35_Q2_1_8'],
              ('3', 3): ['Game_C35_Q3_1_1', 'Game_C35_Q3_1_2', 'Game_C35_Q3_1_3', 'Game_C35_Q3_1_4', 'Game_C35_Q3_1_5', 'Game_C35_Q3_1_6', 'Game_C35_Q3_1_7', 'Game_C35_Q3_1_8'],
              ('3', 4): ['Game_C35_Q4_1_1', 'Game_C35_Q4_1_2', 'Game_C35_Q4_1_3', 'Game_C35_Q4_1_4', 'Game_C35_Q4_1_5', 'Game_C35_Q4_1_6', 'Game_C35_Q4_1_7', 'Game_C35_Q4_1_8'],
              ('3', 5): ['Game_C35_Q5_1_1', 'Game_C35_Q5_1_2', 'Game_C35_Q5_1_3', 'Game_C35_Q5_1_4', 'Game_C35_Q5_1_5', 'Game_C35_Q5_1_6', 'Game_C35_Q5_1_7', 'Game_C35_Q5_1_8'],
              ('3', 6): ['Game_C35_Q6_1_1', 'Game_C35_Q6_1_2', 'Game_C35_Q6_1_3', 'Game_C35_Q6_1_4', 'Game_C35_Q6_1_5', 'Game_C35_Q6_1_6', 'Game_C35_Q6_1_7', 'Game_C35_Q6_1_8'],
              ('3', 7): ['Game_C35_Q7_1_1', 'Game_C35_Q7_1_2', 'Game_C35_Q7_1_3', 'Game_C35_Q7_1_4', 'Game_C35_Q7_1_5', 'Game_C35_Q7_1_6', 'Game_C35_Q7_1_7', 'Game_C35_Q7_1_8'],
              ('3', 8): ['Game_C35_Q8_1_1', 'Game_C35_Q8_1_2', 'Game_C35_Q8_1_3', 'Game_C35_Q8_1_4', 'Game_C35_Q8_1_5', 'Game_C35_Q8_1_6', 'Game_C35_Q8_1_7', 'Game_C35_Q8_1_8'],
              ('3', 9): ['Game_C35_Q9_1_1', 'Game_C35_Q9_1_2', 'Game_C35_Q9_1_3', 'Game_C35_Q9_1_4', 'Game_C35_Q9_1_5', 'Game_C35_Q9_1_6', 'Game_C35_Q9_1_7', 'Game_C35_Q9_1_8'],
              ('3', 10): ['Cohort35_Q10_1_1', 'Cohort35_Q10_1_2', 'Cohort35_Q10_1_3', 'Cohort35_Q10_1_4', 'Cohort35_Q10_1_5', 'Cohort35_Q10_1_6', 'Cohort35_Q10_1_7', 'Cohort35_Q10_1_8'],
              ('4', 1): ['Game_C24_Q1_1_1', 'Game_C24_Q1_1_2', 'Game_C24_Q1_1_3', 'Game_C24_Q1_1_4', 'Game_C24_Q1_1_5', 'Game_C24_Q1_1_6', 'Game_C24_Q1_1_7', 'Game_C24_Q1_1_8'],
              ('4', 2): ['Game_C24_Q2_1_1', 'Game_C24_Q2_1_2', 'Game_C24_Q2_1_3', 'Game_C24_Q2_1_4', 'Game_C24_Q2_1_5', 'Game_C24_Q2_1_6', 'Game_C24_Q2_1_7', 'Game_C24_Q2_1_8'],
              ('4', 3): ['Game_C24_Q3_1_1', 'Game_C24_Q3_1_2', 'Game_C24_Q3_1_3', 'Game_C24_Q3_1_4', 'Game_C24_Q3_1_5', 'Game_C24_Q3_1_6', 'Game_C24_Q3_1_7', 'Game_C24_Q3_1_8'],
              ('4', 4): ['Game_C24_Q4_1_1', 'Game_C24_Q4_1_2', 'Game_C24_Q4_1_3', 'Game_C24_Q4_1_4', 'Game_C24_Q4_1_5', 'Game_C24_Q4_1_6', 'Game_C24_Q4_1_7', 'Game_C24_Q4_1_8'],
              ('4', 5): ['Game_C24_Q5_Time_1_1', 'Game_C24_Q5_Time_1_2', 'Game_C24_Q5_Time_1_3', 'Game_C24_Q5_Time_1_4', 'Game_C24_Q5_Time_1_5', 'Game_C24_Q5_Time_1_6', 'Game_C24_Q5_Time_1_7', 'Game_C24_Q5_Time_1_8'],
              ('4', 6): ['Game_C24_Q6_1_1', 'Game_C24_Q6_1_2', 'Game_C24_Q6_1_3', 'Game_C24_Q6_1_4', 'Game_C24_Q6_1_5', 'Game_C24_Q6_1_6', 'Game_C24_Q6_1_7', 'Game_C24_Q6_1_8'],
              ('4', 7): ['Game_C24_Q7_1_1', 'Game_C24_Q7_1_2', 'Game_C24_Q7_1_3', 'Game_C24_Q7_1_4', 'Game_C24_Q7_1_5', 'Game_C24_Q7_1_6', 'Game_C24_Q7_1_7', 'Game_C24_Q7_1_8'],
              ('4', 8): ['Game_C24_Q8_1_1', 'Game_C24_Q8_1_2', 'Game_C24_Q8_1_3', 'Game_C24_Q8_1_4', 'Game_C24_Q8_1_5', 'Game_C24_Q8_1_6', 'Game_C24_Q8_1_7', 'Game_C24_Q8_1_8'],
              ('4', 9): ['Game_C24_Q9_1_1', 'Game_C24_Q9_1_2', 'Game_C24_Q9_1_3', 'Game_C24_Q9_1_4', 'Game_C24_Q9_1_5', 'Game_C24_Q9_1_6', 'Game_C24_Q9_1_7', 'Game_C24_Q9_1_8'],
              ('4', 10): ['Cohort24_Q10_1_1', 'Cohort24_Q10_1_2', 'Cohort24_Q10_1_3', 'Cohort24_Q10_1_4', 'Cohort24_Q10_1_5', 'Cohort24_Q10_1_6', 'Cohort24_Q10_1_7', 'Cohort24_Q10_1_8'],
              ('5', 1): ['Game_C35_Q1_1_1', 'Game_C35_Q1_1_2', 'Game_C35_Q1_1_3', 'Game_C35_Q1_1_4', 'Game_C35_Q1_1_5', 'Game_C35_Q1_1_6', 'Game_C35_Q1_1_7', 'Game_C35_Q1_1_8'],
              ('5', 2): ['Game_C35_Q2_1_1', 'Game_C35_Q2_1_2', 'Game_C35_Q2_1_3', 'Game_C35_Q2_1_4', 'Game_C35_Q2_1_5', 'Game_C35_Q2_1_6', 'Game_C35_Q2_1_7', 'Game_C35_Q2_1_8'],
              ('5', 3): ['Game_C35_Q3_1_1', 'Game_C35_Q3_1_2', 'Game_C35_Q3_1_3', 'Game_C35_Q3_1_4', 'Game_C35_Q3_1_5', 'Game_C35_Q3_1_6', 'Game_C35_Q3_1_7', 'Game_C35_Q3_1_8'],
              ('5', 4): ['Game_C35_Q4_1_1', 'Game_C35_Q4_1_2', 'Game_C35_Q4_1_3', 'Game_C35_Q4_1_4', 'Game_C35_Q4_1_5', 'Game_C35_Q4_1_6', 'Game_C35_Q4_1_7', 'Game_C35_Q4_1_8'],
              ('5', 5): ['Game_C35_Q5_1_1', 'Game_C35_Q5_1_2', 'Game_C35_Q5_1_3', 'Game_C35_Q5_1_4', 'Game_C35_Q5_1_5', 'Game_C35_Q5_1_6', 'Game_C35_Q5_1_7', 'Game_C35_Q5_1_8'],
              ('5', 6): ['Game_C35_Q6_1_1', 'Game_C35_Q6_1_2', 'Game_C35_Q6_1_3', 'Game_C35_Q6_1_4', 'Game_C35_Q6_1_5', 'Game_C35_Q6_1_6', 'Game_C35_Q6_1_7', 'Game_C35_Q6_1_8'],
              ('5', 7): ['Game_C35_Q7_1_1', 'Game_C35_Q7_1_2', 'Game_C35_Q7_1_3', 'Game_C35_Q7_1_4', 'Game_C35_Q7_1_5', 'Game_C35_Q7_1_6', 'Game_C35_Q7_1_7', 'Game_C35_Q7_1_8'],
              ('5', 8): ['Game_C35_Q8_1_1', 'Game_C35_Q8_1_2', 'Game_C35_Q8_1_3', 'Game_C35_Q8_1_4', 'Game_C35_Q8_1_5', 'Game_C35_Q8_1_6', 'Game_C35_Q8_1_7', 'Game_C35_Q8_1_8'],
              ('5', 9): ['Game_C35_Q9_1_1', 'Game_C35_Q9_1_2', 'Game_C35_Q9_1_3', 'Game_C35_Q9_1_4', 'Game_C35_Q9_1_5', 'Game_C35_Q9_1_6', 'Game_C35_Q9_1_7', 'Game_C35_Q9_1_8'],
              ('5', 10): ['Cohort35_Q10_1_1', 'Cohort35_Q10_1_2', 'Cohort35_Q10_1_3', 'Cohort35_Q10_1_4', 'Cohort35_Q10_1_5', 'Cohort35_Q10_1_6', 'Cohort35_Q10_1_7', 'Cohort35_Q10_1_8']}
      
sol = {1: [0, 0, 0, 2, 2, 3, 0, 2],
       2: [1, 4, 1, 0, 0, 0, 1, 2],
       3: [2, 2, 3, 0, 0, 0, 2, 0],
       4: [0, 0, 0, 1, 0, 4, 1, 3],
       5: [2, 1, 1, 1, 1, 1, 1, 1],
       6: [0, 2, 1, 1, 0, 3, 1, 1],
       7: [0, 1, 1, 1, 2, 1, 2, 1],
       8: [3, 2, 3, 1, 0, 0, 0, 0],
       9: [1, 1, 1, 2, 1, 1, 1, 1],
       10: [0, 1, 0, 2, 2, 3, 0, 1]}

##data = data.query("Finished == 'TRUE' & Status != 'Survey Preview'")

def correct_rate(data):
    for i in range(len(data)):
        row = data.iloc[i, : ]
        case = row['mTurk'][0]
        print(row['mTurk'], " (",case,")")
        for qnum in range(1, 11):
            answer = [int(row[cohort_col[(case, qnum)][i]]) for i in range(8)]
            print(qnum, ": ", answer, sol[qnum] == answer)


##        for i in range(8):
##            print("qnum: ", qnum, ", i:", i, " ==>", row[cohort_col[(case, qnum)][i]])
##    for x in range(

##correct_rate(data)
