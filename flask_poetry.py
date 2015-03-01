
from flask import Flask, render_template

# "__name__" is a special Python variable for the name of the current module; Flask wants
# to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return render_template("index.html")

# route to display a simple web page
@app.route('/pick_a_poet')
def pick_a_poet():
    return render_template("pick_a_poet.html")

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)

