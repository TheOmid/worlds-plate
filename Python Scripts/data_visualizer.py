import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff

#FIXME: code structure can be improved
class DataVisualizer:
    def __init__(self):
        # Windows Path issues: use string literal and fullpath to read using pandas
        self.train = pd.read_json(
            r'C:\Users\oshahidi\Desktop\Worlds Plate\Dataset\JSON\train.json')
        self.train['number_ingredients'] = self.train['ingredients'].str.len()

    def getRecipesPerCuisine(self):
        recipiesPerCuisineCount = self.train['cuisine'].value_counts()
        return pd.DataFrame({'cuisine': recipiesPerCuisineCount.index, 'number of recipes': recipiesPerCuisineCount.values})

    def selfgraphRecipesPerCuisine(self):
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
        ingredient_dict = self.getUniqueIngredientsCount()
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
                     title="Most Popular Ingredients Worldwide",
                     color="ingredient")
        fig.show()

    def sortDictionaryByValue(self, dict):
        return {k: v for k, v in sorted(dict.items(), key=lambda item: item[1])}

    def getUniqueIngredientsCount(self):
        ingredients_list = self.getAllIngredients()
        ingredient_dict = {}
        for ingredient in ingredients_list:
            ingredient_dict[ingredient] = ingredient_dict[ingredient] +1 \
                if ingredient in ingredient_dict \
                else 1

        return ingredient_dict