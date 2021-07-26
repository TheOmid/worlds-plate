import pandas as pd
import plotly.express as px


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
