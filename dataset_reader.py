import pandas as pd

def get_valorant_stats_data():
  return pd.read_csv("static/datasets/valorant-stats.csv")