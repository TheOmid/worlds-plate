import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff

#FIXME: code structure can be improved, refactor when possible
class DataVisualizer:
    def __init__(self):
        # Windows Path issues: use string literal and fullpath to read using pandas
        self.train = pd.read_json(
            r'C:\Users\oshahidi\Desktop\Worlds Plate\Dataset\JSON\train.json')
        self.train['number_ingredients'] = self.train['ingredients'].str.len()

    def getRecipesPerCuisine(self):
        recipiesPerCuisineCount = self.train['cuisine'].value_counts()
        return pd.DataFrame({'cuisine': recipiesPerCuisineCount.index, 'number of recipes': recipiesPerCuisineCount.values})

    def graphRecipesPerCuisine(self):
        data = self.getRecipesPerCuisine()
        fig = px.bar(data,
                     x="number of recipes",
                     y="cuisine", orientation='h',
                     labels={
                         "number of recipes": "Number of Recipes",
                         "cuisine": "Cuisine",
                         "species": "Species of Iris"
                     },
                     title="Number of Recipes Per Cuisine",
                     color="cuisine")
        fig.show()

    def graphDistIngredients(self):
        fig = ff.create_distplot([self.train['number_ingredients']], [
            "Distribution of Number of Ingredients"], curve_type='normal')
        fig.show()

        def graphIngredientsHistogram():
            fig = px.histogram(self.train, x="number_ingredients",
                               labels={
                                   "number_ingredients": "Number of Ingredients"},
                               title="Histogram of Ingredients")
            fig.show()

        graphIngredientsHistogram()

    def getMostCommonIngredients(self, limit=10):
        ingredients_list = self.getAllIngredients(self.train['ingredients'])
        ingredient_dict = self.getUniqueIngredientsCount(ingredients_list)
        ingredient_dict = self.sortDictionaryByValue(ingredient_dict)
        df = pd.DataFrame(ingredient_dict.items(), columns=['ingredient', 'count'])

        return df.iloc[-limit:, :]

    def graphMostCommonIngredients(self, limit=10):
        data = self.getMostCommonIngredients(limit)
        fig = px.bar(data,
                     x="ingredient",
                     y="count",
                     labels={
                         "ingredient": "Ingredient",
                         "count": "Count"
                     },
                     title=f"{limit} Most Popular Ingredients Worldwide",
                     color="ingredient")
        fig.show()

    def sortDictionaryByValue(self, dict):
        return {k: v for k, v in sorted(dict.items(), key=lambda item: item[1])}

    def getUniqueIngredientsCount(self, ingredients_list):
        ingredient_dict = {}
        for ingredient in ingredients_list:
            ingredient_dict[ingredient] = ingredient_dict[ingredient] +1 \
                if ingredient in ingredient_dict \
                else 1

        return ingredient_dict

    def getAllIngredients(self, ingredients_list):
        ingredients_list = [
            ingredient for ingredients in ingredients_list for ingredient in ingredients
        ]

        return ingredients_list

    def getUniqueIngredientsCountByCuisine(self, cuisine):
        df = self.train.groupby('cuisine')
        for groupId, group in df:
            if groupId == cuisine:
                ingredients_list = self.getAllIngredients(group["ingredients"]) 
                return self.getUniqueIngredientsCount(ingredients_list)

    def getMostCommonIngredientsByCuisine(self, cuisine, limit):
        ingredient_dict = self.getUniqueIngredientsCountByCuisine(cuisine)
        ingredient_dict = self.sortDictionaryByValue(ingredient_dict)
        df = pd.DataFrame(ingredient_dict.items(), columns=['ingredient', 'count'])

        return df.iloc[-limit:, :]

    def graphMostCommonIngredientsByCuisine(self, cuisine="italian", limit=10):
        data = self.getMostCommonIngredientsByCuisine(cuisine, limit)
        fig = px.bar(data,
                     x="ingredient",
                     y="count",
                     labels={
                         "ingredient": "Ingredient",
                         "count": "Count"
                     },
                     title=f"{limit} Most Popular Ingredients of {cuisine} cuisine",
                     color="ingredient")
        fig.show()