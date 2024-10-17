import csv
import os
import pandas as pd
from scipy.spatial import distance
import numpy as np

df_freq=pd.read_csv(os.path.join("word_freq_tables", "df_freq.csv"))
df_freq_periods=pd.read_csv(os.path.join("word_freq_tables", "df_freq_periods.csv"))
#Run euc distance on each comparison 
euc_comparison=pd.DataFrame({ 'First_Work': [],'Second_Work':[],'euc_sim':[]})
for i in df_freq.drop(columns=['word']).columns: 
	for j in df_freq.drop(columns=['word']).columns: 

		euc_sim = distance.euclidean(np.array([df_freq[i]]),np.array([df_freq[j]]))
		new_obs=pd.DataFrame({ 'First_Work':[i],'Second_Work':[j],'euc_sim':[round(euc_sim,3)]})
		euc_comparison= pd.concat([euc_comparison,new_obs], ignore_index=True)


# Pivot matrix for easier viewing
euc_matrix= euc_comparison.pivot(index='First_Work', columns='Second_Work', values='euc_sim')		
# Seperate combinations for easier viewing 
Books=euc_matrix.columns.tolist()
early_list = [book for book in Books if book.startswith("Early")]
shk_list = [book for book in Books if book.startswith("Shakespeare")]
late_list=[book for book in Books if book.startswith("Late")]
shakespeare_euc=euc_matrix.loc[shk_list,shk_list]
shakespeare_euc.to_csv(os.path.join("euc_sim", "shakespeare_euc.csv"))
Late_euc=euc_matrix.loc[late_list,late_list]
Late_euc.to_csv(os.path.join("euc_sim", "Late_euc.csv"))

early_euc=euc_matrix.loc[early_list,early_list]
early_euc.to_csv(os.path.join("euc_sim", "early_euc.csv"))

early_vs_late_euc=euc_matrix.loc[early_list,late_list]
early_vs_late_euc.to_csv(os.path.join("euc_sim", "early_vs_late_euc.csv"))

early_vs_shk_euc=euc_matrix.loc[early_list,shk_list]
early_vs_shk_euc.to_csv(os.path.join("euc_sim", "early_vs_shk_euc.csv"))
late_vs_shk_euc=euc_matrix.loc[late_list,shk_list]
late_vs_shk_euc.to_csv(os.path.join("euc_sim", "late_vs_shk_euc.csv"))



#Get euclidian distance for the totals
euc_comparison_total=pd.DataFrame({ 'First_Work': [],'Second_Work':[],'euc_sim':[]})
for i in df_freq_periods.drop(columns=['word']).columns: 
	for j in df_freq_periods.drop(columns=['word']).columns: 

		euc_sim = distance.euclidean(np.array([df_freq_periods[i]]),np.array([df_freq_periods[j]]))
		new_obs=pd.DataFrame({ 'First_Work':[i],'Second_Work':[j],'euc_sim':[round(euc_sim,3)]})
		euc_comparison_total= pd.concat([euc_comparison_total,new_obs], ignore_index=True)


euc_comparison_total=euc_comparison_total.pivot(index='First_Work', columns='Second_Work', values='euc_sim')

euc_comparison_total.to_csv(os.path.join("euc_sim", "euc_comparison_total.csv"))

euc_comparison_totalvsind=pd.DataFrame({ 'Group': [],'Work':[],'euc_sim':[]})
for i in df_freq_periods.drop(columns=['word']).columns: 
	for j in df_freq.drop(columns=['word']).columns: 

		euc_sim = distance.euclidean(np.array([df_freq_periods[i]]),np.array([df_freq[j]]))
		new_obs=pd.DataFrame({ 'Group':[i],'Work':[j],'euc_sim':[round(euc_sim,3)]})
		euc_comparison_totalvsind= pd.concat([euc_comparison_totalvsind,new_obs], ignore_index=True)

euc_comparison_totalvsind=euc_comparison_totalvsind.pivot(index='Work', columns='Group', values='euc_sim')


euc_comparison_totalvsind.to_csv(os.path.join("euc_sim", "euc_comparison_totalvsind.csv"))




