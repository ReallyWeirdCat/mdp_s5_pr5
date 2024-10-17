import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import networkx as nx


def heatmap(matrix):
    """
    matrix - list of lists of floats
    region 5x5,
    temperature range [-10, 40]
    """
    df = pd.DataFrame(matrix)

    plt.figure(figsize=(8, 6))

    sns.heatmap(df, annot=True, cmap='coolwarm', cbar=True,
                vmin=-10, vmax=40)

    plt.title('Тепловая карта')

    plt.show()


def netgraph(graph):
    """
    computer network, 12 nodes
    """
    G = nx.Graph(graph)

    plt.figure(figsize=(10, 8))

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=1800, node_color='lightblue', font_size=10)

    plt.title('Computer Network Graph')

    plt.show()


def main():
    matrix = [[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10],
              [11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25]]
    heatmap(matrix)

    edges = [
        ('router', 'extender'),
        ('extender', 'phone'),
        ('router', 'printer'),
        ('router', 'desktop'),
        ('extender', 'laptop'),
        ('router', 'home server'),
        ('provider', 'router'),
        ('server_1', 'provider'),
        ('server_2', 'provider'),
        ('server_3', 'provider'),
        ('server_4', 'provider'),
        ('server_5', 'provider'),
    ]
    netgraph(edges)


if __name__ == '__main__':
    main()
