from lib.recipe import Recipes

class RecipeRepository:
    def __init__(self, connection):
        self.connection = connection
    
    def all(self):
        rows = self.connection.execute('SELECT * FROM recipes')
        recipes = []
        for row in rows:
            recipe = Recipes(row['id'], row['name'], row['cooking_time'], row['rating'])
            recipes.append(recipe)
        return recipes
    
    def find(self, id):
        rows = self.connection.execute("SELECT * FROM recipes WHERE id = %s", [id])
        row = rows[0]
        return Recipes(row['id'], row['name'], row['cooking_time'], row['rating'])
    