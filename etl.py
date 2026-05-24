import pandas as pd
import logging

logging.basicConfig(filename="etl.log",
                    level=logging.INFO,
                    format="%(asctime)s-%(levelname)s-%(message)s")
def extract():
    logging.info("Extract step started")
    df = pd.read_csv("employees.csv")
    logging.info("CSV file read successfully")
    return df

def transform(df):
    logging.info("Transform step started")
    df["salary"] = df["salary"].fillna(0)
    df = df.drop_duplicates()
    logging.info("Data cleaned successfully")
    return df

def load(df):
    logging.info("Load step started")
    df.to_csv("cleand_employees.csv",index=False)
    logging.info("Cleaned CSV saved successfully")
def main():
    try:
        logging.info("ETL Pipeline Started")
        df = extract() 
        cleaned_df = transform(df)
        load(cleaned_df)
        logging.info("ETL Pipeline Completed Successfully")
        print("ETL Completed Successfully")

    except Exception as e:
        logging.error(f"Error occurred: {e}")
        print("Error occurred:", e)
main()