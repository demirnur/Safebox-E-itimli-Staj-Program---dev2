class Movie_operations:
    def __init__(self):
        self.file_name = "movies.txt"

    def add_movie_to_file(self, movie_name):
        with open(self.file_name, "a") as f:
            f.write(movie_name + "\n")
        print("Movie is added.")

    def get_movies_from_file(self):
        with open(self.file_name, "r") as f:
            movies = f.readlines()
            if not movies:
                print("There is no movie .")
            else:
                print("Movies:")
                for movie in movies:
                    print(movie.strip())

    def operations(self):
        while True:
            operation_choice = int(input("1-Add a movie, 2-List the movies, 3-Exit: "))

            if operation_choice == 1:
                movie_name = input("Name of movie: ")
                self.add_movie_to_file(movie_name)
            elif operation_choice == 2:
                self.get_movies_from_file()
            elif operation_choice == 3:
                print("Exit.")
                break
            else:
                print("The choice is wrong.")


M = Movie_operations()
M.operations()
