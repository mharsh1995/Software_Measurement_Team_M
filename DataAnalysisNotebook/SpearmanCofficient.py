from scipy.stats import spearmanr
import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_excel(r'C:\Users\nvirk\Desktop\Team-M\Projects\FileUpload\DataAnalysis\Correlation1_2_4.xlsx')

print(df)
for col in df.columns: 
    print(col) 
Adaptive_maintainence_effort = df['Adaptive_maintainence_effort'].tolist();
Defect_density = df['Defect_density'].tolist();

print(Adaptive_maintainence_effort)
print(Defect_density)
coefficient, value = spearmanr(Adaptive_maintainence_effort,Defect_density) 
coefficient= round(coefficient, 2)
value= round(value, 4)
print("Spearman correlation coefficient=", coefficient, "\n", "2 sided p value=",value)
plt.xlabel("Defect_density ")
plt.ylabel("Adaptive_maintainence_effort")
plt.plot(X, Y,coefficient, value) 

fig, ax1 = plt.subplots()
ax1.plot(X, Y, 'bo')
plt.xlabel("Defect_density ")
plt.ylabel("Adaptive_maintainence_effort")
plt.title(r'Spearman Correlation'+' R='+str(coefficient)+' P='+str(value),fontweight="bold")
  
plt.show()
