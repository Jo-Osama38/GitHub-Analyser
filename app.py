from flask import Flask ,render_template ,request
import requests 


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
                name_repo = data_repos[num]["name"]
                description = data_repos[num]['description']
                Top_language= data_repos[num]['language']
                forks= data_repos[num]['forks']
                names_repos.append({ "name" :f"{i+1}. {name_repo}","description":f"Description : {description}"
                                    ,"Top_language":f"Top_language:{Top_language}","forks":f"Forks : {forks}"})
                num += 1




        elif respose.status_code == 404:
            message = "The User Name Not Found"
        
    return render_template('index.html', name = name ,repos = repos , url_img = url_img
                           ,message = message , bio = bio , followers =followers ,following=following
                           ,names_repos = names_repos )



if __name__ == "__main__":
    app.run(debug=True)