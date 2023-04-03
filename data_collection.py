# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 14:46:39 2023

@author: adity
"""

import glassdoor_scraper as gs
import pandas as pd

path = "G:/Project/ds_salary_proj/chromedriver"

df = gs.get_jobs('data scientist', 15, False, path, 15)

df.to_csv('glassdoor_jobs.csv'.index = False)