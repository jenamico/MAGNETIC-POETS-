
from flask import Flask, render_template, request
import the_hell

# "__name__" is a special Python variable for the name of the current module; Flask wants
# to know this to know what any imported things are relative to.
app = Flask(__name__)

POETS = { 1:
            {"name":"Anne Sexton",
            "bio":" Anne Sexton began writing as an adult on the advice of a therapist and a priest -  within 10 years she had won the Pulitzer Prize and established herself as both a cautionary tale of self-destruction and artistic genius.  Her signature style was highly personal verse that detailed her struggles with mental illness, suicide, adultery, sex and addiction. Her work conveyed an intimacy considered scandalous for the time and largely untouched by poetic discourse.",
            "image":"static/img/sextonedited.jpg",
            "source":"text_files/anne_sexton.txt",
            "quote": "Saints have no moderation, nor do poets, just exuberance."},

        2:
            {"name": "Audre Lorde",
            "bio":"Audre Lorde's work combined elements of social liberalism and poetics to express her identity as a black, feminist, lesbian.  Lorde's signature style echoes her depth of feeling and intellectual rigor and include the thematic elements of revolution and authenticity. Her primary goal in writing was communication - to share not only the triumphs of life, but also the intense often unmitigated pain of living.",
            "image":"static/audreedit.jpg",
            "source":"text_files/audre_lorde.txt",
            "quote": "I am deliberate and afraid of nothing."},

        3:
            {"name":"Adrienne Rich",
            "bio":"Widely regarded as one of the most influental poets of modern times, Adrienne Rich's work brought the patriarchal oppression of women into the forefront of poetic discourse. Adrienne Rich's signature style was marked by explorations of lesbian sexuality and desire, as well as constructions of gender and identity.  An intellectual powerhouse, Rich's work was a demonstration of the ways in which poetry can serve to dissolve societal isolation and validate the social and sexual outlaw.",
            "image":"static/img/adriennebw.jpg",
            "source":"text_files/adrienne_rich.txt",
            "quote":"The moment of change is the only poem."},
        4:
            {"name":"Pablo Neruda",
            "bio":"Pablo Neruda was the pen name for Neftali Ricardo Reyes, who began writing as a teenager and often in green ink, his personal symbol for desire and hope. Although his work covered a variety of topics, he is most famous for his poetic musings on love. Pablo Neruda's signature style was rich and varied but often thematically oriented towards love and nature. He equated the women he loved with forces of nature and often represented them poetically as powerful forces raised to the cosmic degree.",
            "image":"http://www.lpm-blog.com.br/wp-content/uploads/2013/05/neruda_foto.jpg",
            "source":"text_files/pablo_neruda.txt",
            "quote": "I love you as certain dark things are meant to be loved, in secret, between the shadow and the soul."},
        5:
            {"name": "Langston Hughes",
            "bio":"A notable leader of the Harlem Renaissance, Langston Hughes is known for his insights and portrayal of black life in America. One of the earliest innovators of a literary art form known as jazz poetry, Langston's style incorporated syncopated rhythms and repetitive musical phrasing into his work. Jazz poetry became the basis for the work of the Beat Generation and has evolved into modern times as hip-hop.",
            "image":"http://cp91279.biography.com/1000509261001/1000509261001_2105665572001_Langston-Hughes-House-in-Harlem.jpg",
            "source":"text_files/langston_hughes.txt",
            "quote":"Bring me all your dreams, you dreamer/That I may wrap them in a blue cloud-cloth, Away from the too-rough fingers of the world."},
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
    quote = POETS[poet_id]["quote"]

    file_name = poet["source"]

    f = open(file_name)
    text = f.read()

    words_list = the_hell.assemble_words(text)

    print words_list

    return render_template("individual.html", poet=poet, bio=bio, quote=quote, words_list = words_list)


@app.route('/gallery')
def gallery_page():
    return render_template("gallery.html")


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)

