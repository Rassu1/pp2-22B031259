movies = [
    {
        "name": "Usual Suspects",
        "imdb": 7.0,
        "category": "Thriller"
    },
    {
        "name": "Hitman",
        "imdb": 6.3,
        "category": "Action"
    },
    {
        "name": "Dark Knight",
        "imdb": 9.0,
        "category": "Adventure"
    },
    {
        "name": "The Help",
        "imdb": 8.0,
        "category": "Drama"
    },
    {
        "name": "The Choice",
        "imdb": 6.2,
        "category": "Romance"
    },
    {
        "name": "Colonia",
        "imdb": 7.4,
        "category": "Romance"
    },
    {
        "name": "Love",
        "imdb": 6.0,
        "category": "Romance"
    },
    {
        "name": "Bride Wars",
        "imdb": 5.4,
        "category": "Romance"
    },
    {
        "name": "AlphaJet",
        "imdb": 3.2,
        "category": "War"
    },
    {
        "name": "Ringing Crime",
        "imdb": 4.0,
        "category": "Crime"
    },
    {
        "name": "Joking muck",
        "imdb": 7.2,
        "category": "Comedy"
    },
    {
        "name": "What is the name",
        "imdb": 9.2,
        "category": "Suspense"
    },
    {
        "name": "Detective",
        "imdb": 7.0,
        "category": "Suspense"
    },
    {
        "name": "Exam",
        "imdb": 4.2,
        "category": "Thriller"
    },
    {
        "name": "We Two",
        "imdb": 7.2,
        "category": "Romance"
    }
]

"""
Write a function that takes a single movie and returns True if its IMDB score is above 5.5
"""


def More_5_with_half(movies):
    if movies['imdb'] > 5.5:
        return True
    return False


print(More_5_with_half(movies[1]))

"""
Write a function that returns a sublist of movies with an IMDB score above 5.5.
"""


def sublist_score_More_5(movies):
    spisok = []
    for i in range(0, len(movies)):
        pos = movies[i]
        if pos['imdb'] > 5.5:
            spisok.append(pos)
    return spisok


print(sublist_score_More_5(movies))

"""
Write a function that takes a category name and returns just those movies under that category.
"""


def return_movie_category(movies, cat_name):
    spisok = []
    for i in movies:
        curr_cat = i['category']
        if cat_name.lower() == curr_cat.lower():
            spisok.append(i)
    return spisok


print(return_movie_category(movies, 'Romance'))

"""
Write a function that takes a list of movies and computes the average IMDB score.
"""


def average_score(movies):
    score = 0
    cnt = len(movies)
    for i in movies:
        score = score + i['imdb']
    score = score / cnt
    return score


print(average_score(movies))

"""
Write a function that takes a category and computes the average IMDB score.
"""


def category_average_score(movies, cat_name):
    cat_movies = return_movie_category(movies, cat_name)
    cat_average = average_score(cat_movies)
    return cat_average


print(category_average_score(movies, 'Drama'))
