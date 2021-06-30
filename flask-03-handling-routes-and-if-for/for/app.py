from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def head():
    first="This is my first condition experience"
    return render_template("index.html", message = False )

@app.route('/serdar')
def header():
    name = ["serdar", "fatih", "Ali"]
    return render_template("body.html", object = name)





if __name__=="__main__":
    app.run(debug=True)
