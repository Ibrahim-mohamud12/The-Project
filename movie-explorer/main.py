from movie_explorer.api import search_movies, get_movie_details
from movie_explorer.favorites import save_favorite
from movie_explorer.utils import format_movie

def main():
    query = input("Enter movie title: ")
    results = search_movies(query)

    if results.get("Response") == "True":
        for i, movie in enumerate(results["Search"], start=1):
            print(f"{i}. {format_movie(movie)}")

        choice = int(input("Pick a movie to see details (number): "))
        imdb_id = results["Search"][choice - 1]["imdbID"]
        details = get_movie_details(imdb_id)
        print(f"\nTitle: {details.get('Title')}\nPlot: {details.get('Plot')}")

        if input("Save to favorites? (y/n): ").lower() == "y":
            save_favorite(details)
            print("Saved!")
    else:
        print("No results found.")

if __name__ == "__main__":
    main()
