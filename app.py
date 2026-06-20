from flask import Flask ,render_template ,request
import requests 


app = Flask(__name__)


@app.route("/" , methods = ["POST","GET"])
@app.route("/home", methods = ["POST","GET"])
def home ():
    username = None
    data = None
    name =  None
    repos = None
    message = None

    if request.method == "POST":
        username = request.form.get("username")
        url = f"https://api.github.com/users/{username}"
        respose= requests.get(url)
        data = respose.json()
        if requests.status_codes == 200:
            name = data["login"]
            repos = data["public_repos"]
        elif requests.status_codes == 404:
            message = "The User Name Not Found"
        
    return render_template('index.html' ,username = username ,data = data , name = name ,repos = repos 
                           ,message = message)



if __name__ == "__main__":
    app.run(debug=True)