from recommender_engine import RecommenderEngine
import json

culture_keywords = "history historical art architecture city culture"
beach_n_sun_keywords = "beach beaches park nature holiday sea seaside sand sunshine sun sunny"
nightlife_keywords = "nightclub nightclubs nightlife bar bars pub pubs party beer"

def get_recommendations(keywords):
    result = RecommenderEngine.get_recommendations(keywords)
    return result

def get_top_5_city_names_out_of_json(json_string):
    list = json.loads(json_string)
    result = []
    max = len(list)
    i = 0
    while i < max:
        result.append((list[i]['city'], list[i]['score']))
        i += 1

    return result

top_5_cultural_cities = get_recommendations(culture_keywords)
city_names_for_cultural = get_top_5_city_names_out_of_json(top_5_cultural_cities)
print(city_names_for_cultural)
print("#################")
top_5_summer_cities = get_recommendations(beach_n_sun_keywords)
city_names_for_summer = get_top_5_city_names_out_of_json(top_5_summer_cities)
print(city_names_for_summer)
print("#################")
top_5_party_cities = get_recommendations(nightlife_keywords)
city_names_for_party = get_top_5_city_names_out_of_json(top_5_party_cities)
print(city_names_for_party)
print("#################")
