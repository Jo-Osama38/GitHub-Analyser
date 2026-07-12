from flask import Flask ,render_template ,request
import requests 
from collections import Counter
from analyzer import total_score ,calc_time ,first_project ,Latest_project,created_since ,top_lang,activiy,calc_score_repos,calc_score_forks,calc_score_stars,calc_score_doc,calc_score_activy,calc_score_lang,calc_score_profils
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor
from ai_analyzer import ai_analyzer

import os

app = Flask(__name__)

load_dotenv()
TOKEN = os.getenv("token")
headers = {
    "Authorization": f"Bearer {TOKEN}"
}

def get_languages(repo):
            url = repo["languages_url"]
            response = requests.get(url,headers=headers)

            return response.json()


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
    total_stars = 0
    score = None
    aiAnalyzer =None
    total_forks = 0
    stars = 0
    documentation_score = 0
    num_repos_description = 0
    name_first_project = None
    name_Last_project = None
    create_at = None
    number = 0 
    top_language= None
    languages_counter = Counter()
    language_bytes = {}
    language_data= None
    update_profile= None
    num_lang = 0
    score_repos = 0
    score_stars = 0
    score_forks = 0
    score_documentation = 0
    score_activity = 0
    score_lang = 0
    score_profile =0
    developer_score =0
    last_activity_days = 0
    company =None
    location = None
    blog = None
    years_created_github = 0
    avg_stars =0
    avg_forks =0

    if request.method == "POST":
        username = request.form.get("username")
        url = f"https://api.github.com/users/{username}"
        url_repos = f"https://api.github.com/users/{username}/repos" 
        respose= requests.get(url)
        data = respose.json()
        if respose.status_code == 200:
            repositories= requests.get(url_repos,headers=headers)
            data_repos = repositories.json()
            url_img =data ["avatar_url"]
            name = data["login"]
            repos = data["public_repos"]
            bio = data["bio"]
            followers = data["followers"]
            following = data["following"]
            real_name = data["name"]
            create_at =data ["created_at"] 
            update_profile = data["updated_at"]
            num = 0
            company = data["company"]
            blog = data["blog"]
            location = data["location"]
            
            for i in range(min(4,len(data_repos))):
                name_repo = data_repos[i]["name"]
                description = data_repos[i]['description']
                language = data_repos[i]["language"]
                forks = data_repos[i]['forks']
                stars = data_repos[i]["stargazers_count"]
                last_update = data_repos[i]["updated_at"]
                 
                names_repos.append({ "name" :name_repo,
                                    "description":description,
                                    "forks":forks,
                                    "stars":stars,
                                    "Top_language":language,
                                    "lastupdate":f"{calc_time(last_update)}"
                                    })

            for _ in data_repos:
                description = data_repos[num]["description"]
                if description:
                    num_repos_description += 1
                fork = data_repos[num]["forks_count"]
                total_forks  += fork
                total_stars += data_repos[num]["stargazers_count"]

                num += 1
            with ThreadPoolExecutor(max_workers=10) as executor:
                results = list(executor.map(get_languages, data_repos))

            for language_data in results:
                if "message" in language_data:
                    continue

                for lang, bytes_count in language_data.items():
                    if lang not in language_bytes:
                        language_bytes[lang] = 0
                    language_bytes[lang] += bytes_count


            top_language = top_lang(language_bytes)
            last_activity_days = activiy(update_profile)
            num_lang = len(language_bytes)
            total_lang_score = sum(language_bytes.values())
            
            lang_prsents_sort = dict(sorted(language_bytes.items(), key=lambda item: item[1], reverse=True))
            lang_prsents ={}
            for lang,bytess in lang_prsents_sort.items():
                prsent = (bytess/ total_lang_score)*100
                lang_prsents[lang] = round(prsent,2)

            top_6_languages = list(lang_prsents.items())[:6]
               
           
            if repos:
                documentation_score = (num_repos_description/repos) * 100 



        elif respose.status_code == 404:  
            message = "The User Name Not Found"


        if repos:
            name_first_project = first_project(data_repos)
            name_Last_project  = Latest_project(data_repos)
            years_created_github = created_since(create_at)

        profile = {
                "username": name,
                "real_name": real_name,
                "bio": bio,
                "repositories": repos,
                "followers": followers,
                "following": following,
                "years_on_github": years_created_github,
                "last_activity_days": last_activity_days,
                "total_stars": total_stars,
                "total_forks": total_forks,
                "average_stars": round(avg_stars, 2),
                "average_forks": round(avg_forks, 2),
                "top_language": top_language,
                "languages": language_bytes,
                "documentation_score": round(documentation_score, 1),
                "first_project": name_first_project,
                "latest_project": name_Last_project,
                "developer_score": developer_score,
                "languages":language_bytes,
            }
        aiAnalyzer = ai_analyzer(profile)
        if repos and repos > 0 :
            avg_stars = total_stars / repos
            avg_forks = total_forks/repos
        else:
            avg_forks = 0
            avg_stars = 0 

        avg_stars = round(avg_stars,1)
      
   


        score_repos = calc_score_repos(repos)
        score_stars = calc_score_stars(avg_stars)
        score_forks = calc_score_forks(avg_forks)
        documentation = calc_score_doc(documentation_score)
        score_documentation = round(documentation, 1)
        score_activity = calc_score_activy(last_activity_days)
        score_lang = calc_score_lang(num_lang)
        score_profile =calc_score_profils(real_name,bio,company,location,blog)

        developer_score = score_repos+ score_stars+score_forks +score_documentation+score_activity+score_lang+score_profile


    return render_template('analyze.html', real_name= real_name,name = name ,repos = repos , url_img = url_img
                           ,message = message , bio = bio , followers =followers ,following=following
                           ,names_repos = names_repos ,total_stars = total_stars,score = score,
                           aiAnalyzer = aiAnalyzer,total_forks = total_forks ,lastproject = name_Last_project,firstproject= name_first_project,
                           years_created_github =years_created_github,avg_stars=avg_stars , top_language = top_language,language_bytes=language_bytes,
                           documentation_score=documentation_score,score_activity = score_activity ,
                           score_repos=score_repos,score_stars=score_stars,score_forks=score_forks,
                           score_documentation=score_documentation,score_lang=score_lang,score_profile=score_profile
                           ,developer_score = developer_score,lang_prsents = top_6_languages,company=company,blog =blog,location=location)



if __name__ == "__main__":
    app.run(debug=True)