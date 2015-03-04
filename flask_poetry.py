
from flask import Flask, render_template, request
import the_hell

# "__name__" is a special Python variable for the name of the current module; Flask wants
# to know this to know what any imported things are relative to.
app = Flask(__name__)

POETS = { 1: {"name":"Anne Sexton", "bio":"This is Anne Sexton's Bio",
        "image":"http://www.ikewrites.com/wp-content/uploads/2012/11/anne_sexton_2.jpg",
        "source":"text_files/anne_sexton.txt"},
        2: {"name": "Audre Lorde", "bio":"This is Audre Lorde's Bio",
        "image":"https://bluemilk.files.wordpress.com/2013/07/audre-lorde-the-berlin-years.jpg",
        "source":"text_files/audre_lorde.txt"},
        3: {"name":"Adrienne Rich", "bio":"This is Adrienne Rich's Bio",
        "image":"http://graphics8.nytimes.com/images/2012/03/29/obituaries/subRICH/subRICH-articleLarge.jpg",
        "source":"text_files/adrienne_rich.txt"},
        4: {"name":"Pablo Neruda", "bio":"This is Pablo Neruda's Bio",
        "image":"http://www.nearshoreamericas.com/wp-content/uploads/2013/06/neruda-poetry-king.png",
        "source":"text_files/pablo_neruda.txt"},
        5: {"name": "Langston Hughes", "bio":"This is Pablo Neruda's Bio",
        "image":"https://zocalopoets.files.wordpress.com/2011/09/zp_langston-hughes-in-1941_portrait-photograph-by-gordon-parks.jpg",
        "source":"text_files/langston_hughes.txt"}
        }

# route to handle the landing page of a website.
@app.route('/')
def landing_page():
    return render_template("index.html")

# route to display a simple web page
# @app.route('/anne_sexton')
# def anne_sexton_tiles():
#     return render_template("anne_sexton.html")

# @app.route('/audre_lorde')
# def audre_lorde_tiles():
#     return render_template("audre_lorde.html")

# @app.route('/adrienne_rich')
# def adrienne_rich_tiles():
#     return render_template("adrienne_rich.html")

# @app.route('/pablo_neruda')
# def pablo_neruda_tiles():
#     return render_template("pablo_neruda.html")

# @app.route('/langston_hughes')
# def langston_hughes_tiles():
#     return render_template("langston_hughes.html")

@app.route('/poet')
def show_poet():
    poet_id = int(request.args.get('poet_id'))
    poet = POETS[poet_id]
    print POETS[poet_id]["name"]

    file_name = poet["source"]

    f = open(file_name)
    text = f.read()

    words_list = the_hell.assemble_words(text)

    print words_list



    # call your functions to get the words
    # send words to magnetic poetry template
    return render_template("tiles.html", poet=poet, words_list = words_list)
    # return render_template("tiles.html" poet=poet_name, words=words_list)




if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)

