
from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module; Flask wants
# to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def landing_page():
    return render_template("index.html")

# route to display a simple web page
@app.route('/anne_sexton')
def anne_sexton_tiles():
    return render_template("anne_sexton.html")

@app.route('/audre_lorde')
def audre_lorde_tiles():
    return render_template("audre_lorde.html")

@app.route('/adrienne_rich')
def adrienne_rich_tiles():
    return render_template("adrienne_rich.html")

@app.route('/pablo_neruda')
def pablo_neruda_tiles():
    return render_template("pablo_neruda.html")

@app.route('/langston_hughes')
def langston_hughes_tiles():
    return render_template("langston_hughes.html")

@app.route('/poet')
def show_poet():
    poet = request.args.get('poet')
    print poet
    # turn the number in to a name
    # call your functions to get the words
    # send words to magnetic poetry template
    return render_template("tiles.html", poet=poet)
    # return render_template("tiles.html" poet=poet_name, words=words_list)




if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)

