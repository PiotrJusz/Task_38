import spacy
nlp = spacy.load("en_core_web_md")

# function read title and movie description from a file and store them in a dictionary movie_dict
def  set_movie():
    title = ""
    description = ""
    movie_dict = {}

    try:
        file = open("movies.txt","r")

    except FileNotFoundError:
        print("Can't open database.")
        exit()

    for item in file:
        title, description = item.split(":")
        # adding item to dictionary
        movie_dict[title] = description

    file.close()

    return movie_dict

hulk_description = """Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth,
the illuminati trick Hulk into a shuttle and launch him into space to a planet
where the Hulk can live in peace. Unfortunatrly, Hulk land on the planest Sakaar
where  he is sold into slavery and trained as a gladiator."""
model = nlp(hulk_description)

# variable stored title and description ov movies
movie_database = {}
# variable stored title of movie and similarity 
next_watches = []

# seting movie database as a list
movie_database = set_movie()

# creating list of titles and similarity to the model
for title in movie_database:
    similarity = nlp(movie_database[title]).similarity(model)
    next_watches.append([similarity, title])
    next_watches.sort(reverse = True)

# printing results
print("The most similar movie to \"Planet Hulk\" is/are: ")
for i in range (0, len(next_watches) ):
    print(i+1,". ", end = "") # order
    print(next_watches[i][1], end = "") # title of movie
    print(" - ", end = "")
    print( str( round( next_watches[i][0] * 100, 1 )  )+"%")
