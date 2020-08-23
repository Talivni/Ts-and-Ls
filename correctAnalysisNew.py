import numpy as np
import pandas as pd 
import re
import matplotlib.pyplot as plt

data = pd.read_csv("C:\\Users\\talil\\OneDrive\\Documents\\GitHub\\Ts-and-Ls\\ver3.csv")

headers = ["Mturk_ID", "cohort", "training1_success", "training1_time", "training2_success", "training_2_time", "training3_success", "training3_time", "training4_success", "training4_time", "training_sum_success",
           "game1_success", "game1_time", "game1_sum_identified", "game1_success_rate", "game1_success_distance", "game1_ca_agreed", "game2_success", "game2_time", "game2_sum_identified", "game2_success_rate", "game2_success_distance", "game2_ca_agreed",
           "game3_success", "game3_time", "game3_sum_identified", "game3_success_rate", "game3_success_distance", "game3_ca_agreed", "game4_success", "game4_time", "game4_sum_identified", "game4_success_rate", "game4_success_distance", "game4_ca_agreed",
           "game5_success", "game5_time", "game5_sum_identified", "game5_success_rate", "game5_success_distance", "game5_ca_agreed", "game6_success", "game6_time", "game6_sum_identified", "game6_success_rate", "game6_success_distance", "game6_ca_agreed",
           "game7_success", "game7_time", "game7_sum_identified", "game7_success_rate", "game7_success_distance", "game7_ca_agreed", "game8_success", "game8_time", "game8_sum_identified", "game8_success_rate", "game8_success_distance", "game8_ca_agreed",
           "game9_success", "game9_time", "game9_sum_identified", "game9_success_rate", "game9_success_distance", "game9_ca_agreed", "game10_success", "game10_time", "game10_sum_identified", "game10_success_rate", "game10_success_distance", "game10_ca_agreed",
           "game_sum_success_total", "total_time", "average_game_time", "game_sum_ca_agreed_total", "game_sum_agreed_ca_correct", "game_sum_agreed_ca_wrong", "game_sum_disagreed_ca_correct", "game_sum_disagreed_ca_wrong_success", "game_sum_disagreed_ca_wrong_failure", "avg_task_load", "avg_trust", "avg_explanation"]


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
                   ('2', 1): ['Game_C24_Q1_1_1', 'Game_C24_Q1_1_2', 'Game_C24_Q1_1_3', 'Game_C24_Q1_1_4', 'Game_C24_Q1_1_5', 'Game_C24_Q1_1_6', 'Game_C24_Q1_1_7', 'Game_C24_Q1_1_8'],
                   ('2', 2): ['Game_C24_Q2_1_1', 'Game_C24_Q2_1_2', 'Game_C24_Q2_1_3', 'Game_C24_Q2_1_4', 'Game_C24_Q2_1_5', 'Game_C24_Q2_1_6', 'Game_C24_Q2_1_7', 'Game_C24_Q2_1_8'],
                   ('2', 3): ['Game_C24_Q3_1_1', 'Game_C24_Q3_1_2', 'Game_C24_Q3_1_3', 'Game_C24_Q3_1_4', 'Game_C24_Q3_1_5', 'Game_C24_Q3_1_6', 'Game_C24_Q3_1_7', 'Game_C24_Q3_1_8'],
                   ('2', 4): ['Game_C24_Q4_1_1', 'Game_C24_Q4_1_2', 'Game_C24_Q4_1_3', 'Game_C24_Q4_1_4', 'Game_C24_Q4_1_5', 'Game_C24_Q4_1_6', 'Game_C24_Q4_1_7', 'Game_C24_Q4_1_8'],
                   ('2', 5): ['Game_C24_Q5_1_1', 'Game_C24_Q5_1_2', 'Game_C24_Q5_1_3', 'Game_C24_Q5_1_4', 'Game_C24_Q5_1_5', 'Game_C24_Q5_1_6', 'Game_C24_Q5_1_7', 'Game_C24_Q5_1_8'],
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
                   ('4', 5): ['Game_C24_Q5_1_1', 'Game_C24_Q5_1_2', 'Game_C24_Q5_1_3', 'Game_C24_Q5_1_4', 'Game_C24_Q5_1_5', 'Game_C24_Q5_1_6', 'Game_C24_Q5_1_7', 'Game_C24_Q5_1_8'],
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


