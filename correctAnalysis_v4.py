import numpy as np
import pandas as pd 
import re
import matplotlib.pyplot as plt

data = pd.read_csv("C:\\Users\\talil\\OneDrive\\Documents\\GitHub\\Ts-and-Ls\\raw_cohort5.csv")

headers = ["ProlificID", "cohort", "consent", "gender", "age", "training1_success", "training1_time", "training1_dist_C", "training1_dist_E", "training1_dist_F", "training1_dist_L", "training1_dist_M", "training1_dist_N", "training1_dist_O", "training1_dist_T", "training1_sum_distance",
           "training2_success", "training2_time", "training2_dist_C", "training2_dist_E", "training2_dist_F", "training2_dist_L", "training2_dist_M", "training2_dist_N", "training2_dist_O", "training2_dist_T", "training2_sum_distance",
           "training3_success", "training3_time", "training3_dist_C", "training3_dist_E", "training3_dist_F", "training3_dist_L", "training3_dist_M", "training3_dist_N", "training3_dist_O", "training3_dist_T", "training3_sum_distance",
           "training4_success", "training4_time", "training4_dist_C", "training4_dist_E", "training4_dist_F", "training4_dist_L", "training4_dist_M", "training4_dist_N", "training4_dist_O", "training4_dist_T", "training4_sum_distance", "training_sum_success",
           "game1_success", "game1_time", "game1_sum_identified", "game1_success_rate", "game1_dist_C", "game1_dist_E", "game1_dist_F", "game1_dist_L", "game1_dist_M", "game1_dist_N", "game1_dist_O", "game1_dist_T", "game1_sum_distance", "game1_ca_agreed",
           "game2_success", "game2_time", "game2_sum_identified", "game2_success_rate", "game2_dist_C", "game2_dist_E", "game2_dist_F", "game2_dist_L", "game2_dist_M", "game2_dist_N", "game2_dist_O", "game2_dist_T", "game2_sum_distance", "game2_ca_agreed",
           "game3_success", "game3_time", "game3_sum_identified", "game3_success_rate", "game3_dist_C", "game3_dist_E", "game3_dist_F", "game3_dist_L", "game3_dist_M", "game3_dist_N", "game3_dist_O", "game3_dist_T", "game3_sum_distance", "game3_ca_agreed",
           "game4_success", "game4_time", "game4_sum_identified", "game4_success_rate", "game4_dist_C", "game4_dist_E", "game4_dist_F", "game4_dist_L", "game4_dist_M", "game4_dist_N", "game4_dist_O", "game4_dist_T", "game4_sum_distance", "game4_ca_agreed",
           "game5_success", "game5_time", "game5_sum_identified", "game5_success_rate", "game5_dist_C", "game5_dist_E", "game5_dist_F", "game5_dist_L", "game5_dist_M", "game5_dist_N", "game5_dist_O", "game5_dist_T", "game5_sum_distance", "game5_ca_agreed",
           "game6_success", "game6_time", "game6_sum_identified", "game6_success_rate", "game6_dist_C", "game6_dist_E", "game6_dist_F", "game6_dist_L", "game6_dist_M", "game6_dist_N", "game6_dist_O", "game6_dist_T", "game6_sum_distance", "game6_ca_agreed",
           "game7_success", "game7_time", "game7_sum_identified", "game7_success_rate", "game7_dist_C", "game7_dist_E", "game7_dist_F", "game7_dist_L", "game7_dist_M", "game7_dist_N", "game7_dist_O", "game7_dist_T", "game7_sum_distance", "game7_ca_agreed",
           "game8_success", "game8_time", "game8_sum_identified", "game8_success_rate", "game8_dist_C", "game8_dist_E", "game8_dist_F", "game8_dist_L", "game8_dist_M", "game8_dist_N", "game8_dist_O", "game8_dist_T", "game8_sum_distance", "game8_ca_agreed",
           "game9_success", "game9_time", "game9_sum_identified", "game9_success_rate", "game9_dist_C", "game9_dist_E", "game9_dist_F", "game9_dist_L", "game9_dist_M", "game9_dist_N", "game9_dist_O", "game9_dist_T", "game9_sum_distance", "game9_ca_agreed",
           "game10_success", "game10_time", "game10_sum_identified", "game10_success_rate", "game10_dist_C", "game10_dist_E", "game10_dist_F", "game10_dist_L", "game10_dist_M", "game10_dist_N", "game10_dist_O", "game10_dist_T", "game10_sum_distance", "game10_ca_agreed",
           "game_sum_success_total", "total_time", "average_game_time", "game_sum_ca_agreed_total", "game_sum_agreed_ca_right", "game_sum_agreed_ca_wrong", "game_sum_disagreed_ca_right", "game_sum_disagreed_ca_wrong_success", "game_sum_disagreed_ca_wrong_failure", "avg_task_load", "avg_trust", "avg_explanation"]


