import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
#print(tips.head())
plt.plot(tips.total_bill)
plt.show()
#print("The current version is :",  sys.version)
#print("The current executable is :", sys.executable)
