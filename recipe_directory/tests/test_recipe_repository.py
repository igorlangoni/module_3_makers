from lib.recipe_repository import RecipeRepository
from lib.recipe import Recipes
from lib.database_connection import DatabaseConnection

"""
When calling #all
Returns all instances of recipe in the directory
"""

def test_calling_all_returns_all_instances(db_connection):
    db_connection.seed("seeds/recipe_directory.sql")
    recipe_repository = RecipeRepository(db_connection)
    expected = recipe_repository.all()
    assert expected == [
        Recipes(1, 'Strogonoff', 40, 8),
        Recipes(2, 'Lasagna', 70, 7.5),
        Recipes(3, 'Feijoada', 120, 10),
        Recipes(4, 'Prawn Curry', 40, 7.5),
        Recipes(5, 'Rice and Beans', 25, 7),
        Recipes(6, 'Meatball Spaghetti', 25, 8),
        Recipes(7, 'Roasted Joint', 300, 8),
        Recipes(8, 'Cake', 120, 4)
    ]

def test_calling_find_returns_specific_recipe(db_connection):
    db_connection.seed("seeds/recipe_directory.sql")
    repository = RecipeRepository(db_connection)
    expected = repository.find(2)
    assert expected == Recipe(2, 'Lasagna', 70, 7.5)

