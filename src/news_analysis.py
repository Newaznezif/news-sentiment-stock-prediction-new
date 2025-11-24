import pandas as pd

class NewsData:
    """Class to handle loading, cleaning, and analyzing news CSVs."""

    def __init__(self, file_path, date_col="date"):
        self.file_path = file_path
        self.date_col = date_col
        self.df = None
        self.load()

    def load(self):
        """Load CSV and parse date column."""
        df = pd.read_csv(self.file_path)
        if self.date_col in df.columns:
            df[self.date_col] = pd.to_datetime(df[self.date_col], errors='coerce')
            df = df.dropna(subset=[self.date_col])
            df = df.sort_values(self.date_col).reset_index(drop=True)
            df = df.rename(columns={self.date_col: "timestamp"})
        else:
            raise KeyError(f"Expected column '{self.date_col}'")
        self.df = df
        return df

    def clean_text(self, column="headline"):
        """Clean the text column: lowercase, remove special chars."""
        df = self.df.copy()
        df[column] = df[column].astype(str).str.replace(r"[^A-Za-z0-9\s]", "", regex=True)
        df[column] = df[column].str.lower().str.strip()
        self.df = df
        return df

    def daily_publication_counts(self):
        """Count number of articles per day."""
        return self.df.groupby(self.df["timestamp"].dt.date).size()
