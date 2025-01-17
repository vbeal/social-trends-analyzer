import streamlit as st
from data_loader import load_dataset, rename_columns
from visualizations import plot_distribution, plot_scatter, plot_bar

def main():
    # Configuração inicial
    st.set_page_config(page_title="Social Trends Analyzer - Spotify", layout="wide")
    st.title("🎵 Analisador de Tendências Musicais - Spotify")

    # Seleção de datasets
    st.sidebar.title("⚙️ Configurações")
    files = {
        "Alta Popularidade": "data/high_popularity_spotify_data.csv",
        "Baixa Popularidade": "data/low_popularity_spotify_data.csv"
    }
    dataset_choice = st.sidebar.selectbox("Selecione o dataset:", list(files.keys()))
    dataset_path = files[dataset_choice]

    # Carregar e processar o dataset
    try:
        df = load_dataset(dataset_path)
        df = rename_columns(df)

        st.header(f"📊 Visualizando o Dataset: {dataset_choice}")
        st.dataframe(df.head())

        # Gráficos
        st.subheader("⚡ Distribuição da Energia")
        plt = plot_distribution(df, "Energia", "Distribuição da Energia", "Energia", "Frequência", color="green")
        st.pyplot(plt)

        st.subheader("💃 Dançabilidade vs Humor")
        if "Dançabilidade" in df.columns and "Humor" in df.columns:
            plt = plot_scatter(df, "Dançabilidade", "Humor", "Dançabilidade vs Humor", "Dançabilidade", "Humor")
            st.pyplot(plt)

        st.subheader("🎤 Artistas Mais Frequentes")
        if "Artista" in df.columns:
            plt = plot_bar(df, "Artista", "Top 10 Artistas Mais Frequentes", "Artistas", "Quantidade de Músicas")
            st.pyplot(plt)

    except FileNotFoundError as e:
        st.error(e)
    except Exception as e:
        st.error(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()