cohort_game_col = {('1', 1): ['Game_C1_Q1_1_1', 'Game_C1_Q1_1_2', 'Game_C1_Q1_1_3', 'Game_C1_Q1_1_4', 'Game_C1_Q1_1_5', 'Game_C1_Q1_1_6', 'Game_C1_Q1_1_7', 'Game_C1_Q1_1_8'],
                   ('1', 2): ['Game_C1_Q2_1_1', 'Game_C1_Q2_1_2', 'Game_C1_Q2_1_3', 'Game_C1_Q2_1_4', 'Game_C1_Q2_1_5', 'Game_C1_Q2_1_6', 'Game_C1_Q2_1_7', 'Game_C1_Q2_1_8'],
                   ('1', 3): ['Game_C1_Q3_1_1', 'Game_C1_Q3_1_2', 'Game_C1_Q3_1_3', 'Game_C1_Q3_1_4', 'Game_C1_Q3_1_5', 'Game_C1_Q3_1_6', 'Game_C1_Q3_1_7', 'Game_C1_Q3_1_8'],
                   ('1', 4): ['Game_C1_Q4_1_1', 'Game_C1_Q4_1_2', 'Game_C1_Q4_1_3', 'Game_C1_Q4_1_4', 'Game_C1_Q4_1_5', 'Game_C1_Q4_1_6', 'Game_C1_Q4_1_7', 'Game_C1_Q4_1_8'],
                   ('1', 5): ['Game_C1_Q5_1_1', 'Game_C1_Q5_1_2', 'Game_C1_Q5_1_3', 'Game_C1_Q5_1_4', 'Game_C1_Q5_1_5', 'Game_C1_Q5_1_6', 'Game_C1_Q5_1_7', 'Game_C1_Q5_1_8'],
                   ('1', 6): ['Game_C1_Q6_1_1', 'Game_C1_Q6_1_2', 'Game_C1_Q6_1_3', 'Game_C1_Q6_1_4', 'Game_C1_Q6_1_5', 'Game_C1_Q6_1_6', 'Game_C1_Q6_1_7', 'Game_C1_Q6_1_8'],
                   ('1', 7): ['Game_C1_Q7_1_1', 'Game_C1_Q7_1_2', 'Game_C1_Q7_1_3', 'Game_C1_Q7_1_4', 'Game_C1_Q7_1_5', 'Game_C1_Q7_1_6', 'Game_C1_Q7_1_7', 'Game_C1_Q7_1_8'],
                   ('1', 8): ['Game_C1_Q8_1_1', 'Game_C1_Q8_1_2', 'Game_C1_Q8_1_3', 'Game_C1_Q8_1_4', 'Game_C1_Q8_1_5', 'Game_C1_Q8_1_6', 'Game_C1_Q8_1_7', 'Game_C1_Q8_1_8'],
                   ('1', 9): ['Game_C1_Q9_1_1', 'Game_C1_Q9_1_2', 'Game_C1_Q9_1_3', 'Game_C1_Q9_1_4', 'Game_C1_Q9_1_5', 'Game_C1_Q9_1_6', 'Game_C1_Q9_1_7', 'Game_C1_Q9_1_8'],
                   ('1', 10): ['Cohort1_Q10_1_1', 'Cohort1_Q10_1_2', 'Cohort1_Q10_1_3', 'Cohort1_Q10_1_4', 'Cohort1_Q10_1_5', 'Cohort1_Q10_1_6', 'Cohort1_Q10_1_7', 'Cohort1_Q10_1_8'],
                   ('2', 1): ['Game_C24_Q1_1', 'Game_C24_Q1_2', 'Game_C24_Q1_3', 'Game_C24_Q1_4', 'Game_C24_Q1_5', 'Game_C24_Q1_6', 'Game_C24_Q1_7', 'Game_C24_Q1_8'],
                   ('2', 2): ['Game_C24_Q2_1', 'Game_C24_Q2_2', 'Game_C24_Q2_3', 'Game_C24_Q2_4', 'Game_C24_Q2_5', 'Game_C24_Q2_6', 'Game_C24_Q2_7', 'Game_C24_Q2_8'],
                   ('2', 3): ['Game_C24_Q3_1', 'Game_C24_Q3_2', 'Game_C24_Q3_3', 'Game_C24_Q3_4', 'Game_C24_Q3_5', 'Game_C24_Q3_6', 'Game_C24_Q3_7', 'Game_C24_Q3_8'],
                   ('2', 4): ['Game_C24_Q4_1', 'Game_C24_Q4_2', 'Game_C24_Q4_3', 'Game_C24_Q4_4', 'Game_C24_Q4_5', 'Game_C24_Q4_6', 'Game_C24_Q4_7', 'Game_C24_Q4_8'],
                   ('2', 5): ['Game_C24_Q5_1', 'Game_C24_Q5_2', 'Game_C24_Q5_3', 'Game_C24_Q5_4', 'Game_C24_Q5_5', 'Game_C24_Q5_6', 'Game_C24_Q5_7', 'Game_C24_Q5_8'],
                   ('2', 6): ['Game_C24_Q6_1', 'Game_C24_Q6_2', 'Game_C24_Q6_3', 'Game_C24_Q6_4', 'Game_C24_Q6_5', 'Game_C24_Q6_6', 'Game_C24_Q6_7', 'Game_C24_Q6_8'],
                   ('2', 7): ['Game_C24_Q7_1', 'Game_C24_Q7_2', 'Game_C24_Q7_3', 'Game_C24_Q7_4', 'Game_C24_Q7_5', 'Game_C24_Q7_6', 'Game_C24_Q7_7', 'Game_C24_Q7_8'],
                   ('2', 8): ['Game_C24_Q8_1', 'Game_C24_Q8_2', 'Game_C24_Q8_3', 'Game_C24_Q8_4', 'Game_C24_Q8_5', 'Game_C24_Q8_6', 'Game_C24_Q8_7', 'Game_C24_Q8_8'],
                   ('2', 9): ['Game_C24_Q9_1', 'Game_C24_Q9_2', 'Game_C24_Q9_3', 'Game_C24_Q9_4', 'Game_C24_Q9_5', 'Game_C24_Q9_6', 'Game_C24_Q9_7', 'Game_C24_Q9_8'],
                   ('2', 10): ['Cohort24_Q10_1', 'Cohort24_Q10_2', 'Cohort24_Q10_3', 'Cohort24_Q10_4', 'Cohort24_Q10_5', 'Cohort24_Q10_6', 'Cohort24_Q10_7', 'Cohort24_Q10_8'],
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
                   ('4', 5): ['Game_C24_Q5_1_1', 'Game_C24_Q5_1_2', 'Game_C24_Q5_1_3', 'Game_C24_Q5_1_4', 'Game_C24_Q5_1_5', 'Game_C24_Q5_1_6', 'Game_C24_Q5_1_7', 'Game_C24_Q5_1_8'],
                   ('4', 6): ['Game_C24_Q6_1_1', 'Game_C24_Q6_1_2', 'Game_C24_Q6_1_3', 'Game_C24_Q6_1_4', 'Game_C24_Q6_1_5', 'Game_C24_Q6_1_6', 'Game_C24_Q6_1_7', 'Game_C24_Q6_1_8'],
                   ('4', 7): ['Game_C24_Q7_1_1', 'Game_C24_Q7_1_2', 'Game_C24_Q7_1_3', 'Game_C24_Q7_1_4', 'Game_C24_Q7_1_5', 'Game_C24_Q7_1_6', 'Game_C24_Q7_1_7', 'Game_C24_Q7_1_8'],
                   ('4', 8): ['Game_C24_Q8_1_1', 'Game_C24_Q8_1_2', 'Game_C24_Q8_1_3', 'Game_C24_Q8_1_4', 'Game_C24_Q8_1_5', 'Game_C24_Q8_1_6', 'Game_C24_Q8_1_7', 'Game_C24_Q8_1_8'],
                   ('4', 9): ['Game_C24_Q9_1_1', 'Game_C24_Q9_1_2', 'Game_C24_Q9_1_3', 'Game_C24_Q9_1_4', 'Game_C24_Q9_1_5', 'Game_C24_Q9_1_6', 'Game_C24_Q9_1_7', 'Game_C24_Q9_1_8'],
                   ('4', 10): ['Cohort24_Q10_1_1', 'Cohort24_Q10_1_2', 'Cohort24_Q10_1_3', 'Cohort24_Q10_1_4', 'Cohort24_Q10_1_5', 'Cohort24_Q10_1_6', 'Cohort24_Q10_1_7', 'Cohort24_Q10_1_8'],
                   ('5', 1): ['Game_C35_Q1_table_1_1', 'Game_C35_Q1_table_1_2', 'Game_C35_Q1_table_1_3', 'Game_C35_Q1_table_1_4', 'Game_C35_Q1_table_1_5', 'Game_C35_Q1_table_1_6', 'Game_C35_Q1_table_1_7', 'Game_C35_Q1_table_1_8'],
                   ('5', 2): ['Game_C35_Q2_table_1_1', 'Game_C35_Q2_table_1_2', 'Game_C35_Q2_table_1_3', 'Game_C35_Q2_table_1_4', 'Game_C35_Q2_table_1_5', 'Game_C35_Q2_table_1_6', 'Game_C35_Q2_table_1_7', 'Game_C35_Q2_table_1_8'],
                   ('5', 3): ['Game_C35_Q3_table_1_1', 'Game_C35_Q3_table_1_2', 'Game_C35_Q3_table_1_3', 'Game_C35_Q3_table_1_4', 'Game_C35_Q3_table_1_5', 'Game_C35_Q3_table_1_6', 'Game_C35_Q3_table_1_7', 'Game_C35_Q3_table_1_8'],
                   ('5', 4): ['Game_C35_Q4_table_1_1', 'Game_C35_Q4_table_1_2', 'Game_C35_Q4_table_1_3', 'Game_C35_Q4_table_1_4', 'Game_C35_Q4_table_1_5', 'Game_C35_Q4_table_1_6', 'Game_C35_Q4_table_1_7', 'Game_C35_Q4_table_1_8'],
                   ('5', 5): ['Game_C35_Q5_table_1_1', 'Game_C35_Q5_table_1_2', 'Game_C35_Q5_table_1_3', 'Game_C35_Q5_table_1_4', 'Game_C35_Q5_table_1_5', 'Game_C35_Q5_table_1_6', 'Game_C35_Q5_table_1_7', 'Game_C35_Q5_table_1_8'],
                   ('5', 6): ['Game_C35_Q6_table_1_1', 'Game_C35_Q6_table_1_2', 'Game_C35_Q6_table_1_3', 'Game_C35_Q6_table_1_4', 'Game_C35_Q6_table_1_5', 'Game_C35_Q6_table_1_6', 'Game_C35_Q6_table_1_7', 'Game_C35_Q6_table_1_8'],
                   ('5', 7): ['Game_C35_Q7_table_1_1', 'Game_C35_Q7_table_1_2', 'Game_C35_Q7_table_1_3', 'Game_C35_Q7_table_1_4', 'Game_C35_Q7_table_1_5', 'Game_C35_Q7_table_1_6', 'Game_C35_Q7_table_1_7', 'Game_C35_Q7_table_1_8'],
                   ('5', 8): ['Game_C35_Q8_table_1_1', 'Game_C35_Q8_table_1_2', 'Game_C35_Q8_table_1_3', 'Game_C35_Q8_table_1_4', 'Game_C35_Q8_table_1_5', 'Game_C35_Q8_table_1_6', 'Game_C35_Q8_table_1_7', 'Game_C35_Q8_table_1_8'],
                   ('5', 9): ['Game_C35_Q9_table_1_1', 'Game_C35_Q9_table_1_2', 'Game_C35_Q9_table_1_3', 'Game_C35_Q9_table_1_4', 'Game_C35_Q9_table_1_5', 'Game_C35_Q9_table_1_6', 'Game_C35_Q9_table_1_7', 'Game_C35_Q9_table_1_8'],
                   ('5', 10): ['Cohort35_Q10_table_1_1', 'Cohort35_Q10_table_1_2', 'Cohort35_Q10_table_1_3', 'Cohort35_Q10_table_1_4', 'Cohort35_Q10_table_1_5', 'Cohort35_Q10_table_1_6', 'Cohort35_Q10_table_1_7', 'Cohort35_Q10_table_1_8']}


