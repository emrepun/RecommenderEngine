import numpy as np
import pandas as pd
from nltk.corpus import stopwords

df = pd.read_csv('city_data.csv')

def clear(city):
    #1
    city = city.lower()
    #2
    city = city.split()
    #3
    city_keywords = [word for word in city if word not in stopwords.words('english')]

    merged_city = " ".join(city_keywords)
    return merged_city
