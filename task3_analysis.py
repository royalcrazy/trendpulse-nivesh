import pandas as pd
import numpy as np
import os

def analyze_trending_data():
    # 1. Cleaned CSV file then load 
    file_path = "data/cleaned_trends.csv"
    
    if not os.path.exists(file_path):
        print("Error: Task 2 ki CSV file nahi mili!")
        return

    df = pd.read_csv(file_path)

    print("--- HackerNews Trend Analysis ---")

    # 2. Basic Stats using NumPy/Panda
    avg_scores = df.groupby('category')['score'].mean()
    print("\nAverage Scores by Category:")
    print(avg_scores)

    # 3. each category popular score
    print("\nTop Story per Category:")
    top_stories = df.sort_values('score', ascending=False).drop_duplicates(['category'])
    print(top_stories[['category', 'title', 'score']])

    #4  total engagement using numpy
    total_comments = np.sum(df['num_comments'].values)
    print(f"\nTotal Comments across all stories: {total_comments}")

    summary_text = f"Analysis Summary:\nTotal Stories: {len(df)}\nTotal Comments: {total_comments}"
    with open("data/analysis_summary.txt", "w") as f:
        f.write(summary_text)
    
    print("\nAnalysis complete. Summary saved to data/analysis_summary.txt")

if __name__ == "__main__":
    analyze_trending_data()