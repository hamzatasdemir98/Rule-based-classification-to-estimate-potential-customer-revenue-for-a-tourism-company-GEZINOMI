import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = pd.read_excel("datasets/miuul_gezinomi - Kopya.xlsx")
df.head()
df.info()
#Step-1 Calculate avarage price for each "concept_type", "city_name", and "season_number" combinations
df = df.groupby(["concept_type", "city_name", "season_number"]).agg({"price": "mean"})
df.head(15)
df.reset_index(inplace=True)
df.head(15)

#Step-2 Combine all variables in one variable
df['sales_level_based'] = df[["concept_type", "city_name", "season_number"]].agg(lambda x: '_'.join(x), axis=1)
df.head(15)
#Step-3 Create segments for revenues
df["segment"] = pd.qcut(df["price"], 4, ["D", "C", "B", "A"])
df.head(15)
df.groupby("segment").agg({"price": ["mean", "max", "sum"]})
#Step-4 Summarize dataset by keeping needed variables
df = df[["sales_level_based", "segment", "price"]]
df.head(15)
#Step-5 Forecast customer revenue for random customers
# new_customer1 : conccept_type: C, city_name: A, season_number:2
new_customer1="concept_C_city_A_S_2"
df[df["sales_level_based"]=="concept_C_city_A_S_2"]
# new_customer1 : conccept_type: B, city_name: C, season_number: 1
new_customer2="concept_B_city_C_S_1"
df[df["sales_level_based"]=="concept_B_city_C_S_1"]
