import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Görev 1: Aşağıdaki Soruları Yanıtlayınız.

# Soru 1: persona.csv dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz.

df = pd.read_csv("persona.csv")
df.head()
df.info()
df.shape
df.columns
df.describe().T

# Soru 2: Kaç unique SOURCE vardır? Frekansları nedir?

df["SOURCE"].nunique()
df["SOURCE"].value_counts()

# Soru 3: Kaç unique PRICE vardır?

df["PRICE"].nunique()

# Soru 4: Hangi PRICE'dan kaçar tane satış gerçekleşmiş?

df["PRICE"].value_counts()

# Soru 5: Hangi ülkeden kaçar tane satış olmuş?

df["COUNTRY"].value_counts()

# Soru 6: Ülkelere göre satışlardan toplam ne kadar kazanılmış?

df.groupby("COUNTRY")["PRICE"].sum()

# Soru 7: SOURCE türlerine göre satış sayıları nedir?

df["SOURCE"].value_counts()

# Soru 8: Ülkelere göre PRICE ortalamaları nedir?

df.groupby("COUNTRY")["PRICE"].mean()

# Soru 9: SOURCE'lara göre PRICE ortalamaları nedir?

df.groupby("SOURCE")["PRICE"].mean()


# Soru 10: COUNTRY-SOURCE kırılımında PRICE ortalamaları nedir?

df.groupby(["COUNTRY","SOURCE"])["PRICE"].mean() #ya da
df.groupby(["COUNTRY", "SOURCE"]).agg({"PRICE":"mean"})

#Görev 2: COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar nedir?

df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE":"mean"})

#Görev 3: Çıktıyı PRICE’a göre sıralayınız.

#Önceki sorudaki çıktıyı daha iyi görebilmek için sort_values metodunu azalan olacak şekilde PRICE’a göre
#uygulayınız.Çıktıyı agg_df olarak kaydediniz.

df.groupby(["COUNTRY","SOURCE","SEX","AGE"]).agg({"PRICE":"mean"}).sort_values("PRICE",ascending=False)

agg_df = df.groupby(["COUNTRY","SOURCE","SEX","AGE"]).agg({"PRICE":"mean"}).sort_values("PRICE",ascending=False)

#Görev 4: Indekste yer alan isimleri değişken ismine çeviriniz.
#Üçüncü sorunun çıktısında yer alan PRICE dışındaki tüm değişkenler index isimleridir.
# Bu isimleri değişken isimlerine çeviriniz.

agg_df = agg_df.reset_index()
agg_df

#Görev 5: Age değişkenini kategorik değişkene çeviriniz ve agg_df’e ekleyiniz.
# Age sayısal değişkenini kategorik değişkene çeviriniz.
# Aralıkları ikna edici şekilde oluşturunuz.
# Örneğin: ‘0_18', ‘19_23', '24_30', '31_40', '41_70'

agg_df["AGE"].dtype

agg_df["AGE_CAT"] = pd.cut(agg_df["AGE"],[0, 18, 23, 30, 40, 70], labels=["0_18","19_23","24_30","31_40","41_70"])
agg_df["AGE_CAT"]
agg_df

#Görev 6: Yeni seviye tabanlı müşterileri (persona) tanımlayınız.
#Yeni seviye tabanlı müşterileri (persona) tanımlayınız ve veri setine değişken olarak ekleyiniz.
#Yeni eklenecek değişkenin adı: customers_level_based
#Önceki soruda elde edeceğiniz çıktıdaki gözlemleri bir araya getirerek customers_level_based değişkenini
# oluşturmanız gerekmektedir.
#Dikkat! List comprehension ile customers_level_based değerleri oluşturulduktan sonra bu
# değerlerin tekilleştirilmesi gerekmektedir.
#Örneğin birden fazla şu ifadeden olabilir: USA_ANDROID_MALE_0_18.
# Bunları groupby'a alıp price ortalamalarını almak gerekmektedir.

customer_level_based = [f"{col['COUNTRY'].upper()}_{col['SOURCE'].upper()}_{col['SEX'].upper()}_{col['AGE_CAT'].upper()}" for index, col in agg_df.iterrows()]
agg_df["customer_level_based"] = customer_level_based
agg_df

agg_df = agg_df.groupby(["customers_level_based"]).agg({"PRICE": "mean"})
agg_df = agg_df.reset_index()
agg_df

#Görev 7: Yeni müşterileri (personaları) segmentlere ayırınız.
#Yeni müşterileri (Örnek: USA_ANDROID_MALE_0_18) PRICE’a göre 4 segmente ayırınız.
#Segmentleri SEGMENT isimlendirmesi ile değişken olarak agg_df’e ekleyiniz.
#Segmentleri betimleyiniz (Segmentlere göre group by yapıp price mean, max, sum’larını alınız).

agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"], 4, labels = ["D", "C", "B", "A"])

agg_df.groupby("SEGMENT").agg({"PRICE":["mean", "max", "sum"]})

#Görev 8: Yeni gelen müşterileri sınıflandırıp, ne kadar gelir getirebileceklerini tahmin ediniz.

new_user = 'TUR_ANDROID_FEMALE_31_40'
agg_df[agg_df["customers_level_based"] == new_user]

def gelir_tahmini(new_user):
    return agg_df[agg_df["customers_level_based"] == new_user]

#33 yaşında ANDROID kullanan bir Türk kadını hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir?

new_user1 = 'TUR_ANDROID_FEMALE_31_40'
gelir_tahmini(new_user1)

#35 yaşında IOS kullanan bir Fransız kadını hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir?

new_user2 ='FRA_IOS_FEMALE_31_40'
gelir_tahmini(new_user2)




