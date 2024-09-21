import polars as pl
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

dataset = pl.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv", 
                       truncate_ragged_lines=True)

def get_summary_statistics():
    return dataset.describe()

def get_mode():
    return (
        dataset
        .select([
            pl.col("carat").mode().alias("carat"),
            pl.col("cut").mode().alias("cut"),
            pl.col("color").mode().alias("color"),
            pl.col("clarity").mode().alias("clarity"),
            pl.col("depth").mode().alias("depth"),
            pl.col("table").mode().alias("table"),
            pl.col("price").mode().alias("price"),
            pl.col("x").mode().alias("x"),
            pl.col("y").mode().alias("y"),
            pl.col("z").mode().alias("z"),
        ])
    ).to_dict()


def get_variance_std():
    variance = dataset["price"].var()
    std_dev = dataset["price"].std()
    return variance, std_dev

def generate_viz_diamonds(save_as_image=False):
    """Generates and saves a visualization of diamond prices."""
    prices = dataset['price'].to_numpy()  # Convert to NumPy array

    plt.figure(figsize=(10, 6))
    ax = sns.histplot(prices, color='blue', kde=True, bins=30, alpha=1, fill=True, edgecolor="black", linewidth=3)
    ax.set_title('Distribution of Diamond Prices')
    ax.set_xlabel('Price')
    ax.set_ylabel('Frequency')

    if save_as_image:
        plt.savefig('diamonds_price_distribution.png')
    plt.show()

import pandas as pd

def save_diamonds_report_to_markdown():
    """Generates a markdown report for the diamonds dataset and saves it to a file."""
    # Call helper functions with the dataset
    summary_df = get_summary_statistics()
    mode_dict = get_mode()  # get_mode should return a dictionary now
    variance, std_dev = get_variance_std()
    
    # Manually create markdown for summary statistics
    markdown_summary = "# Summary Statistics\n"
    for col in summary_df.columns:
        markdown_summary += f"## {col}\n"
        for stat in summary_df[col]:
            markdown_summary += f"- {stat}\n"
    
    # Manually create markdown for mode
    markdown_mode = "## Mode\n"
    for col, value in mode_dict.items():  # iterate over the dictionary
        markdown_mode += f"- {col}: {value}\n"
    
    variance_std_markdown = f"**Variance:** {variance}\n\n**Standard Deviation:** {std_dev}\n"
    
    # Generate visualization
    generate_viz_diamonds(save_as_image=True)
    
    # Write the markdown report to a file
    with open("diamonds_summary.md", "w", encoding="utf-8") as file:
        file.write("# Diamonds Dataset Summary Report\n\n")
        file.write(markdown_summary)
        file.write("\n\n")
        file.write(markdown_mode)
        file.write("\n\n")
        file.write("## Variance and Standard Deviation:\n")
        file.write(variance_std_markdown)
        file.write("\n\n")
        
        # Visualization
        file.write("## Diamond Price Distribution:\n")
        file.write("![Diamond Price Distribution](diamonds_price_distribution.png)\n")
    
    print("Markdown report saved as 'diamonds_summary.md'.")

if __name__ == '__main__':
    save_diamonds_report_to_markdown()