cohort_training_col = {('1', 1): ["Training_C1_Q1_1_1", "Training_C1_Q1_1_2", "Training_C1_Q1_1_3", "Training_C1_Q1_1_4", "Training_C1_Q1_1_5", "Training_C1_Q1_1_6", "Training_C1_Q1_1_7", "Training_C1_Q1_1_8"],
                       ('1', 2): ["Training_C1_Q2_1_1", "Training_C1_Q2_1_2", "Training_C1_Q2_1_3", "Training_C1_Q2_1_4", "Training_C1_Q2_1_5", "Training_C1_Q2_1_6", "Training_C1_Q2_1_7", "Training_C1_Q2_1_8"],
                       ('1', 3): ["Training_C1_Q3_1_1", "Training_C1_Q3_1_2", "Training_C1_Q3_1_3", "Training_C1_Q3_1_4", "Training_C1_Q3_1_5", "Training_C1_Q3_1_6", "Training_C1_Q3_1_7", "Training_C1_Q3_1_8"],
                       ('1', 4): ["Training_C1_Q4_1_1", "Training_C1_Q4_1_2", "Training_C1_Q4_1_3", "Training_C1_Q4_1_4", "Training_C1_Q4_1_5", "Training_C1_Q4_1_6", "Training_C1_Q4_1_7", "Training_C1_Q4_1_8"],
                       ('2', 1): ["Training_C24_Q1_1_1", "Training_C24_Q1_1_2", "Training_C24_Q1_1_3", "Training_C24_Q1_1_4", "Training_C24_Q1_1_5", "Training_C24_Q1_1_6", "Training_C24_Q1_1_7", "Training_C24_Q1_1_8"],
                       ('2', 2): ["Training_C24_Q2_1_1", "Training_C24_Q2_1_2", "Training_C24_Q2_1_3", "Training_C24_Q2_1_4", "Training_C24_Q2_1_5", "Training_C24_Q2_1_6", "Training_C24_Q2_1_7", "Training_C24_Q2_1_8"],
                       ('2', 3): ["Training_C24_Q3_1_1", "Training_C24_Q3_1_2", "Training_C24_Q3_1_3", "Training_C24_Q3_1_4", "Training_C24_Q3_1_5", "Training_C24_Q3_1_6", "Training_C24_Q3_1_7", "Training_C24_Q3_1_8"],
                       ('2', 4): ["Training_C24_Q4_1_1", "Training_C24_Q4_1_2", "Training_C24_Q4_1_3", "Training_C24_Q4_1_4", "Training_C24_Q4_1_5", "Training_C24_Q4_1_6", "Training_C24_Q4_1_7", "Training_C24_Q4_1_8"],
                       ('3', 1): ["Training_C35_Q1_1_1", "Training_C35_Q1_1_2", "Training_C35_Q1_1_3", "Training_C35_Q1_1_4", "Training_C35_Q1_1_5", "Training_C35_Q1_1_6", "Training_C35_Q1_1_7", "Training_C35_Q1_1_8"],
                       ('3', 2): ["Training_C35_Q2_1_1", "Training_C35_Q2_1_2", "Training_C35_Q2_1_3", "Training_C35_Q2_1_4", "Training_C35_Q2_1_5", "Training_C35_Q2_1_6", "Training_C35_Q2_1_7", "Training_C35_Q2_1_8"],
                       ('3', 3): ["Training_C35_Q3_1_1", "Training_C35_Q3_1_2", "Training_C35_Q3_1_3", "Training_C35_Q3_1_4", "Training_C35_Q3_1_5", "Training_C35_Q3_1_6", "Training_C35_Q3_1_7", "Training_C35_Q3_1_8"],
                       ('3', 4): ["Training_C35_Q4_1_1", "Training_C35_Q4_1_2", "Training_C35_Q4_1_3", "Training_C35_Q4_1_4", "Training_C35_Q4_1_5", "Training_C35_Q4_1_6", "Training_C35_Q4_1_7", "Training_C35_Q4_1_8"],
                       ('4', 1): ["Training_C24_Q1_1_1", "Training_C24_Q1_1_2", "Training_C24_Q1_1_3", "Training_C24_Q1_1_4", "Training_C24_Q1_1_5", "Training_C24_Q1_1_6", "Training_C24_Q1_1_7", "Training_C24_Q1_1_8"],
                       ('4', 2): ["Training_C24_Q2_1_1", "Training_C24_Q2_1_2", "Training_C24_Q2_1_3", "Training_C24_Q2_1_4", "Training_C24_Q2_1_5", "Training_C24_Q2_1_6", "Training_C24_Q2_1_7", "Training_C24_Q2_1_8"],
                       ('4', 3): ["Training_C24_Q3_1_1", "Training_C24_Q3_1_2", "Training_C24_Q3_1_3", "Training_C24_Q3_1_4", "Training_C24_Q3_1_5", "Training_C24_Q3_1_6", "Training_C24_Q3_1_7", "Training_C24_Q3_1_8"],
                       ('4', 4): ["Training_C24_Q4_1_1", "Training_C24_Q4_1_2", "Training_C24_Q4_1_3", "Training_C24_Q4_1_4", "Training_C24_Q4_1_5", "Training_C24_Q4_1_6", "Training_C24_Q4_1_7", "Training_C24_Q4_1_8"],
                       ('5', 1): ["Training_C35_Q1_1_1", "Training_C35_Q1_1_2", "Training_C35_Q1_1_3", "Training_C35_Q1_1_4", "Training_C35_Q1_1_5", "Training_C35_Q1_1_6", "Training_C35_Q1_1_7", "Training_C35_Q1_1_8"],
                       ('5', 2): ["Training_C35_Q2_1_1", "Training_C35_Q2_1_2", "Training_C35_Q2_1_3", "Training_C35_Q2_1_4", "Training_C35_Q2_1_5", "Training_C35_Q2_1_6", "Training_C35_Q2_1_7", "Training_C35_Q2_1_8"],
                       ('5', 3): ["Training_C35_Q3_1_1", "Training_C35_Q3_1_2", "Training_C35_Q3_1_3", "Training_C35_Q3_1_4", "Training_C35_Q3_1_5", "Training_C35_Q3_1_6", "Training_C35_Q3_1_7", "Training_C35_Q3_1_8"],
                       ('5', 4): ["Training_C35_Q4_1_1", "Training_C35_Q4_1_2", "Training_C35_Q4_1_3", "Training_C35_Q4_1_4", "Training_C35_Q4_1_5", "Training_C35_Q4_1_6", "Training_C35_Q4_1_7", "Training_C35_Q4_1_8"]}


