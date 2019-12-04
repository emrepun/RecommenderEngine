import numpy as np
import pandas as pd
from cosine_similarity import CosineSimilarity
from rating_extractor import RatingExtractor
import operator
import json

class RecommenderEngine:
    def __init__(self):
        print("engine initialized")

    def calculate_final_score(cs, r):
        amount = (cs / 100) * r

        return cs + amount

    # Version-3
    def get_recommendations_include_rating_count_threshold(keywords):
        df = pd.read_csv('city_data_cleared.csv')

        score_dict = {}

        for index, row in df.iterrows():
            cs_score = CosineSimilarity.cosine_similarity_of(row['description'], keywords)

            rating = row['rating']
            rating_count = row['rating_count']
            threshold = 1000000
            rating_contribution = RatingExtractor.get_rating_weight_with_quantity(rating,rating_count,threshold,100)

            final_score = RecommenderEngine.calculate_final_score(cs_score, rating_contribution)

            score_dict[index] = final_score

        #sort cities by score and index.
        sorted_scores = sorted(score_dict.items(), key=operator.itemgetter(1), reverse=True)

        counter = 0

        #create an empty results data frame.
        resultDF = pd.DataFrame(columns=('city', 'popularity', 'description', 'score'))

        #get highest scored 5 cities.
        for i in sorted_scores:
            #print index and score of the city.
            #print(i[0], i[1])
            resultDF = resultDF.append({'city': df.iloc[i[0]]['city'], 'popularity': df.iloc[i[0]]['popularity'], 'description': df.iloc[i[0]]['description'], 'score': i[1]}, ignore_index=True)
            counter += 1

            if counter>4:
                break

        #convert DF to json.
        json_result = json.dumps(resultDF.to_dict('records'))
        return json_result


    # Version-2
    def get_recommendations_include_rating(keywords):
        df = pd.read_csv('city_data_cleared.csv')

        score_dict = {}

        for index, row in df.iterrows():
            cs_score = CosineSimilarity.cosine_similarity_of(row['description'], keywords)

            rating = row['rating']
            rating_contribution = RatingExtractor.get_rating_weight(rating,10)

            final_score = RecommenderEngine.calculate_final_score(cs_score, rating_contribution)

            score_dict[index] = final_score

        #sort cities by score and index.
        sorted_scores = sorted(score_dict.items(), key=operator.itemgetter(1), reverse=True)

        counter = 0

        #create an empty results data frame.
        resultDF = pd.DataFrame(columns=('city', 'popularity', 'description', 'score'))

        #get highest scored 5 cities.
        for i in sorted_scores:
            #print index and score of the city.
            #print(i[0], i[1])
            resultDF = resultDF.append({'city': df.iloc[i[0]]['city'], 'popularity': df.iloc[i[0]]['popularity'], 'description': df.iloc[i[0]]['description'], 'score': i[1]}, ignore_index=True)
            counter += 1

            if counter>4:
                break

        #convert DF to json.
        json_result = json.dumps(resultDF.to_dict('records'))
        return json_result

    #Version-1
    def get_recommendations(keywords):

        df = pd.read_csv('city_data_cleared.csv')

        score_dict = {}

        for index, row in df.iterrows():
            score_dict[index] = CosineSimilarity.cosine_similarity_of(row['description'], keywords)

        #sort cities by score and index.
        sorted_scores = sorted(score_dict.items(), key=operator.itemgetter(1), reverse=True)

        counter = 0

        #create an empty results data frame.
        resultDF = pd.DataFrame(columns=('city', 'popularity', 'description', 'score'))

        #get highest scored 5 cities.
        for i in sorted_scores:
            #print index and score of the city.
            #print(i[0], i[1])
            resultDF = resultDF.append({'city': df.iloc[i[0]]['city'], 'popularity': df.iloc[i[0]]['popularity'], 'description': df.iloc[i[0]]['description'], 'score': i[1]}, ignore_index=True)
            counter += 1

            if counter>4:
                break

        #convert DF to json.
        json_result = json.dumps(resultDF.to_dict('records'))
        return json_result
