# Perform a two-way ANOVA to test for interaction effects

import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Create data
data = pd.DataFrame({
    "Score": [
        80, 82, 85, 87,
        75, 78, 80, 82,
        90, 92, 94, 95,
        85, 87, 89, 90
    ],
    
    "Method": [
        "Online", "Online", "Online", "Online",
        "Online", "Online", "Online", "Online",
        "Classroom", "Classroom", "Classroom", "Classroom",
        "Classroom", "Classroom", "Classroom", "Classroom"
    ],
    
    "Gender": [
        "Male", "Male", "Female", "Female",
        "Male", "Male", "Female", "Female",
        "Male", "Male", "Female", "Female",
        "Male", "Male", "Female", "Female"
    ]
})

# Two-way ANOVA model
model = ols("Score ~ C(Method) * C(Gender)", data=data).fit()

# ANOVA table
anova_table = sm.stats.anova_lm(model, typ=2)

print(anova_table)