import pandas as pd

df= pd.DataFrame({
    "category_column": ["A", "B", "A", "B", "A", "B"],
    "numeric_column": [10, 20, 30, 40, 50, 60]
})

grouped = df.groupby("category_column", as_index=False)

# #Operations
# for name, group in grouped:
#     print(name)
#     print(group)

##################
   
# #Aggregation Operations 
# group_mean = grouped.mean()
# print("Mean is : \n", group_mean)
# group_sum = grouped.sum()
# print("Sum is : \n", group_sum)

#################

# #Aggreagtion Functions
# group_mean = df.groupby("category_column", as_index = False)["numeric_column"].mean()
# print("Mean is : \n", group_mean)

# group_stats = df.groupby("category_column", as_index = False).agg({"numeric_column":["mean", "max", "min"]})
# print("Stats are : \n", group_stats)

#################

# #Pivot Table
# pivot = df.pivot_table(
#     values="numeric_column",
#     index="category_column",
#     aggfunc="mean"
# )
# print("Pivot Table : \n", pivot)

#################

# #Custom Aggregation
# def range_func(x):
#     return x.max() - x.min()

# cus_agg = df.groupby("category_column")["numeric_column"].agg(range_func)
# print(cus_agg)

group_mean = df.groupby("category_column")["numeric_column"].mean()
print("Mean is : \n", group_mean)

group_max = df.groupby("category_column")["numeric_column"].max()
print("Max is : \n", group_max)

group_min = df.groupby("category_column")["numeric_column"].min()
print("Min is : \n", group_min)