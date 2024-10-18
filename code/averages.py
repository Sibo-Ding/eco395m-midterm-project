import csv
import os
import pandas as pd



euc_comparison_totalvsind=pd.read_csv(os.path.join("euc_sim", "euc_comparison_totalvsind_long.csv"),index_col=None)
print(euc_comparison_totalvsind)