time_game_col = {'1': ["Game_C1_Q1_time_Page Submit", "Game_C1_Q2_time_Page Submit", "Game_C1_Q3_time_Page Submit", "Game_C1_Q4_time_Page Submit", "Game_C1_Q5_time_Page Submit", "Game_C1_Q6_time_Page Submit", "Game_C1_Q7_time_Page Submit", "Game_C1_Q8_time_Page Submit", "Game_C1_Q9_time_Page Submit", "Cohort1_Q10_time_Page Submit"],
                 '2': ["Game_C24_Q1_time_Page Submit", "Game_C24_Q2_time_Page Submit", "Game_C24_Q3_time_Page Submit", "Game_C24_Q4_time_Page Submit", "Game_C24_Q5_time_Page Submit", "Game_C24_Q6_time_Page Submit", "Game_C24_Q7_time_Page Submit", "Game_C24_Q8_time_Page Submit", "Game_C24_Q9_time_Page Submit", "Cohort24_Q10_time_Page Submit"],
                 '3': ["Game_C35_Q1_time_Page Submit", "Game_C35_Q2_time_Page Submit", "Game_C35_Q3_time_Page Submit", "Game_C35_Q4_time_Page Submit", "Game_C35_Q5_time_Page Submit", "Game_C35_Q6_time_Page Submit", "Game_C35_Q7_time_Page Submit", "Game_C35_Q8_time_Page Submit", "Game_C35_Q9_time_Page Submit", "Game_C35_Q10_time_Page Submit"],
                 '4': ["Game_C24_Q1_time_Page Submit", "Game_C24_Q2_time_Page Submit", "Game_C24_Q3_time_Page Submit", "Game_C24_Q4_time_Page Submit", "Game_C24_Q5_time_Page Submit", "Game_C24_Q6_time_Page Submit", "Game_C24_Q7_time_Page Submit", "Game_C24_Q8_time_Page Submit", "Game_C24_Q9_time_Page Submit", "Cohort24_Q10_time_Page Submit"],
                 '5': ["Game_C35_Q1_time_Page Submit", "Game_C35_Q2_time_Page Submit", "Game_C35_Q3_time_Page Submit", "Game_C35_Q4_time_Page Submit", "Game_C35_Q5_time_Page Submit", "Game_C35_Q6_time_Page Submit", "Game_C35_Q7_time_Page Submit", "Game_C35_Q8_time_Page Submit", "Game_C35_Q9_time_Page Submit", "Game_C35_Q10_time_Page Submit"]}


