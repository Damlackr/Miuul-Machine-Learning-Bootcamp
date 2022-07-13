# Görev1: cat_summary() fonksiyonuna 1 özellik ekleyiniz. Bu özellik argümanla biçimlendirilebilir olsun. Var olan
# özelliği de argümanla kontrol edilebilir hale getirebilirsiniz.

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()


def cat_summary(dataframe, col_name, tail=5):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################")
    print(dataframe.tail(tail))


cat_summary(df, "sex")


# Görev2: check_df(), cat_summary() fonksiyonlarına 4 bilgi (uygunsa) barındıran numpy tarzı docstring
# yazınız. (task, params, return, example)


def check_df(dataframe, head=5):
    """
   Task
   ----------

   Veri setindeki değişkenlerin shape, types, head, tail, Na ve quatiles gibi özellikleri yani
    genel bilgisi hakında bilgi verir.

   Parameters
   ----------
    dataframe: dataframe
       değişken isimleri alınmak istenen dataframe'dir.
   head: int
       değişkenleri ekrana gösterirken head ya da tail gibi fonksiyonların limitini gösterir.

   Returns
   ----------
   Shape
       dataframe.shape
       dataframe'e ait satır ve sütun bilgileri.
   Types
       dataframe.dtypes
       dataframe'e ait sütun tip bilgileri.
   Head
       dataframe.head(head)
       dataframe'in ilk verilen limit satırı.
   Tail
       dataframe.tail(head)
       dataframe'in son verilen limit satırı.
   Na
       dataframe.isnull().sum()
       dataframe'e ait sütunlardaki boş değer sayısı.
   Quantiles
       dataframe.describe([0, 0.05, 0.5, 0.95, 0.99, 1]).T
       dataframe'e ait numerik değerlerin %0, %5, %50, %95, %99 ve %100. değerlerini.

   Examples
   ----------

   dataframe_özellikleri = check_df(dataframe)

   """
    print("##################### Shape #####################")
    print(dataframe.shape)
    print("##################### Types #####################")
    print(dataframe.dtypes)
    print("##################### Head #####################")
    print(dataframe.head(head))
    print("##################### Tail #####################")
    print(dataframe.tail(head))
    print("##################### NA #####################")
    print(dataframe.isnull().sum())
    print("##################### Quantiles #####################")
    print(dataframe.describe([0, 0.05, 0.50, 0.95, 0.99, 1]).T)


check_df(df)


#################################################################################################


def cat_summary(dataframe, col_name, plot=False):
    """
   Task
   ----------
   Verilen veri setindeki kategorik değişkenlerin oranlarını veren fonksiyon.
   Parameters
   ----------
   dataframe : dataframe
       değişken isimleri alınmak istenen dataframe'dir.

   col_name :  str, int
       analiz edilmek istenen sütunu adı ya da indeksi.

   plot : bool
       grafik olarak çıktı alınsın mı alınmasın mı, diye döner.

   Returns
   ---------

   Examples
   ----------
   cat_summary(df, "sex", plot = True)

   """
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################")
    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show()


cat_summary(df, "sex", plot=True)