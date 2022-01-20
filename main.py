# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 07:11:41 2021

@author: Huy Do
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import time
import pandas as pd
import numpy as np
import itertools





#os.chdir= ("Directory/Where/The/Dataset/Located")


#read the first dataset
raw_df_1 = pd.read_csv('testing_data_1.csv')
df_1 = pd.DataFrame(raw_df_1)
#Convert target chains into list
target_input = df_1['Entry'].values.tolist()

#Check for name of columns in df_1 if there are more than 2 columns
df_1.columns.tolist() 

#read the second dataset
raw_df_2 = pd.read_csv('testing_data_2.csv')
df_2 = pd.DataFrame(raw_df_2)
query_input = df_2['Entry'].values.tolist()

#Check for name of columns in df_1 if there are more than 2 columns
df_2.columns.tolist() 




def topmatch(target_input,query_input):
    score = []
    rmd = []
    tc = []
    qc = []
    target_list = [] 
    chromedriver_path = 'C:/Users/huydo/Box/Virtual Kuhn Lab/Group Member Folders/Huy Do/Jupyter Workplace/Web Automation/chromedriver_win32/chromedriver.exe'
    for num in range(0, len(target_input)):
        target_chain = target_input[int(num)]
        query_chain = query_input[int(num)]
        #PATH = "/Users/huydo/Desktop/Jupyter Workplace/GNAT Domain-Motifs/chromedriver.exe"
        driver = webdriver.Chrome(chromedriver_path)
        #driver = webdriver.Chrome(PATH)
        #download_dir = "/Users/Huy Do/Desktop/Jupyter Workplace/GNAT Domain-Motifs/"
        driver.get("https://topmatch.services.came.sbg.ac.at/")
        print(driver.title)
        search = driver.find_element_by_name("query_txt")
        search.send_keys(query_chain)
        
        search = driver.find_element_by_name("target_txt")
        search.send_keys(target_chain)
        
        search.send_keys(Keys.RETURN)
        time.sleep(2)
        rmd_path = driver.find_element_by_xpath('//*[@id="algRow1"]/td[5]')
        score_path = driver.find_element_by_xpath('//*[@id="algRow1"]/td[4]')
        tc_path = driver.find_element_by_xpath('//*[@id="algRow1"]/td[3]')
        qc_path = driver.find_element_by_xpath('//*[@id="algRow1"]/td[2]')
        rmd_text = rmd_path.text
        score_text = score_path.text
        tc_text = tc_path.text
        qc_text = qc_path.text
        rmd.append(rmd_text)
        score.append(score_text)
        tc.append(tc_text)
        qc.append(qc_text)
        target_list.append(query_chain)  
        link = driver.find_element_by_link_text("Downloads")
        link.click()
        

        download_link = driver.find_element_by_id("downloadLinkZIP")
        driver.execute_script("$(arguments[0]).click();", download_link)
        time.sleep(5)
        driver.quit()
    print("score = " + str(score)   )
    print("rmd = " + str(rmd)   )
    print("tc = " + str(tc)   )
    print("qc = " + str(qc)   )
    print("target_list = " + str(target_list))
    total_list = pd.DataFrame(
            {'Score': score,
             'RMD': rmd,
             'TC': tc,
             'QC': qc,
             'Target': target_list})
    total_list.to_csv('Topmatch Scoring Data.csv')
    







