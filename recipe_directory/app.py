from lib.database_connection import DatabaseConnection
from lib.recipe_repository import RecipeRepository

#Establish Connection
connection = DatabaseConnection()
connection.connect()

#Extract info from seed
connection.seed("seeds/recipe_directory.sql")

#Retrieve recipes from repository
recipe_repository = RecipeRepository(connection)
recipes = recipe_repository.all()

for recipe in recipes:
    print(recipe)

print(recipe_repository.find(3))
print(recipe_repository.find(8))


