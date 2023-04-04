# Import the spaCy module
import spacy


def get_movies_data():
    """
    This function will read the movies.txt and store each line in the textfile as an element of the list.
    This function will return a list.
    """
    with open('movies.txt', 'r') as file:
        data = (file.read().strip()).split('\n')
    return data


def get_movie_title():
    """
    This function will return a list that stores only movie titles.
    """
    movies_data = get_movies_data()
    movie_title_list = []
    n = 0
    for movie_data in movies_data:
        movie_data = (movie_data.split(':'))
        for data in movie_data:
            if n % 2 == 0: 
                movie_title_list.append(data)
            n += 1
    return movie_title_list


def get_movie_description():
    """
    This function will return a list that stores only movie descriptions.
    """
    movies_data = get_movies_data()
    movie_descr_list = []
    n = 0
    for movie_data in movies_data:
        movie_data = (movie_data.split(':'))
        for data in movie_data:
            if n % 2 != 0: 
                movie_descr_list.append(data)
            n += 1
    return movie_descr_list


def find_similar_movie(descrp):
    """
    This function takes in the description of the previous movie as a parameter and return the title of the most similar movie.
    """
    similarity_indexes = []
    movies_descr = get_movie_description()
    movies_title = get_movie_title()

    # This loop will go through every movie description in the movie_desr and compare it with the description that is provided.
    for token in movies_descr:
        token = nlp(token)
        for token_ in description:
            token_ = nlp(token_)
            similarity_indexes.append(token.similarity(token_))
    high_similarity_index = similarity_indexes.index(max(similarity_indexes))
    return movies_title[high_similarity_index]

# Create a model and store it in a variable
nlp = spacy.load('en_core_web_md')

description = ['Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.']

print(f'Based on the description of your previous move you should watch: {find_similar_movie(description)}')
