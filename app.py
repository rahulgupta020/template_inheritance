from flask import Flask, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def mainPage():
    return "This is Main Page. You can go in home and about page"

@app.route('/home', methods=['GET'])
def homePage():
    return render_template("home.html")

@app.route('/about', methods=['GET'])
def aboutPage():
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)