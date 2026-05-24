import pandas as pd

def extract():
    df =pd.read_csv("employees.csv")
    return df

def transform(df):
    df["salary"] = df["salary"].fillna(0)
    df = df.drop_duplicate()
    return df

def load(df):
    df.to_csv("cleand_employees.csv",index=False)
def main():
   df = extract() 
   cleaned_df = transform(df)
   load(cleaned_df)
   print("EtL Completed Successfully")
main()