from flask import Flask

app = Flask(__name__)

@app.route('/')
def head():
    return "I like Flask"

@app.route('/second')
def second():
    return "This is the second page"

@app.route('/third/subthird')
def third():
    return "this is the subpage of the third page"

@app.route('/forth/<string:id>')
def forth(id):
    return f'Id of this page is {id}'
if __name__ =="__main__":
    app.run(debug=True) #This is the mandatory part of Flask

