import matplotlib.pyplot as plt

def plot_distribution(data, column, title, xlabel, ylabel, color="blue"):
    """
    Gera um histograma para a distribuição de valores em uma coluna.
    """
    plt.figure(figsize=(10, 5))
    plt.hist(data[column], bins=20, color=color, edgecolor='black')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    return plt

def plot_scatter(data, x, y, title, xlabel, ylabel, color="purple"):
    """
    Gera um gráfico de dispersão entre duas variáveis.
    """
    plt.figure(figsize=(10, 5))
    plt.scatter(data[x], data[y], alpha=0.5, color=color)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    return plt

def plot_bar(data, column, title, xlabel, ylabel, top_n=10, color="green"):
    """
    Gera um gráfico de barras para os valores mais frequentes de uma coluna.
    """
    counts = data[column].value_counts().head(top_n)
    plt.figure(figsize=(10, 5))
    counts.plot(kind='bar', color=color, edgecolor='black')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    return plt
