## Gerekli kütüphanelerin import edilmesi

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

#Veriseti Gezinomi firmasına ait satış verilerini barındırmaktadır. Ancak bu verileri paylaşamayacağım için, 
# çalışmayı aynı mantıkla yapabileceğiniz manüpile edilmiş verisetini paylaştım
# Konsept bilgisi, herşey dahil, yarım pansiyon gibi seçenekler barındırmaktadır.
# City bilgisi hangi şehirde tatil yapılacağı bilgisini barındırır
# Season bilgisi ise yaz ve kış sezonları bilgisini barındırmaktadır.

df = pd.read_excel("datasets/dataset.xlsx")
df.head()
df.info()

#Kural tabanlı sınıflandırma

#Adım-1 Konsept, şehir ve sezon bilgilerinin tüm kombinasyonları için ortalama ücret hesaplanır.

df = df.groupby(["concept_type", "city_name", "season_number"]).agg({"price": "mean"})
df.head(15)
df.reset_index(inplace=True)
df.head(15)

#Adım-2 Verisetinde ayrı ayrı bulunan konsept, şehir ve sezon bilgileri birleştirilebilir durumdadır.
# Bu değişkenlerle ilgili tüm olasılıklarım price ortalaması hesaplandığı için artık her bir olasılık bir
# kayıt haline getirilip değişkenler tek bir kolonda ifade edilir.

df['sales_level_based'] = df[["concept_type", "city_name", "season_number"]].agg(lambda x: '_'.join(x), axis=1)
df.head(15)

#Adım-3 Ortalama ücret bilgisine göre veri seti segmentlere ayrılır. 

df["segment"] = pd.qcut(df["price"], 4, ["D", "C", "B", "A"])
df.head(15)
df.groupby("segment").agg({"price": ["mean", "max", "sum"]})

#Adım-4 Veriseti sadece gerekli bilgiler kalacak şekilde sadeleştirilir.

df = df[["sales_level_based", "segment", "price"]]
df.head(15)

#Adım-5 Yeni gelen herhangibir müşteri için gelir tahmini yapılır. 
# Bu tahmin yapılırken yeni gelen müşterinin bilgileri alınarak veri setinde eşleşebileceği uygun formatta yazılır. 
# Veri setinde tüm olasılıklar teker teker kaydedildiği için eşleşmeme durumu yoktur. Yeni kaydın eşleştiği duruma göre 
# beklenen ortalama kazanç verisetinden çekilir

# new_customer1 : conccept_type: C, city_name: A, season_number:2
# C konsepti, A şehri ve 2. sezonda tatil yapmayı planlayan bir müşterinin beklenen kazancı şöyle hesaplanır:

new_customer1="concept_C_city_A_S_2"
df[df["sales_level_based"]=="concept_C_city_A_S_2"]

# new_customer1 : conccept_type: B, city_name: C, season_number: 1
# B konsepti, C şehri ve 1. sezonda tatil yapmayı planlayan bir müşterinin beklenen kazancı şöyle hesaplanır:

new_customer2="concept_B_city_C_S_1"
df[df["sales_level_based"]=="concept_B_city_C_S_1"]