cohort_training_col = {('1', 1): ["Training_C1_Q1_1", "Training_C1_Q1_2", "Training_C1_Q1_3", "Training_C1_Q1_4", "Training_C1_Q1_5", "Training_C1_Q1_6", "Training_C1_Q1_7", "Training_C1_Q1_8"],
                       ('1', 2): ["Training_C1_Q2_1", "Training_C1_Q2_2", "Training_C1_Q2_3", "Training_C1_Q2_4", "Training_C1_Q2_5", "Training_C1_Q2_6", "Training_C1_Q2_7", "Training_C1_Q2_8"],
                       ('1', 3): ["Training_C1_Q3_1", "Training_C1_Q3_2", "Training_C1_Q3_3", "Training_C1_Q3_4", "Training_C1_Q3_5", "Training_C1_Q3_6", "Training_C1_Q3_7", "Training_C1_Q3_8"],
                       ('1', 4): ["Training_C1_Q4_1", "Training_C1_Q4_2", "Training_C1_Q4_3", "Training_C1_Q4_4", "Training_C1_Q4_5", "Training_C1_Q4_6", "Training_C1_Q4_7", "Training_C1_Q4_8"],
                       ('2', 1): ["Training_C24_Q1_1", "Training_C24_Q1_2", "Training_C24_Q1_3", "Training_C24_Q1_4", "Training_C24_Q1_5", "Training_C24_Q1_6", "Training_C24_Q1_7", "Training_C24_Q1_8"],
                       ('2', 2): ["Training_C24_Q2_1", "Training_C24_Q2_2", "Training_C24_Q2_3", "Training_C24_Q2_4", "Training_C24_Q2_5", "Training_C24_Q2_6", "Training_C24_Q2_7", "Training_C24_Q2_8"],
                       ('2', 3): ["Training_C24_Q3_1", "Training_C24_Q3_2", "Training_C24_Q3_3", "Training_C24_Q3_4", "Training_C24_Q3_5", "Training_C24_Q3_6", "Training_C24_Q3_7", "Training_C24_Q3_8"],
                       ('2', 4): ["Training_C24_Q4_1", "Training_C24_Q4_2", "Training_C24_Q4_16", "Training_C24_Q4_17", "Training_C24_Q4_18", "Training_C24_Q4_19", "Training_C24_Q4_20", "Training_C24_Q4_21"],
                       ('3', 1): ["Training_C35_Q1_1_1", "Training_C35_Q1_1_2", "Training_C35_Q1_1_3", "Training_C35_Q1_1_4", "Training_C35_Q1_1_5", "Training_C35_Q1_1_6", "Training_C35_Q1_1_7", "Training_C35_Q1_1_8"],
                       ('3', 2): ["Training_C35_Q2_1_1", "Training_C35_Q2_1_2", "Training_C35_Q2_1_3", "Training_C35_Q2_1_4", "Training_C35_Q2_1_5", "Training_C35_Q2_1_6", "Training_C35_Q2_1_7", "Training_C35_Q2_1_8"],
                       ('3', 3): ["Training_C35_Q3_1_1", "Training_C35_Q3_1_2", "Training_C35_Q3_1_3", "Training_C35_Q3_1_4", "Training_C35_Q3_1_5", "Training_C35_Q3_1_6", "Training_C35_Q3_1_7", "Training_C35_Q3_1_8"],
                       ('3', 4): ["Training_C35_Q4_1_1", "Training_C35_Q4_1_2", "Training_C35_Q4_1_3", "Training_C35_Q4_1_4", "Training_C35_Q4_1_5", "Training_C35_Q4_1_6", "Training_C35_Q4_1_7", "Training_C35_Q4_1_8"],
                       ('4', 1): ["Training_C24_Q1_1_1", "Training_C24_Q1_1_2", "Training_C24_Q1_1_3", "Training_C24_Q1_1_4", "Training_C24_Q1_1_5", "Training_C24_Q1_1_6", "Training_C24_Q1_1_7", "Training_C24_Q1_1_8"],
                       ('4', 2): ["Training_C24_Q2_1_1", "Training_C24_Q2_1_2", "Training_C24_Q2_1_3", "Training_C24_Q2_1_4", "Training_C24_Q2_1_5", "Training_C24_Q2_1_6", "Training_C24_Q2_1_7", "Training_C24_Q2_1_8"],
                       ('4', 3): ["Training_C24_Q3_1_1", "Training_C24_Q3_1_2", "Training_C24_Q3_1_3", "Training_C24_Q3_1_4", "Training_C24_Q3_1_5", "Training_C24_Q3_1_6", "Training_C24_Q3_1_7", "Training_C24_Q3_1_8"],
                       ('4', 4): ["Training_C24_Q4_1_1", "Training_C24_Q4_1_2", "Training_C24_Q4_1_16", "Training_C24_Q4_1_17", "Training_C24_Q4_1_18", "Training_C24_Q4_1_19", "Training_C24_Q4_1_20", "Training_C24_Q4_1_21"],
                       ('5', 1): ["Training_C35_Q1_tabl_1_1", "Training_C35_Q1_tabl_1_2", "Training_C35_Q1_tabl_1_3", "Training_C35_Q1_tabl_1_4", "Training_C35_Q1_tabl_1_5", "Training_C35_Q1_tabl_1_6", "Training_C35_Q1_tabl_1_7", "Training_C35_Q1_tabl_1_8"],
                       ('5', 2): ["Training_C35_Q2_tabl_1_1", "Training_C35_Q2_tabl_1_2", "Training_C35_Q2_tabl_1_3", "Training_C35_Q2_tabl_1_4", "Training_C35_Q2_tabl_1_5", "Training_C35_Q2_tabl_1_6", "Training_C35_Q2_tabl_1_7", "Training_C35_Q2_tabl_1_8"],
                       ('5', 3): ["Training_C35_Q3_tabl_1_1", "Training_C35_Q3_tabl_1_2", "Training_C35_Q3_tabl_1_3", "Training_C35_Q3_tabl_1_4", "Training_C35_Q3_tabl_1_5", "Training_C35_Q3_tabl_1_6", "Training_C35_Q3_tabl_1_7", "Training_C35_Q3_tabl_1_8"],
                       ('5', 4): ["Training_C35_Q4_tabl_1_1", "Training_C35_Q4_tabl_1_2", "Training_C35_Q4_tabl_1_3", "Training_C35_Q4_tabl_1_4", "Training_C35_Q4_tabl_1_5", "Training_C35_Q4_tabl_1_6", "Training_C35_Q4_tabl_1_7", "Training_C35_Q4_tabl_1_8"]}


