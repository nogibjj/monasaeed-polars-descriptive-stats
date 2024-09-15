import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns

dataset = sns.load_dataset('diamonds')

def get_summary_statistics():
    return dataset.describe()

def get_mode():
    return dataset.mode().iloc[0]

def get_variance_std():
    variance = dataset.var()
    std_dev = dataset.std()
    return pd.DataFrame({'Variance': variance, 'Standard Deviation': std_dev})

def generate_viz_diamonds():
    #df = sns.load_dataset('diamonds')
    plt.subplots(figsize=(20, 8))
    palette = ["#c94727","#ea5b17","#e57716","#f2a324","#a2c0a6","#7ac0a8","#5e9786","#557260","#5b5572"]
    p = sns.histplot(dataset["price"],color=palette[8],kde=True,bins=30,alpha=1,fill=True,edgecolor="black",linewidth=3)
    p.axes.lines[0].set_color("orange")
    p.axes.set_title("\nDiamond's Price Distribution\n",fontsize=25)
    plt.ylabel("Count",fontsize=20)
    plt.xlabel("\nPrice",fontsize=20)
    plt.yscale("linear")
    sns.despine(left=True, bottom=True)
    plt.show()

def generate_summary_report():
    print("Summary Statistics:\n", get_summary_statistics(dataset))
    print("\nMode:\n", get_mode(dataset))
    print("\nVariance and Standard Deviation:\n", get_variance_std(dataset))
    print(f"The Distribution of Prices :", generate_viz_diamonds(dataset))