time_training_col = {'1': ["Training_C1_Q1_time_Page Submit", "Training_C1_Q2_time_Page Submit", "Training_C1_Q3_time_Page Submit", "Training_C1_Q4_time_Page Submit"],
                     '2': ["Training_C24_Q1_time_Page Submit", "Training_C24_Q2_time_Page Submit", "Training_C24_Q3_time_Page Submit","Training_C24_Q4_time_Page Submit"],
                     '3': ["Training_C35_Q1_time_Page Submit", "Training_C35_Q2_time_Page Submit", "Training_C35_Q3_time_Page Submit", "Training_C35_Q4_time_Page Submit"],
                     '4': ["Training_C24_Q1_time_Page Submit", "Training_C24_Q2_time_Page Submit", "Training_C24_Q3_time_Page Submit","Training_C24_Q4_time_Page Submit"],
                     '5': ["Training_C35_Q1_time_Page Submit", "Training_C35_Q2_time_Page Submit", "Training_C35_Q3_time_Page Submit", "Training_C35_Q4_time_Page Submit"]}               


sol_game = {1: [0, 0, 0, 2, 2, 3, 0, 2],
            2: [1, 4, 1, 0, 0, 0, 1, 2],
            3: [2, 2, 3, 0, 0, 0, 2, 0],
            4: [0, 0, 0, 1, 0, 4, 1, 3],
            5: [2, 1, 1, 1, 1, 1, 1, 1],
            6: [0, 2, 1, 1, 0, 3, 1, 1],
            7: [0, 1, 1, 1, 2, 1, 2, 1],
            8: [3, 2, 3, 1, 0, 0, 0, 0],
            9: [1, 1, 1, 2, 1, 1, 1, 1],
            10: [0, 1, 0, 2, 2, 3, 0, 1]}


sol_training = {1: [0, 1, 0, 1, 0, 2, 0, 1],
                2: [0, 1, 1, 1, 0, 0, 0, 2],
                3: [1, 0, 0, 0, 2, 0, 2, 0],
                4: [1, 1, 1, 0, 1, 0, 1, 0]}


CA_game = {1: [0, 0, 0, 1, 2, 3, 0, 1],
           2: [0, 4, 1, 0, 0, 0, 0, 2],
           3: [3, 3, 2, 0, 0, 0, 1, 0],
           4: [0, 0, 0, 0, 0, 4, 1, 4],
           5: [2, 1, 1, 1, 1, 1, 1, 2],
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
      print(row['MTurk'], " (",case,")")
      for qnum in range(1, 11):
          answer = [int(row[cohort_game_col[(case, qnum)][i]]) for i in range(8)]
          print(qnum, ": ", answer, sol_game[qnum] == answer)

"""
This function Arranges and writes the data into a CSV in the following format:
1. Mturk_ID, cohort - participants Mturk ID and cohort number (1-5)
2. Training- for each question:
   a. Whether   or not (boolean)
   b. Time it took
   And overall success rate (out of 4 questions)
3. Game - for each question:
   a. gameX_success - Whether succeded or not (boolean)
   b. gameX_time - Time it took
   c. gameX_sum_identified - How many symbols identified in total (correct should be always 9)
   d. gameX_success_rate - how many symbols quantities (out of 8) were identified correctly
   e. gameX_success_distance - how distant is the participant answer from the correct answer (in Manhattan Distance) to estimate the proximity of the answer to the right answer.
   f. gameX_ca_agreed - whether agreed with CA or not (boolean)
4. Game success in total - how many correct answers the participant get in total
5. Total time - total time the participant spend in qualtrics (for MTurk compensation)
6. Average game time - how much time each question took in average
7. 
"""
def arrange_csv(data):
   df_csv = []
   for i in range(len(data)):
      row = data.iloc[i, :]
      case = str(row['cohort_num'])
      new_row = [row['MTurk'], row['cohort_num']]
      training_success = 0
      game_success = 0
      for qnum in range(1, 5): #Adding training section
         answer = [int(row[cohort_training_col[(case, qnum)][i]]) for i in range (8)]
         new_row.append(sol_training[qnum] == answer)
         training_success += (sol_training[qnum] == answer)
         new_row.append(round(row[time_training_col[case][qnum - 1]], 2))

      new_row.append(training_success) #adding overall success in training

      
      print(new_row)

arrange_csv(data)
#correct_rate(data)
