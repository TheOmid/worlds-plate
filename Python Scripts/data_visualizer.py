import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff


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
                         labels={"number_ingredients": "Number of Ingredients"},
                         title="Histogram of Ingredients")
            fig.show()

        graphIngredientsHistogram()