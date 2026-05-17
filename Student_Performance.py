import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df =pd.read_csv('StudentsPerformance.csv')
print(df.head(5))
print(df.shape)
print(df.info())
print(df.describe())
print(df[['math score','reading score','writing score']].isnull().sum())
print(df.isnull().sum())
print(df.duplicated().sum())
#EDA
plt.pie(df['parental level of education'].value_counts(),labels=df['parental level of education'].value_counts().index,autopct='%1.1f%%',shadow=True)
plt.title('Parental Level of Education')
plt.show()
#Box plot for score distribution
sns.boxplot(data=df[['math score', 'reading score', 'writing score']])
plt.ylabel('scores')
plt.xlabel('subjects')
print(plt.show())

plt.pie(df[['math score', 'reading score', 'writing score']].mean(),labels=df[['math score', 'reading score', 'writing score']].mean().index,autopct='%1.1f%%')
plt.title('score distribution')
print(plt.show())
# heat map between scores/ numerical values
corr=df[['math score','reading score','writing score']].corr()
print(corr)
sns.heatmap(corr,annot=True,cmap='coolwarm')
print(plt.show())
# MAKING HISTPLOT OF NUMERICAL VALUES
plt.figure(figsize=(20,10))
plt.subplot(2,2,1)
sns.histplot(df['math score'],bins=30,kde=True)
plt.title('MATH SCORE')
plt.subplot(2,2,2)
sns.histplot(df['reading score'],bins=30,kde=True)
plt.title('READING SCORE')
plt.subplot(2,2,3)
sns.histplot(df['writing score'],bins=30,kde=True)
plt.title('WRITING SCORE')

print(plt.show())
