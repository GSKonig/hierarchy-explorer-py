import pandas as pd


def load_nodes():
    df = pd.read_csv("data/hierarchy.csv").fillna("")
    return df.to_dict(orient="records")