time_game_col = {'1': ["Game_C1_Q1_time_Page Submit", "Game_C1_Q2_time_Page Submit", "Game_C1_Q3_time_Page Submit", "Game_C1_Q4_time_Page Submit", "Game_C1_Q5_time_Page Submit", "Game_C1_Q6_time_Page Submit", "Game_C1_Q7_time_Page Submit", "Game_C1_Q8_time_Page Submit", "Game_C1_Q9_time_Page Submit", "Cohort1_Q10_time_Page Submit"],
                 '2': ["Game_C24_Q1_time_Page Submit", "Game_C24_Q2_time_Page Submit", "Game_C24_Q3_time_Page Submit", "Game_C24_Q4_time_Page Submit", "Game_C24_Q5_time_Page Submit", "Game_C24_Q6_time_Page Submit", "Game_C24_Q7_time_Page Submit", "Game_C24_Q8_time_Page Submit", "Game_C24_Q9_time_Page Submit", "Cohort24_Q10_time_Page Submit"],
                 '3': ["Game_C35_Q1_time_Page Submit", "Game_C35_Q2_time_Page Submit", "Game_C35_Q3_time_Page Submit", "Game_C35_Q4_time_Page Submit", "Game_C35_Q5_time_Page Submit", "Game_C35_Q6_time_Page Submit", "Game_C35_Q7_time_Page Submit", "Game_C35_Q8_time_Page Submit", "Game_C35_Q9_time_Page Submit", "Cohort35_Q10_time_Page Submit"],
                 '4': ["Game_C24_Q1_time_Page Submit", "Game_C24_Q2_time_Page Submit", "Game_C24_Q3_time_Page Submit", "Game_C24_Q4_time_Page Submit", "Game_C24_Q5_time_Page Submit", "Game_C24_Q6_time_Page Submit", "Game_C24_Q7_time_Page Submit", "Game_C24_Q8_time_Page Submit", "Game_C24_Q9_time_Page Submit", "Cohort24_Q10_time_Page Submit"],
                 '5': ["Game_C35_Q1_time_Page Submit", "Game_C35_Q2_time_Page Submit", "Game_C35_Q3_time_Page Submit", "Game_C35_Q4_time_Page Submit", "Game_C35_Q5_time_Page Submit", "Game_C35_Q6_time_Page Submit", "Game_C35_Q7_time_Page Submit", "Game_C35_Q8_time_Page Submit", "Game_C35_Q9_time_Page Submit", "Cohort35_Q10_time_Page Submit"]}


