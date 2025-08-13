from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", title="Home")

@app.route('/surveys')
def survey_selection():
    return render_template("survey_selection.html", title="Take Survey")

@app.route('/about')
def about():
    return render_template("about.html", title="About Us")



if __name__ == '__main__':
    app.run(debug=True)