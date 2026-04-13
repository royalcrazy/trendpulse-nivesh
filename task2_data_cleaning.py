import pandas as pd
import os
import glob

def clean_trending_data():
    # 1. Sabse latest JSON file dhoondna (Task 1 ka output)
    list_of_files = glob.glob('data/trends_*.json')
    if not list_of_files:
        print("Error: Task 1 ki koi JSON file nahi mili!")
        return
    
    latest_file = max(list_of_files, key=os.path.getctime)
    print(f"Reading file: {latest_file}")

    # 2. JSON ko DataFrame mein load karna
    df = pd.read_json(latest_file)

    # 3. Data Cleaning
    print("Cleaning data...")
    
    # Duplicate posts hatayein (post_id ke basis par)
    df.drop_duplicates(subset=['post_id'], keep='first', inplace=True)

    # Agar koi empty values hain toh unhe handle karein
    # Example: 'score' ya 'num_comments' agar missing ho toh 0 kar dein
    df['score'] = df['score'].fillna(0).astype(int)
    df['num_comments'] = df['num_comments'].fillna(0).astype(int)

    # 4. CSV mein save karna
    output_file = "data/cleaned_trends.csv"
    df.to_csv(output_file, index=False)

    print(f"Success! Cleaned data saved to {output_file}")
    print(f"Total records processed: {len(df)}")

if __name__ == "__main__":
    clean_trending_data()