"""
Donald Cull
Recipe Class
"""


class Recipe:

    recipe_difficulty_levels = ["Easy", "Medium", "Hard"]

    def __init__(self, name="new recipe", ingredients="add ingredients", method="add recipe method",
                 recipe_type="add recipe type",recipe_origin="add recipe origin", favourite=False,
                 recipe_difficulty="Set recipe difficulty"):
        """
        Initialise new recipe object
        :param name: name of new recipe
        """
        self.name = name
        self.ingredients = ingredients
        self.method = method
        self.recipe_type = recipe_type
        self.recipe_origin = recipe_origin
        self.favourite = favourite
        self.recipe_difficulty = recipe_difficulty

    def __str__(self):
        """

        :return: Displays all attributes of an recipe object
        """
        return "name:{}\ningredients:{}\nmethod:{}\nrecipe type:{}\norigin:{}\nfavourite:{}\ndifficulty:{}\n".\
            format(self.name, self.ingredients, self.method, self.recipe_type, self.recipe_origin,
                           self.favourite, self.recipe_difficulty)

    def favourite_recipe(self):
        """
        Toggles the favourite status of the recipe
        :return: None
        """
        if self.favourite:
            self.favourite = False
        else:
            self.favourite = True

    def display_recipe_difficulties(self):
        """

        :return: Recipe.recipe_difficulty_levels
        """
        return Recipe.recipe_difficulty_levels

    def set_recipe_difficulty(self, difficulty_choice):
        """
        Changes the difficulty of the recipe
        :return:
        """
        self.recipe_difficulty = difficulty_choice



