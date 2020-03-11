import pandas as pd
import download
import os

url_db = "https://www.data.gouv.fr/fr/datasets/r/ab84353b-498b-4ef5-9a02-a6403f2ead96"
path_target = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "data", "bicycle_db.csv")


class Load_db:
  def __init__(self, url=url_db, target_name=path_target):
    download(url, target_name, replace=False)
    
  @staticmethod
  def save_as_df():
    df_bikes = pd.read_csv(path_target, na_values="", low_memory=False, converters={'data': str, 'heure': str})
    return df_bikes