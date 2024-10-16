import csv
import os
import pandas as pd
#Set up dataframes to add info in loops
df_freq = pd.DataFrame({ 'word': []})
df_total= pd.DataFrame({ 'word': []})
df_late= pd.DataFrame({ 'word': []})
df_early=pd.DataFrame({ 'word': []})
df_shk=pd.DataFrame({ 'word': []})

#Use listdir to get the filenames. Then loop and create a frequency column for each word in the universe
#Words that appear in a text but do not appear in other becomne 1. 
for f in os.listdir(os.path.join("words_freq")): 

	IN_PATH = os.path.join("words_freq", f)
	file=pd.read_csv(IN_PATH)
	file[f[:-4]]=file["count"]/file["count"].sum()
	file=file[["word",f[:-4]]]
	df_freq=pd.merge(df_freq,file, on='word', how='outer').fillna(0)


#Create a dataframe for each period  
for f in os.listdir(os.path.join("words_freq")):
	if f.startswith("Late"): 
		IN_PATH = os.path.join("words_freq", f)
		file=pd.read_csv(IN_PATH)
		file=file.rename(columns={'count':f[:-4]})
		df_late=pd.merge(df_late,file, on='word', how='outer').fillna(0)
	elif f.startswith("Early"): 
		IN_PATH = os.path.join("words_freq", f)
		file=pd.read_csv(IN_PATH)
		file=file.rename(columns={'count':f[:-4]})
		df_early=pd.merge(df_early,file, on='word', how='outer').fillna(0)	
	elif f.startswith("Shake"): 
		IN_PATH = os.path.join("words_freq", f)
		file=pd.read_csv(IN_PATH)
		file=file.rename(columns={'count':f[:-4]})
		df_shk=pd.merge(df_shk,file, on='word', how='outer').fillna(0)	





df_late["total"]= df_late.drop(columns=['word']).sum(axis=1)
df_late["Late"]=df_late["total"]/df_late["total"].sum()

print(df_late[["word","Late"]])

df_early["total"]= df_early.drop(columns=['word']).sum(axis=1)
df_early["Early"]=df_early["total"]/df_early["total"].sum()


df_shk["total"]= df_shk.drop(columns=['word']).sum(axis=1)
df_shk["Shakespeare"]=df_shk["total"]/df_shk["total"].sum()

both_periods=pd.merge(df_early[["word","Early"]],df_late[["word","Late"]], on='word', how='outer').fillna(0)

df_freq_periods=pd.merge(both_periods,df_shk[["word","Shakespeare"]], on='word', how='outer').fillna(0)

print(df_freq_periods)



