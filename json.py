# loading json file in dataframe

import pandas as pd

df = pd.read_json('data.json')

print(df.to_string()) 