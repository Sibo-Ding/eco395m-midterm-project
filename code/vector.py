import csv
import os
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

df_freq=pd.read_csv(os.path.join("word_freq_tables", "df_freq.csv"))
df_freq_periods=pd.read_csv(os.path.join("word_freq_tables", "df_freq_periods.csv"))

cosine_comparison=pd.DataFrame({ 'First_Work': [],'Second_Work':[],'Cosine_sim':[]})
for i in df_freq.drop(columns=['word']).columns: 
	for j in df_freq.drop(columns=['word']).columns: 

		cos_sim = cosine_similarity(np.array([df_freq[i]]),np.array([df_freq[j]]))
		new_obs=pd.DataFrame({ 'First_Work':[i],'Second_Work':[j],'Cosine_sim':[round(cos_sim[0,0],3)]})
		cosine_comparison= pd.concat([cosine_comparison,new_obs], ignore_index=True)



cosine_matrix= cosine_comparison.pivot(index='First_Work', columns='Second_Work', values='Cosine_sim')		

Books=cosine_matrix.columns.tolist()
early_list = [book for book in Books if book.startswith("Early")]
shk_list = [book for book in Books if book.startswith("Shakespeare")]
late_list=[book for book in Books if book.startswith("Late")]
shakespeare_cos=cosine_matrix.loc[shk_list,shk_list]
shakespeare_cos.to_csv(os.path.join("cosine_sim", "shakespeare_cos.csv"))
Late_cos=cosine_matrix.loc[late_list,late_list]
Late_cos.to_csv(os.path.join("cosine_sim", "Late_cos.csv"))

early_cos=cosine_matrix.loc[early_list,early_list]
early_cos.to_csv(os.path.join("cosine_sim", "early_cos.csv"))

early_vs_late_cos=cosine_matrix.loc[early_list,late_list]
early_vs_late_cos.to_csv(os.path.join("cosine_sim", "early_vs_late_cos.csv"))

early_vs_shk_cos=cosine_matrix.loc[early_list,shk_list]
early_vs_shk_cos.to_csv(os.path.join("cosine_sim", "early_vs_shk_cos.csv"))
late_vs_shk_cos=cosine_matrix.loc[late_list,shk_list]
late_vs_shk_cos.to_csv(os.path.join("cosine_sim", "late_vs_shk_cos.csv"))




cosine_comparison_total=pd.DataFrame({ 'First_Work': [],'Second_Work':[],'Cosine_sim':[]})
for i in df_freq_periods.drop(columns=['word']).columns: 
	for j in df_freq_periods.drop(columns=['word']).columns: 

		cos_sim = cosine_similarity(np.array([df_freq_periods[i]]),np.array([df_freq_periods[j]]))
		new_obs=pd.DataFrame({ 'First_Work':[i],'Second_Work':[j],'Cosine_sim':[round(cos_sim[0,0],3)]})
		cosine_comparison_total= pd.concat([cosine_comparison_total,new_obs], ignore_index=True)


cosine_comparison_total=cosine_comparison_total.pivot(index='First_Work', columns='Second_Work', values='Cosine_sim')

cosine_comparison_total.to_csv(os.path.join("cosine_sim", "cosine_comparison_total.csv"))