time_training_col = {'1': ["Training_C1_Q1_time_Page Submit", "Training_C1_Q2_time_Page Submit", "Training_C1_Q3_time_Page Submit", "Training_C1_Q4_time_Page Submit"],
                     '2': ["Training_C24_Q1_time_Page Submit", "Training_C24_Q2_time_Page Submit", "Training_C24_Q3_time_Page Submit","Training_C24_Q4_time_Page Submit"],
                     '3': ["Training_C35_Q1_time_Page Submit", "Training_C35_Q2_time_Page Submit", "Training_C35_Q3_time_Page Submit", "Training_C35_Q4_time_Page Submit"],
                     '4': ["Training_C24_Q1_time_Page Submit", "Training_C24_Q2_time_Page Submit", "Training_C24_Q3_time_Page Submit","Training_C24_Q4_time_Page Submit"],
                     '5': ["Training_C35_Q1_time_Page Submit", "Training_C35_Q2_time_Page Submit", "Training_C35_Q3_time_Page Submit", "Training_C35_Q4_time_Page Submit"]}               


sol_game = {1: [1, 0, 0, 1, 2, 3, 1, 1],
            2: [1, 4, 1, 0, 0, 0, 1, 2],
            3: [0, 1, 0, 1, 2, 3, 1, 1],
            4: [0, 0, 0, 1, 2, 4, 2, 0],
            5: [2, 1, 2, 1, 1, 1, 1, 0],
            6: [0, 2, 1, 1, 0, 3, 1, 1],
            7: [0, 1, 1, 1, 2, 1, 2, 1],
            8: [3, 2, 3, 1, 0, 0, 0, 0],
            9: [1, 1, 1, 2, 1, 1, 1, 1],
            10: [0, 1, 0, 2, 2, 3, 0, 1]}


