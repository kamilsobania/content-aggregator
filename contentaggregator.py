import csv
import random

def read_historical_data(csv_file):
    aggregated_articles = []
    
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            article_info = {
                "title": row["title"],
                "content": row["content"]
            }
            aggregated_articles.append(article_info)
    
    return aggregated_articles

if __name__ == "__main__":
    csv_file = "historical_news_data.csv"  # Replace with the path to your CSV file
    news_articles = read_historical_data(csv_file)
    
    # Print the aggregated news articles
    for idx, article in enumerate(news_articles, start=1):
        print(f"{idx}. {article['title']}")
        print(article['content'])
        print("\n")
