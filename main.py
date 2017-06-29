"""
Donald Cull
Recipe App
This program will allow user to add, edit, view and manage cooking recipes.
"""
from Recipe import Recipe
from recipe_list import RecipeList

user_recipes = RecipeList()
first_recipe = Recipe("Onigiri","rice")
user_recipes.add_recipe_to_list(first_recipe)
print(user_recipes)

app = App(title="Hello world")
app.display()
