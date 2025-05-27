from movie_explorer.utils import format_movie

def test_format_movie():
    movie = {"Title": "Inception", "Year": "2010", "imdbID": "tt1375666"}
    assert format_movie(movie) == "Inception (2010) - tt1375666"
