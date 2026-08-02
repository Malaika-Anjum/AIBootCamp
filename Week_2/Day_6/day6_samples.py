import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

#Basic Plot
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
plt.plot(x, y)
plt.show()

#################

# #Line Plot
# plt.plot([1, 2, 3], [10, 20, 30], label="Trend", color="purple", linestyle="--", marker="o")
# #Or I can make x y variable and pass it instead of values
# plt.title("Line Plot")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.legend()
# plt.show()

#################

# #Bar Chart
# categories = ["A", "B", "C", "D","E", "F"]
# values = [10, 15, 7, 3, 9, 11]
# plt.bar(categories, values, color="violet")
# plt.title("Bar Chart")
# plt.show()

#################

# #Histogram
# data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
# plt.hist(data, bins=4, color="yellow", edgecolor="black")
# plt.title("Histogram")
# plt.show()

#################

# #Scatter Plot
# x = [1, 2, 3, 4, 5]
# y = [10, 12, 25, 30, 45]
# plt.scatter(x, y, color="red")
# plt.title("Scatter Plot")
# plt.xlabel("X-axis Label")
# plt.ylabel("Y-axis Label")
# plt.legend(["Dataset 1"])
# plt.show()

#################

# #Heatmap
# data = np.random.rand(5, 5)
# sns.heatmap(data, annot=True, cmap="coolwarm")
# plt.title("HeatMap")
# plt.show()

################

# #Pairplot
# df = pd.DataFrame(np.random.randn(5, 5), columns=["A", "B", "C", "D", "E"])
# sns.pairplot(df)
# plt.show()






