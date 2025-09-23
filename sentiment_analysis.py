import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = '.\\Downloads\\sentimentdataset.csv'

try:
    # Load the dataset
    data = pd.read_csv(file_path)
    
    # Ensure the 'Sentiment' column exists
    if 'Sentiment' not in data.columns:
        raise ValueError("The dataset does not contain a 'Sentiment' column.")
except FileNotFoundError:
    print("File not found. Please check the file path and try again.")
    exit()
except ValueError as e:
    print(e)
    exit()

# Count the occurrences of each sentiment
sentiment_counts = data['Sentiment'].value_counts()
total_counts = sentiment_counts.sum()

# Filter sentiments above 1.5%
sentiment_percentages = (sentiment_counts / total_counts) * 100
filtered_sentiments = sentiment_percentages[sentiment_percentages > 1.0]
filtered_counts = sentiment_counts[filtered_sentiments.index]

# Automatically generate sentiment labels if not already mapped
unique_sentiments = filtered_counts.index
labels = [
    f"Sentiment {sentiment}" if sentiment not in [0, 1] else 
    {0: "Negative", 1: "Positive"}[sentiment]
    for sentiment in unique_sentiments
]

# Enhance the visuals for the pie chart
plt.figure(figsize=(12, 10))
filtered_counts.plot.pie(
    autopct='%1.1f%%',
    labels=labels,
    colors=sns.color_palette("coolwarm", len(unique_sentiments)),
    startangle=140,
    textprops={'fontsize': 14},
    wedgeprops={'linewidth': 1.5, 'edgecolor': 'gray'}
)
plt.title('Sentiment Distribution (Enhanced Pie Chart)', fontsize=20, fontweight='bold')
plt.ylabel('')  # Remove the default y-label
plt.savefig('.\\Downloads\\enhanced_sentiment_pie_chart.png', dpi=300)
plt.show()

# Enhance the visuals for the bar graph
plt.figure(figsize=(14, 10))
sns.barplot(
    x=unique_sentiments,
    y=filtered_counts.values,
    palette=sns.color_palette("coolwarm", len(unique_sentiments))
)
for i, value in enumerate(filtered_counts.values):
    plt.text(i, value + max(filtered_counts.values) * 0.02, f'{value:,}', ha='center', fontsize=14, color='black', fontweight='bold')

plt.title('Sentiment Distribution (Enhanced Bar Graph)', fontsize=20, fontweight='bold')
plt.xlabel('Sentiments', fontsize=16, fontweight='bold')
plt.ylabel('Count', fontsize=16, fontweight='bold')
plt.xticks(ticks=range(len(labels)), labels=labels, fontsize=14, fontweight='bold')
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.8)
plt.tight_layout()
plt.savefig('.\\Downloads\\enhanced_sentiment_bar_chart.png', dpi=300)
plt.show()
