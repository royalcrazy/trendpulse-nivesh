import pandas as pd
import os
import glob

def clean_trending_data():
    list_of_files = glob.glob('data/trends_*.json')
    if not list_of_files:
        print("Error: Task 1 ki koi JSON file nahi mili!")
        return
    
    latest_file = max(list_of_files, key=os.path.getctime)
    print(f"Reading file: {latest_file}")

    df = pd.read_json(latest_file)

    print("Cleaning data...")
    
    df.drop_duplicates(subset=['post_id'], keep='first', inplace=True)

    df['score'] = df['score'].fillna(0).astype(int)
    df['num_comments'] = df['num_comments'].fillna(0).astype(int)

    output_file = "data/cleaned_trends.csv"
    df.to_csv(output_file, index=False)

    print(f"Success! Cleaned data saved to {output_file}")
    print(f"Total records processed: {len(df)}")

if __name__ == "__main__":
    clean_trending_data()
