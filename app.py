# Import sys module
import sys

# Create movie list
movies_list = []


# Function Name: menu
# Description: Displays a list of program options and accepts input from user
def menu():
    options = input('Options: Add new movie (press "a"), Show all movies (press "s"), Find movie (press "f"), '
                    'Quit(press "q"), Delete movie (press "d") \n')
    while options != 'q':
        # user presses wants to add a new movie
        if options == 'a':
            add_movie_to_list()
        # User wants to see all movies
        elif options == 's':
            if len(movies_list) > 0:
                show_all_movies()
            else:
                print('There are no records to display.\n')
        elif options == 'f':
            find_movie()
        elif options == 'd':
            delete_movie()
        else:
            print('That is not a valid command. Please choose a valid command.\n')
        options = input('Options: Add new movie (press "a"), Show all movies (press "s"), Find movie (press "f"), '
                        'Quit(press "q"), Delete movie (press "d") \n')

    # User wants to quit
    if options == 'q':
        sys.exit()


# Function Name: add_movie
# Description: Creates new movie dictionary based on user input
def add_movie():
    # Create variable for movie input validation
    movie_validation = False
    # Get user input for new movie
    name = input('Please enter the name of the new movie: \n')
    director = input('Please enter the director(s) of the new movie: \n')
    year = input('Please enter the year that the movie was released: \n')
    # Validate that input is numeric
    if year.isdigit() is True:
        movie_validation = True
    else:
        movie_validation = False
    if movie_validation is True:
        # Create keys for new movie
        movie_keys = ('name', 'director', 'year', 'location', 'shelf')
        # Create new movie
        new_movie = dict.fromkeys(movie_keys)
        # Create updates for new movie
        updated_name = {'name': name}
        updated_director = {'director': director}
        updated_year = {'year': year}
        # Update keys for new movie
        new_movie.update(updated_name)
        new_movie.update(updated_director)
        new_movie.update(updated_year)
        # Tell user movie was added
        print('The movie was successfully added.\n')
        # Return final new movie
        return new_movie
    else:
        print('Please input a valid year.')


# Function Name: delete_movie
# Description: Removes movie from the list
def delete_movie():
    # Make sure there are movies
    if len(movies_list) > 0:
        # User specifies movie to be deleted
        deletion_choice = input('Please input the name of the movie that you want to delete: \n').lower()
        # Loop through movies
        for movie in movies_list:
            # Delete movie if it matches user input
            if deletion_choice == movie['name'].lower():
                movies_list.remove(movie)
                print('The movie was successfully deleted.')
    else:
        print('There are no movies to delete. \n')


# Function Name: add_movie_to_list
# Description: Adds new movie dictionary to list of movies
def add_movie_to_list():
    movies_list.append(add_movie())
    return movies_list


# Function Name: show_all_movies
# Description: Displays all movie dictionaries that are in the movie list
def show_all_movies():
    for movie in movies_list:
        print_movie(movie)


# Function Name: print_movie
# Description: Prints all of the information for one movie
def print_movie(movie):
    print('')
    print(f"Name: {movie['name']}")
    print(f"Director: {movie['director']}")
    print(f"Year: {movie['year']}")
    print('')


# Function Name: find_movie
# Description: Searches lists of movies based on user-based parameters and returns results
def find_movie():
    # Create array that will hold the movies that match the search parameters
    search_results = []
    # Create variable for validation
    validation = False
    # Accept user input
    search_type = input('Please input how you want to search for movies, by "name", "director", or "year": \n')
    # User searches by name
    if search_type.lower() == 'name':
        validation = True
        search_input = input('Please enter the name of the movie you want to search for: \n').lower()
        for movie in movies_list:
            if search_input == movie['name'].lower():
                search_results.append(movie)
    # User searches by director
    elif search_type.lower() == 'director':
        validation = True
        search_input = input('Please enter the name of the director you want to search for: \n').lower()
        for movie in movies_list:
            if search_input == movie['director'].lower():
                search_results.append(movie)
    # User searches by year
    elif search_type.lower() == 'year':
        search_input = input('Please enter the year of the movie you want to search for: \n')
        # Validate that input is numeric
        if search_input.isdigit():
            validation = True
            for movie in movies_list:
                if search_input == movie['year'].lower():
                    search_results.append(movie)
        else:
            print('Please input a valid year.\n')
    # User enters invalid parameter
    else:
        print('That is not a valid search parameter. Please search by "name", "director", or "year".\n')
        validation = False
    # Show user search results
    if validation is True:
        # Create variable used to validate that the list contains results
        list_validation = False
        if len(search_results) > 0:
            list_validation = True
            if list_validation is True:
                print('The following results match your search: \n')
                for result in search_results:
                    print_movie(result)
        else:
            print('There are no movies that match your search results.\n')


# Call menu function
menu()
