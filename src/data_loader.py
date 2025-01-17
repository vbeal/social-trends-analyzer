import pandas as pd

def load_dataset(path):
    """
    Carrega o dataset a partir do caminho fornecido.
    """
    try:
        df = pd.read_csv(path)
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"Erro: O arquivo {path} não foi encontrado.")
    except Exception as e:
        raise Exception(f"Erro ao carregar o dataset: {e}")

def rename_columns(df):
    """
    Renomeia as colunas do dataset para português.
    """
    column_mapping = {
        "energy": "Energia",
        "tempo": "Tempo",
        "danceability": "Dançabilidade",
        "loudness": "Intensidade",
        "valence": "Humor",
        "track_artist": "Artista",
        "time_signature": "Assinatura do Tempo",
        "speechiness": "Proporção de Fala"
    }
    return df.rename(columns=column_mapping)
