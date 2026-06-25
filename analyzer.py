

def total_score (repos,num_followers,num_stars):
    
            score = 20
            if repos <= 60:score += repos / 2 
            else :score += 30

            if num_followers <= 250: score += num_followers/10
            else : score += 25

            if num_stars <= 125: score += num_stars/5
            else : score += 25

            return score


from datetime import datetime, timezone
def calc_time(time):


            time = "2026-06-25T00:42:31Z"

            post_time = datetime.strptime(time, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
            today_date = datetime.now(timezone.utc).date()

            post_date = post_time.date()

            if post_date == today_date:
                last_update = "Last Update : Today "
            elif (today_date - post_date).days == 1:
                last_update = "Last Update : yesterday "
            else:
                days_ago = (today_date - post_date).days
                last_update = f"Last Update : {days_ago} days ago "

            return last_update