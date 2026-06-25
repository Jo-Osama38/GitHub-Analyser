

def total_score (nums,num_followers,num_stars):
    
            score = 20
            if nums <= 60:score += nums / 2 
            else :score += 30

            if num_followers <= 250: score += num_followers/10
            else : score += 25

            if num_stars <= 125: score += num_stars/5
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
                last_update = f"Last Update : {days_ago} days ago "

            return last_update

global num 
num = 1
def first_project(datanums):
       
        name_project = datanums[0]["name"]
        time_create_project = datanums[0]["created_at"]
        for _ in datanums :
            if time_create_project > datanums[num]["created_at"]:
                name_project = datanums[num]["name"]
                time_create_project = datanums[num]["created_at"]
                num += 1

        return name_project

def Latest_project(datanums):
       
        name_project = datanums[0]["name"]
        time_create_project = datanums[0]["created_at"]
        for _ in datanums :
            if time_create_project < datanums[num]["created_at"]:
                name_project = datanums[num]["name"]
                time_create_project = datanums[num]["created_at"]
                num += 1

        return name_project

            
       
