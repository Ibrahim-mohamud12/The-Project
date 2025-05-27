from movie_explorer import favorites

def test_save_and_load(tmp_path):
    test_file = tmp_path / "favorites.json"
    favorites.FAV_FILE = test_file
    
    movie = {"Title": "Test Movie"}
    favorites.save_favorite(movie)
    
    favs = favorites.load_favorites()
    assert movie in favs
