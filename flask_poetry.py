
from flask import Flask, render_template, request
import the_hell

# "__name__" is a special Python variable for the name of the current module; Flask wants
# to know this to know what any imported things are relative to.
app = Flask(__name__)

POETS = { 1:
            {"name":"Anne Sexton",
            "bio":"era 1950 - 1970's  The modern model of the confessional poet, Anne Sexton began writing as an adult on the advice of a therapist and a priest -  within 10 years she had already won the Pulitzer Prize and established herself as both a cautionary tale of self-destruction and artistic genius.  Anne Sexton's signature style was highly personal verse that detailed her struggles with mental illness, suicide, adultery, sex and addiction. Her work conveyed an intimacy considered scandalous for the time and largely untouched by poetic discourse.",
            "image":"http://www.ikewrites.com/wp-content/uploads/2012/11/anne_sexton_2.jpg",
            "source":"text_files/anne_sexton.txt"},

        2:
            {"name": "Audre Lorde",
            "bio":"This is Audre Lorde's Bio",
            "image":"https://bluemilk.files.wordpress.com/2013/07/audre-lorde-the-berlin-years.jpg",
            "source":"text_files/audre_lorde.txt"},

        3:
            {"name":"Adrienne Rich",
            "bio":"era 1950's - 1970's  Widely regarded as one of the most influental poets of modern times, Adrienne Rich's work brought the patriarchal oppression of women into the forefront of poetic discourse. Adrienne Rich's signature style was marked by explorations of lesbian sexuality and desire, as well as constructions of gender and identity.  An intellectual powerhouse, Rich was one of the first poets to address and incorporate the theme of lesbian existence and sexual equality. Rich's work was a demonstration of the ways in which poetry can serve to dissolve societal isolation and validate the beauty of the social and sexual outlaw.",
            "image":"http://graphics8.nytimes.com/images/2012/03/29/obituaries/subRICH/subRICH-articleLarge.jpg",
            "source":"text_files/adrienne_rich.txt"},
        4:
            {"name":"Pablo Neruda",
            "bio":"era 1930's - 1960's Pablo Neruda was the pen name for Neftali Ricardo Reyes Basoalso, born July 12, 1904 in Chile. Pablo began writing as a teenager and often in green ink, his personal symbol for desire and hope. Although his work covered a variety of topics, he is most famous for his poetic musings on love. Pablo Neruda's signature style was rich and varied but often thematically oriented towards love and nature. He equated the women he loved with forces of nature and often represented them poetically as powerful forces raised to the cosmic degree.",
            "image":"http://www.nearshoreamericas.com/wp-content/uploads/2013/06/neruda-poetry-king.png",
            "source":"text_files/pablo_neruda.txt"},
        5:
            {"name": "Langston Hughes",
            "bio":"era 1920 - 1960's  A notable leader of the Harlem Renaissance, Langston Hughes is known for his insights and portrayal of black life in America. Hughes distinguished himself with his literary reflections on black culture, and sought to write about life in a way that reflected the entirety of black experience including both societal suffering and a love of language and music. One of the earliest innovators of a literary art form known as jazz poetry, Langston's style incorporated syncopated rhythms and repetitive musical phrasing into his work. Jazz poetry became the basis for the work of the Beat Generation and has evolved into modern times as hip-hop.",
            "image":"https://zocalopoets.files.wordpress.com/2011/09/zp_langston-hughes-in-1941_portrait-photograph-by-gordon-parks.jpg",
            "source":"text_files/langston_hughes.txt"}
        }

# route to handle the landing page of a website.
@app.route('/')
def landing_page():
    return render_template("index.html")


@app.route('/poet')
def show_poet():
    poet_id = int(request.args.get('poet_id'))
    poet = POETS[poet_id]
    bio = POETS[poet_id]["bio"]
    print POETS[poet_id]["name"]

    file_name = poet["source"]

    f = open(file_name)
    text = f.read()

    words_list = the_hell.assemble_words(text)

    print words_list

    return render_template("tiles.html", poet=poet, bio=bio,words_list = words_list)





if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)

