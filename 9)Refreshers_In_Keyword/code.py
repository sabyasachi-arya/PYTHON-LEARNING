# In keyword is used to check if a particular thing is inside of something or not.
Uefa_members = ["Real Madrid", "AC Milan", "Barcelona", "PSG", "Man Utd"]  # sets can be used here, because clubs
# won't be repeated
print("Arsenal" in Uefa_members)
print("AC Milan" in Uefa_members)
print("---------------------------------------------------------")
movies_by_Nolan = {"Interstellar", "Inception", "Oppenheimer"}  # SET is used because same movies can not be repeated
user_movie = input("Type a movie name to check if its made by Nolan or not: ").title()
# because every element in the set is in .title mode(first letter is capital)
# we also convert the input to the same style by .title so that user can type anyway they want but the input
# will always be the first letter capital so that it will be easy to check if the input is in the set
if user_movie in movies_by_Nolan:
    print(f"Yep! {user_movie} was made by Christopher Nolan.")
else:
    print(f"Nope, I dont know who made {user_movie}.")