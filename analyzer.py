

def total_score (nums,num_followers,num_forks):
    
            score = 20
            if nums <= 60:score += nums / 2 
            else :score += 30

            if num_followers <= 250: score += num_followers/10
            else : score += 25

            if num_forks <= 125: score += num_forks/5
            else : score += 25

            return score


from datetime import datetime, timezone
def calc_time(time):

            post_time = datetime.strptime(time, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
            today_date = datetime.now(timezone.utc).date()

            post_date = post_time.date()

            if post_date == today_date:
                last_update = "Last Update : Today "
            elif (today_date - post_date).days == 1:
                last_update = "Last Update : yesterday "
            else:
                days_ago = (today_date - post_date).days
                if days_ago < 30:
                      last_update = f"Last Update : {days_ago} days ago "
                elif 365.25 > days_ago > 30 :
                      last_update = f"Last Update : {days_ago/30} month ago "
                else:
                    last_update = f"Last Update : {days_ago/365.25} years ago "


            return last_update


def first_project(datanums):
        num = 1
        name_project = datanums[0]["name"]
        time_create_project = datanums[0]["created_at"]
        for _ in datanums :
            if time_create_project > datanums[num]["created_at"]:
                name_project = datanums[num]["name"]
                time_create_project = datanums[num]["created_at"]
                num += 1

        return name_project

def Latest_project(datanums):
        num = 1 
        name_project = datanums[0]["name"]
        time_create_project = datanums[0]["created_at"]
        for _ in datanums :
            if time_create_project < datanums[num]["created_at"]:
                name_project = datanums[num]["name"]
                time_create_project = datanums[num]["created_at"]
                num += 1

        return name_project


def created_since(create_at):

    created = datetime.strptime(create_at,"%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    now = datetime.now(timezone.utc)
    years = now.year - created.year

    if (now.month, now.day) < (created.month, created.day):
        years -= 1
    return years

def top_lang(listoflang):
        if not listoflang:
               return "umknow"


        top_language = max(listoflang, key=listoflang.get)
        return top_language

def activiy(time):
        post_time = datetime.strptime(time, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
        today_date = datetime.now(timezone.utc).date()
        post_date = post_time.date()
        days =  (today_date - post_date).days 
        return days  

def calc_score_repos(repos):
    if repos :
            if repos > 15:
                  repos_score = 5
            elif 15 < repos <30:
                  repos_score = 10
            elif 30 < repos < 50:
                  repos_score = 15
            elif 50 < repos:
                  repos_score = 20 
    else :
            repos_score = 0
    
    return repos_score


def calc_score_stars(avg):
    if avg:
            if avg > 50:
                stars_score = 5
            elif 50 < avg < 100 :
                  stars_score = 7
            elif 100 < avg < 150 :
                  stars_score = 10
            elif 150 < avg < 200 :
                  stars_score = 13
            elif  avg > 200 :
                  stars_score = 15
    else:
          stars_score = 0
    return stars_score

def calc_score_forks(avg):
    if avg:
            if avg > 50:
                forks_score = 5
            elif 50 < avg < 100 :
                  forks_score = 7
            elif 100 < avg < 150 :
                  forks_score = 10
            elif 150 < avg < 200 :
                  forks_score = 13
            elif  avg > 200 :
                  forks_score = 15
    else:
          forks_score = 0
    return forks_score

def calc_score_doc(persent):
    if persent:
            doc_score = persent / 10
    else:
          doc_score = 0
    return doc_score

def calc_score_activy(days):
    if days < 3:
            score_activity = 10 
    elif 3< days <  10:
          score_activity = 9
    elif 10< days <  20:
          score_activity = 8
    elif 20< days <  40:
          score_activity = 7
    elif 40< days <  50:
          score_activity = 6
    elif 50< days <  70:
          score_activity = 5
    elif 70< days <  100:
          score_activity = 4
    elif 100< days <  150:
          score_activity = 3
    elif 150< days <  200:
          score_activity = 2
    elif 200< days <  365:
          score_activity = 1
    else:
        score_activity =0

    return score_activity

def calc_score_profils(name,bio,company,location,blog):
        if name :
            score_profile += 1
        if bio :
            score_profile += 1
        if company :
            score_profile += 1
        if location :
            score_profile += 1
        if blog :
            score_profile += 1
        return score_profile

def calc_score_lang(num_lang):
      if num_lang:
            if num_lang <= 10:
                score_lang = num_lang
            else:
                  score_lang = 10
      else:
            score_lang = 0
      return score_lang



       
