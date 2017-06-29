"""
Donald Cull
"""


class RecipeList:

    def __init__(self):
        """
        Initialise new recipe list
        """
        self.recipe_list = []

    def __str__(self):
        """

        :return: Returns string representation of recipes in recipe list
        """
        return ';'.join(str(recipe) for recipe in self.recipe_list)

    def add_recipe_to_list(self, recipe):
        """
        Adds new recipe to recipe list
        :param recipe: Recipe to be added to the list
        :return: None
        """
        self.recipe_list.append(recipe)
