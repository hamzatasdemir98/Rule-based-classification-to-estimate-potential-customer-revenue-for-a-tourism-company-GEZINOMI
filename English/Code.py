## Importing necessary libraries

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

#The data set contains sales data of Gezinomi company. However, since I cannot share this data,
# I shared the manipulated data set with which you can use the same logic.
# Concept information includes options such as all-inclusive and half-board.
# City information contains information in which city the holiday will be held.
# Season information contains information about the summer and winter seasons.

df = pd.read_excel("datasets/dataset.xlsx")
df.head()
df.info()

#Rule-Based Classification

#Step-1 The average price is calculated for all combinations of concept, city and season information.

df = df.groupby(["concept_type", "city_name", "season_number"]).agg({"price": "mean"})
df.head(15)
df.reset_index(inplace=True)
df.head(15)

#Step-2 Concept, city, and season information, which are available separately in the data set, can be combined.
# Since the price average of all possibilities related to these variables is calculated, 
# each possibility is now turned into a record and the variables are expressed in a single column.

df['sales_level_based'] = df[["concept_type", "city_name", "season_number"]].agg(lambda x: '_'.join(x), axis=1)
df.head(15)

#Step-3 The data set is divided into segments according to the average price information.

df["segment"] = pd.qcut(df["price"], 4, ["D", "C", "B", "A"])
df.head(15)
df.groupby("segment").agg({"price": ["mean", "max", "sum"]})

#Step-4 The dataset is simplified so that only the necessary information remains.

df = df[["sales_level_based", "segment", "price"]]
df.head(15)

# Step-5 Revenue estimation is made for any new customer. While making this prediction, 
# the information of the new customer is taken and written in the appropriate format that can be matched in the data set.
# Since all possibilities are recorded one by one in the data set, there is no mismatch.
# The expected average gain is drawn from the data set based on when the new record matches

# new_customer1 : conccept_type: C, city_name: A, season_number:2
# The expected earnings of a customer planning a holiday in concept C, city A and season 2 are calculated as follows:

new_customer1="concept_C_city_A_S_2"
df[df["sales_level_based"]=="concept_C_city_A_S_2"]

# new_customer1 : conccept_type: B, city_name: C, season_number: 1
# The expected earnings of a customer planning a holiday in concept B, city C and season 1 are calculated as follows:

new_customer2="concept_B_city_C_S_1"
df[df["sales_level_based"]=="concept_B_city_C_S_1"]
