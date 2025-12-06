import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


def generate_heatmap(all_results: list[dict]):
    df = pd.DataFrame(all_results)  # rows = documents, cols = fields with 0/1
    sns.heatmap(df, annot=True, cmap="Reds", linewidths=.5)
    plt.title("LLM Field-Level Error Heatmap")
    plt.savefig("C:\\Users\\Madalina Diaconu\\PycharmProjects\\contract-extraction-pipeline\\src\\evaluation\\results\\heatmap.png")
    plt.close()
