import seaborn as sns
import polars as pl
import numpy as np
import matplotlib.pyplot as plt


diamonds = sns.load_dataset('diamonds')
df = pl.DataFrame(diamonds)

def get_descriptive_statistics(column_name):
    """
    Returns mean, median, variance, and standard deviation for a given column in the dataset.
    """
    mean = df[column_name].mean()
    median = df[column_name].median()
    variance = df[column_name].var()
    std_dev = df[column_name].std()
    
    return {
        'mean': mean,
        'median': median,
        'variance': variance,
        'std_dev': std_dev
    }

def generate_carat_price_scatter_plot(save_as_image=False):
    # Extract carat and price columns as lists using Polars
    carat = df["carat"].to_list()
    price = df["price"].to_list()
    
    # Generate scatter plot using matplotlib
    plt.scatter(carat, price, alpha=0.5)
    plt.title("Carat vs Price Scatter Plot")
    plt.xlabel("Carat")
    plt.ylabel("Price")
    
    # Save the plot as a PNG image if requested
    if save_as_image:
        plt.savefig("carat_price_scatter_plot.png")
        print("Plot saved as carat_price_scatter_plot.png")
    
    # Show the plot
    plt.show()

def get_summary_statistics():
    pandas_df = df.to_pandas()
    desc_stats = pandas_df.describe()
    mode_df = pandas_df.mode().iloc[0]

    # Prepare summary statistics as markdown
    markdown_summary = "## Diamonds Dataset Summary Statistics\n\n"
    markdown_summary += "### Descriptive Statistics:\n\n"
    markdown_summary += desc_stats.to_markdown() + "\n\n"
    markdown_summary += "### Mode of Each Column:\n\n"
    markdown_summary += mode_df.to_markdown() + "\n"

    return markdown_summary

# Function to save summary report to a markdown file
def save_summary_report_to_markdown():
    # Generate scatter plot and save as .png
    generate_carat_price_scatter_plot(save_as_image=True)

    # Get summary statistics in markdown format
    markdown_summary = get_summary_statistics()

    # Add the image to the markdown report
    markdown_summary += "\n## Carat vs Price Scatter Plot\n"
    markdown_summary += "![Carat vs Price Scatter Plot](carat_price_scatter_plot.png)\n"

    # Save the report to a markdown file
    with open("diamonds_summary_report.md", "w") as f:
        f.write(markdown_summary)

    print("Summary report saved as diamonds_summary_report.md")

if __name__ == "__main__":
    stats = get_descriptive_statistics('price')
    generate_carat_price_scatter_plot(save_as_image=True)
    save_summary_report_to_markdown()