sol_training = {1: [0, 1, 0, 1, 0, 2, 0, 1],
                2: [0, 1, 1, 1, 0, 0, 0, 2],
                3: [1, 0, 0, 0, 2, 0, 2, 0],
                4: [1, 1, 1, 0, 1, 0, 1, 0]}


CA_game = {1: [1, 0, 0, 0, 2, 3, 1, 0],
           2: [0, 4, 1, 0, 0, 0, 0, 2],
           3: [1, 0, 1, 1, 2, 3, 0, 1],
           4: [0, 0, 0, 0, 2, 4, 2, 1],
           5: [2, 1, 2, 1, 1, 1, 1, 1],
           6: [1, 2, 1, 1, 0, 3, 1, 1],
           7: [0, 1, 1, 1, 2, 1, 2, 1],
           8: [3, 2, 3, 1, 0, 0, 0, 0],
           9: [1, 1, 1, 2, 1, 1, 1, 1],
           10: [0, 1, 0, 2, 2, 3, 0, 1]}


CA_training = {1: [0, 1, 0, 1, 0, 2, 0, 0],
               2: [0, 2, 0, 1, 0, 0, 0, 2],
               3: [2, 0, 0, 0, 2, 0, 2, 0],
               4: [1, 1, 1, 0, 1, 0, 1, 0]}



