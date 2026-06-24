

def total_score (repos,num_followers,num_stars):
    
            score = 20
            if repos <= 60:score += repos / 2 
            else :score += 30

            if num_followers <= 250: score += num_followers/10
            else : score += 25

            if num_stars <= 125: score += num_stars/5
            else : score += 25

            return score

