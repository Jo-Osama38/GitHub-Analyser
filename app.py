from flask import Flask ,render_template ,request
import requests 
from collections import Counter
from analyzer import total_score ,calc_time ,first_project ,Latest_project
import time
# from ai_analyzer import ai_analyzer


app = Flask(__name__)



@app.route("/" )
@app.route("/home")
def home ():
    torvalds_img = "https://avatars.githubusercontent.com/u/1024025?v=4"
    facebook_img = "https://avatars.githubusercontent.com/u/69631?v=4"
    google_img = "https://avatars.githubusercontent.com/u/1342004?v=4"
    microsoft_img = "https://avatars.githubusercontent.com/u/6154722?v=4"
    return render_template("index.html" ,torvalds_img = torvalds_img , facebook_img = facebook_img, google_img=google_img , microsoft_img = microsoft_img)

@app.route("/analyze", methods=["POST"])
def analyzer():
    username = None
    name =  None
    real_name =  None
    repos = None
    message = None
    url_img = None
    bio = None
    followers = None
    following = None
    name_repo = None
    names_repos = []
    most_lang_list = []
    most_lang = None
    total_stars = 0
    score = None
    aiAnalyzer =None
    total_forks = 0
    stars = 0
    documentation_score = 0
    num_repos_description = 0
    name_first_project = None
    name_Last_project = None


    if request.method == "POST":
        username = request.form.get("username")
        url = f"https://api.github.com/users/{username}"
        url_repos = f"https://api.github.com/users/{username}/repos" 
        respose= requests.get(url)
        data = respose.json()
        if respose.status_code == 200:
            repositories= requests.get(url_repos)
            data_repos = repositories.json()
            url_img =data ["avatar_url"]
            name = data["login"]
            repos = data["public_repos"]
            bio = data["bio"]
            followers = data["followers"]
            following = data["following"]
            real_name = data["name"]
            num = 0
            
            for i in range(min(5,len(data_repos))):
                name_repo = data_repos[i]["name"]
                description = data_repos[i]['description']
                Top_language= data_repos[i]['language']
                forks = data_repos[i]['forks']
                stars = data_repos[i]["stargazers_count"]
                last_update = data_repos[i]["updated_at"]
                names_repos.append({ "name" :f"{i+1}. {name_repo}",
                                    "description":f"Description : {description}"
                                    ,"Top_language":f"Top_language:{Top_language}",
                                    "forks":f"Forks : {forks}",
                                    "stars":f"Stars : {stars}",
                                    "lastupdate":f"Last Update : {calc_time(last_update)}"
                                    })

            for _ in data_repos:
                description = data_repos[num]["description"]
                if description:
                    num_repos_description += 1
                Top_language_all= data_repos[num]['language']
                fork = data_repos[num]["forks_count"]
                total_forks  += fork
                most_lang_list.append(Top_language_all)
                total_stars += data_repos[num]["stargazers_count"]

                num += 1
            if len(data_repos) > 0 :
                most_lang = Counter(most_lang_list).most_common()[0][0]


            score = total_score(repos,followers,total_stars)
            if repos:
                documentation_score = (num_repos_description/repos) * 100 

        elif respose.status_code == 404:  
            message = "The User Name Not Found"




        if repos:
            name_first_project = first_project(data_repos)
            name_Last_project  = Latest_project(data_repos)

        profile = {
            "repos": repos,
            "followers": followers,
            "total_stars": stars,
            "top_language": most_lang,
            "score": score,
            "total_forks": total_forks,
            "documentation_score" : documentation_score

        }
        # aiAnalyzer = ai_analyzer(profile)
          

        


    return render_template('analyze.html', real_name= real_name,name = name ,repos = repos , url_img = url_img
                           ,message = message , bio = bio , followers =followers ,following=following
                           ,names_repos = names_repos ,most_lang = most_lang,total_stars = total_stars,score = score,
                           aiAnalyzer = aiAnalyzer,total_forks = total_forks ,lastproject = name_Last_project,firstproject= name_first_project)



if __name__ == "__main__":
    app.run(debug=True)