data = data.query("Finished == True & Status != 'Survey Preview'")
##print(data.head(10))

"""
Prints the result of each participant in each game and whether it's true or not. 
"""
def correct_rate(data):
   for i in range(len(data)):
      row = data.iloc[i, : ]
      case = str(row['cohort_num'])
      print(row['Prolific_ver'], " (",case,")")
      for qnum in range(1, 11):
          answer = [int(row[cohort_game_col[(case, qnum)][i]]) for i in range(8)]
          print(qnum, ": ", answer, sol_game[qnum] == answer)

"""
This function Arranges and writes the data into a CSV in the following format:
1. Mturk_ID, cohort - participants Mturk ID and cohort number (1-5)
2. Training- for each question:
   a. trainingX_success - whether succeded or not (boolean)
   b. trainingX_time - time it took
   And overall success rate (out of 4 questions)
3. Game - for each question:
   a. gameX_success - Whether succeded or not (boolean)
   b. gameX_time - time it took
   c. gameX_sum_identified - How many symbols identified in total (correct should be always 9)
   d. gameX_success_rate - how many symbols quantities (out of 8) were identified correctly
   e. gameX_success_distance - how distant is the participant answer from the correct answer (in Manhattan Distance) to estimate the proximity of the answer to the right answer.
   f. gameX_ca_agreed - whether agreed with CA or not (boolean)
4. game_sum_success_total - how many correct answers the participant get in total
5. total_time - total time the participant spend in qualtrics (for MTurk compensation)
6. average_game_time - average time the participant spend in the 10 game questions 
7. game_sum_ca_agreed_total - How many times the participant agreed with the CA, in total
8. game_sum_agreed_ca_right - How many times the participant agreed with the CA, when CA was right
9. game_sum_agreed_ca_wrong - How many times the participant agreed with the CA, when CA was wrong
10. game_sum_disagreed_ca_right- How many times the participant disagreed with the CA, when CA was right
11. game_sum_disagreed_ca_wrong_success - How many times the participant disagreed with the CA, when CA was wrong, and the participant answered correctly
12. game_sum_disagreed_ca_wrong_failure - How many times the participant disagreed with the CA, when CA was wrong, and the participant answered incorrectly
13. Questionnaires  -
    a. avg_task_load - Average grade of task load questions
    b. avg_trust - Average grade of CA trust questionnaire  (relevant to cohort 2-5)
    c. avg_explanation - Average grade of explanation satisfaction questionnaire  (relevant to cohort 3-5)
"""
def arrange_csv(data):
   rows = []
   rows.append(headers)
   
   for i in range(len(data)):
      row = data.iloc[i, :]
      case = str(row['cohort_num'])
      print(len(data))
      new_row = [row['Prolific_ver'], row['cohort_num'], row['consent2'], row['gender'], row['nativeness']]
      training_success = 0

      for qnum in range(1, 5): #Adding training section
         answer = [int(row[cohort_training_col[(case, qnum)][i]]) for i in range(8)]
         solution = sol_training[qnum]
         
         new_row.append(sol_training[qnum] == answer)
         training_success += (sol_training[qnum] == answer)
         new_row.append(round(row[time_training_col[case][qnum - 1]], 2))

         distance_vec = []

         for x, y in zip(answer, solution): #adding letters individual distance
              distance_vec.append(abs(x - y))
        
         new_row = new_row + distance_vec
         new_row.append(sum(distance_vec)) 

      new_row.append(training_success) #adding overall training success

      sum_game_success = 0
      sum_ca_agreed = 0
      sum_ca_agreed_right = 0
      sum_ca_agreed_wrong = 0
      sum_ca_disagreed_right = 0
      sum_ca_disagreed_wrong_success = 0
      sum_ca_disagreed_wrong_failure = 0
      total_game_time = 0
      bool_ca_right = False

      for qnum in range(1, 11): #adding game section
          if qnum == 7: #CA is right in Q7-Q10
              bool_ca_right = True

          answer = [int(row[cohort_game_col[(case, qnum)][i]]) for i in range (8)]
          solution = sol_game[qnum] 
          new_row.append(solution == answer) #append 3a
          game_success = int(solution == answer)
          sum_game_success += (game_success)

          game_time = round(row[time_game_col[case][qnum -1]], 2)
          total_game_time += game_time
          new_row.append(game_time) #append 3b
         
          new_row.append(sum(answer)) #append 3c
        
          new_row.append(sum(x==y for x, y in zip(answer, solution))) #append 3d
          
          distance_vec = []

          for x, y in zip(answer, solution): #adding letters individual distance
              distance_vec.append(abs(x - y))
        
          new_row = new_row + distance_vec
          new_row.append(sum(distance_vec)) #append 3e
          new_row.append(CA_game[qnum] == answer) #append 3f
        
          ca_agreed = int(CA_game[qnum] == answer)
          sum_ca_agreed += ca_agreed
          sum_ca_agreed_right += (ca_agreed and bool_ca_right)
          sum_ca_agreed_wrong += (ca_agreed and (not bool_ca_right))
          sum_ca_disagreed_right += ((not ca_agreed) and bool_ca_right)
          sum_ca_disagreed_wrong_success += ((not ca_agreed) and (not bool_ca_right) and game_success)
          sum_ca_disagreed_wrong_failure += ((not ca_agreed) and (not bool_ca_right) and (not game_success))

      new_row.append(sum_game_success) #append 4
      new_row.append(row['Duration (in seconds)']) #append 5
      new_row.append(total_game_time/10) #append 6
      new_row.append(sum_ca_agreed) #append 7
      new_row.append(sum_ca_agreed_right) #append 8
      new_row.append(sum_ca_agreed_wrong) #append 9
      new_row.append(sum_ca_disagreed_right) #append 10
      new_row.append(sum_ca_disagreed_wrong_success) #append 11
      new_row.append(sum_ca_disagreed_wrong_failure) #append 12
      new_row.append(row['avg_task_load']) #append 13
      new_row.append(row['avg_trust'])
      new_row.append(row['avg_explanation'])

      rows.append(new_row)

   table = pd.DataFrame(rows)
   table.to_csv("processedData_c5.csv", header = False, index = False)

arrange_csv(data)
#correct_rate(data)
