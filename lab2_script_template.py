"""
The main purpose of this script is to print my name and split my first name from my last, print my student number, print my favourite pizza toppings, movies and what genre those movies are. The toppings must be printed in all caps first, and then print again with additional toppings added but in lower case. The toppings must be printed with bullet points. Then I must print out only the movie genres and have them seperated with commas, and do the same with the movie titles but they must all begin with capitals.
"""
def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = {
        "full_name": "Jordan Hall",
        "student_id": 10227505,
        "pizza_toppings": ["PEPPERONI", "GREEN PEPPERS", "BACON"],
        "movies": [
            {
                "title": "scott pilgrim",
                "genre": "action"
            },
            {
                "title": "hot rod",
                "genre": "comedy"
            }
        ]
    }

    # TODO: Step 3 - Add another movie to the data structure
    new_movie =  {"title": "toy story", "genre": "adventure"}
    about_me["movies"].append(new_movie)
    print_student_name_and_id(about_me)
    print_pizza_toppings(about_me)
    add_pizza_toppings(about_me, ("MUSHROOMS", "SAUSAGE"))
    print_pizza_toppings(about_me)
    print_movie_genres(about_me)
    print_movie_titles(about_me)
# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):
    full_name = about_me["full_name"]
    first_name = full_name.split()[0]
    student_id = about_me["student_id"]
    print(f"My name is {full_name}, but you can call me Mr. {first_name}.\nMy student ID is {student_id}")
    return

# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    for new in toppings:
        about_me["pizza_toppings"].append(new)
    about_me["pizza_toppings"] = [toppings.lower() for toppings in about_me["pizza_toppings"]]
    about_me["pizza_toppings"].sort()
    return about_me["pizza_toppings"]

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    print("My favourite toppings are: ")
    for stuff in about_me["pizza_toppings"]:
        print(f"- {stuff}")
    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    moviegen = [single["genre"] for single in about_me["movies"]]
    genres = ", ".join(moviegen)
    print(f"I like to watch {genres}")
    return

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(about_me):
    favourites = [mymovies["title"] for mymovies in about_me["movies"]]
    favs = ", ".join(favourites)
    print(f"Some of my favourite movies are {favs.title()}")
    return
    
if __name__ == '__main__':
    main()