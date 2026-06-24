from flask import Flask ,render_template ,request
import requests 
from collections import Counter
from analyzer import total_score
from ai_analyzer import ai_analyzer



app = Flask(__name__)


@app.route("/" , methods = ["POST","GET"])
@app.route("/home", methods = ["POST","GET"])
def home ():
    username = None
    name =  None
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
            num = 0
            
            for i in range(min(5,len(data_repos))):
                name_repo = data_repos[i]["name"]
                description = data_repos[i]['description']
                Top_language= data_repos[i]['language']
                forks= data_repos[i]['forks']
                stars = data_repos[i]["stargazers_count"]
                names_repos.append({ "name" :f"{i+1}. {name_repo}","description":f"Description : {description}"
                                    ,"Top_language":f"Top_language:{Top_language}","forks":f"Forks : {forks}","stars":f"Stars : {stars}"})

            for _ in data_repos:
                Top_language_all= data_repos[num]['language']
                most_lang_list.append(Top_language_all)
                total_stars += data_repos[num]["stargazers_count"]
                num += 1
            if len(data_repos) > 0 :
                most_lang = Counter(most_lang_list).most_common()[0][0]

            score = total_score(repos,followers,total_stars)
            

        elif respose.status_code == 404:  
            message = "The User Name Not Found"



        profile = {
            "repos": repos,
            "followers": followers,
            "stars": stars,
            "top_language": most_lang,
            "score": score
        }
        aiAnalyzer = ai_analyzer(profile)
          

        


    return render_template('index.html', name = name ,repos = repos , url_img = url_img
                           ,message = message , bio = bio , followers =followers ,following=following
                           ,names_repos = names_repos ,most_lang = most_lang,total_stars = total_stars,score = score,
                           aiAnalyzer = aiAnalyzer)



if __name__ == "__main__":
    app.run(debug=True)