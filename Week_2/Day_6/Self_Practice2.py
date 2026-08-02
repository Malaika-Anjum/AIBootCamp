#Use Seaborn to create a violen plot or box plot for visualization of the distribution.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Boxplot
df = pd.DataFrame({
    "Department": ["IT", "IT", "IT", "HR", "HR", "HR", "Sales", "Sales", "Sales"],
    "Salary": [50000, 60000, 70000, 45000, 48000, 52000, 55000, 65000, 75000]
})

sns.boxplot(x="Department", y="Salary", data=df)

plt.title("Salary Distribution by Department")
plt.show()

#Violenplot
df = pd.DataFrame({
    "Department": ["IT", "IT", "IT", "HR", "HR", "HR", "Sales", "Sales", "Sales"],
    "Salary": [50000, 60000, 70000, 45000, 48000, 52000, 55000, 65000, 75000]
})

sns.violinplot(x="Department", y="Salary", data=df)

plt.title("Salary Distribution by Department")
plt.show()
