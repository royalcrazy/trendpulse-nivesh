import pandas as pd
import matplotlib.pyplot as plt
import os

def create_visualizations():
    # 1. Data Load
    file_path = "data/cleaned_trends.csv"
    if not os.path.exists(file_path):
        print("Error: CSV file nahi mili!")
        return
    
    df = pd.read_csv(file_path)

    # Making visualization Folder
    if not os.path.exists('visuals'):
        os.makedirs('visuals')

    # Bar Chart 
    plt.figure(figsize=(10, 6))
    category_counts = df['category'].value_counts()
    category_counts.plot(kind='bar', color='skyblue', edgecolor='black')
    
    plt.title('Number of Trending Stories per Category', fontsize=14)
    plt.xlabel('Category', fontsize=12)
    plt.ylabel('Count', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Save chart
    plt.tight_layout()
    plt.savefig('visuals/category_counts.png')
    print("Bar chart saved to visuals/category_counts.png")
    plt.close()

    # Scatter Plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['score'], df['num_comments'], alpha=0.5, color='orange')
    
    plt.title('Engagement: Score vs Comments', fontsize=14)
    plt.xlabel('Upvotes (Score)', fontsize=12)
    plt.ylabel('Number of Comments', fontsize=12)
    
    # Save chart
    plt.tight_layout()
    plt.savefig('visuals/engagement_scatter.png')
    print("Scatter plot saved to visuals/engagement_scatter.png")
    plt.close()

    print("\nAll visualizations completed successfully!")

if __name__ == "__main__":
    create_visualizations()