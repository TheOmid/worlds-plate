import pandas as pd


class DataVisualizer:
    def __init__(self):
        # Windows Path issues: use string literal and fullpath to read using pandas
        self.train = pd.read_json(
            r'C:\Users\oshahidi\Desktop\Worlds Plate\Dataset\JSON\train.json')
        self.train['number_ingredients'] = self.train['ingredients'].str.len()
