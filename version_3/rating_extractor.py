from math import e

class RatingExtractor:
    def __init__(self):
        print("rating initialized")

    #Returns value between -q and q. for rating input between 0 and 10.
    #Parameters:
        #rating: indicates the rating for the destination
        #q: indicates the percentage of rating for general score. (default is 10.)
        #c: rating count
        #T: indicates the amount of rating as a threshold where score will be halved.
    @staticmethod
    def get_rating_weight_with_quantity(rating, c, T, q=10):
        if rating > 10 or rating < 0:
            return None
        else:
            m = (2*q) / 10 #10 because rating varies between 0 and 10
            b = -q
            val = (m*rating) + b

            M = e**((-T*0.68)/c)

            return val * M

    #Returns value between -q and q. for rating input between 0 and 10.
    #Parameters:
        #rating: indicates the rating for the destination
        #q: indicates the percentage of rating for general score. (default is 10.)
    @staticmethod
    def get_rating_weight(rating, q=10):
        if rating > 10 or rating < 0:
            return None
        else:
            m = (2*q) / 10 #10 because rating varies between 0 and 10
            b = -q
            return (m*rating) + b
