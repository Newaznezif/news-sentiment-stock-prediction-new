import pandas as pd
import re

class NewsData:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)

    def clean_text(self):
        self.df['headline'] = self.df['headline'].str.replace(r"[^A-Za-z0-9 ]", "", regex=True)
        self.df['headline'] = self.df['headline'].str.lower()
        return self.df

    def publisher_analysis(self):
        return self.df['publisher'].value_counts().head(10)
