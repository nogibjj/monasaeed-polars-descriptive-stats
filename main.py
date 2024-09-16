import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dataset = sns.load_dataset('diamonds')

def get_summary_statistics():
    return dataset.describe()

def get_mode():
    return dataset.mode().iloc[0]

def get_variance_std():
    variance = dataset['price'].var()
    std_dev = dataset['price'].std()
    return variance, std_dev

def generate_viz_diamonds(save_as_image=True):
    """Generates and optionally saves the diamond price distribution plot."""
    fig, ax = plt.subplots(figsize=(20, 8)) # pylint: disable=unused-variable
    palette = ["#c94727", "#ea5b17", "#e57716", "#f2a324", "#a2c0a6", "#7ac0a8", "#5e9786", "#557260", "#5b5572"]
    prices = np.array(dataset["price"]).flatten()
    
    # Plotting price distribution
    sns.histplot(prices, color=palette[8], kde=True, bins=30, alpha=1, fill=True, edgecolor="black", linewidth=3, ax=ax)
    
    # Set plot title, labels, and scale
    ax.set_title("\nDiamond's Price Distribution\n", fontsize=25)
    ax.set_ylabel("Count", fontsize=20)
    ax.set_xlabel("\nPrice", fontsize=20)
    ax.set_yscale("linear")
    
    sns.despine(left=True, bottom=True)
    
    if save_as_image:
        plt.savefig("diamonds_price_distribution.png")
    
    plt.show()



def save_diamonds_report_to_markdown():
    """Generates a markdown report for the diamonds dataset and saves it to a file."""
    # Call helper functions with the dataset
    summary_df = get_summary_statistics()
    mode_df = pd.DataFrame(get_mode()).T  
    variance, std_dev = get_variance_std()
    
    # Convert to markdown
    markdown_summary = summary_df.to_markdown()
    markdown_mode = mode_df.to_markdown()
    variance_std_markdown = f"**Variance:** {variance}\n\n**Standard Deviation:** {std_dev}\n"
    
    # Generate visualization
    generate_viz_diamonds(save_as_image=True)
    
    # Write the markdown report to a file
    with open("diamonds_summary.md", "w", encoding="utf-8") as file:
        file.write("# Diamonds Dataset Summary Report\n\n")
        file.write("## Summary Statistics:\n")
        file.write(markdown_summary)
        file.write("\n\n")
        file.write("## Mode:\n")
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