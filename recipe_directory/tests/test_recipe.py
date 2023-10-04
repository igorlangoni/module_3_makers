from lib.recipe import Recipe

"""
When constructing an instance
With name, cooking_time and rating
These are reflected on the properties
"""
def test_constructing_reflect_properties():
    recipe = Recipe(1, 'Strogonoff', 40, 8)
    assert recipe.id == 1
    assert recipe.name == 'Strogonoff'
    assert recipe.cooking_time == 40
    assert recipe.rating == 8
"""
When I construct identical recipes
They are recognized as equals
"""
def test_when_two_objects_are_the_same_returns_true():
    recipe_1 = Recipe(1, 'Strogonoff', 40, 8)
    recipe_2 = Recipe(1, 'Strogonoff', 40, 8)
    assert recipe_1 == recipe_2
