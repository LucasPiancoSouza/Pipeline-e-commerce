#Biblioteca python para trabalhar com caminhos de pastas,
#o pathlib ele representa caminhos como objetos
from pathlib import Path
import pandas as pd

PASTA_DADOS = Path("data/raw")

#O nome das coisas deve explicar a sua responsabilidade
def encontrar_arquivos_csv(pasta:Path) -> list[Path]:
    #pasta:Path - espera receber um objeto Path
    #list[Path] - esta função retorna uma lista de objetos Path
    return list(pasta.glob("*.csv"))

def carregar_csvs(arquivos: list[Path]) -> tuple[ dict[str, pd.DataFrame],dict[Path, str]]:

    erros: dict[Path, str] = {}
    dataframes: dict[str, pd.DataFrame] = {} 

    for arquivo in arquivos:
# Tenta carregar o arquivo CSV
        nome = arquivo.stem
        nome = nome.replace("olist_", "")
        nome = nome.replace("_dataset", "")
        try:
            df = pd.read_csv(arquivo)
            dataframes[nome] = df

# Caso ocorra algum erro durante a leitura, registra o erro
        except Exception as erro:
            erros[arquivo] = str(erro) 

    return dataframes, erros

def relatorio_dataframe(dataframes: dict[str, pd.DataFrame]):
    for nome, df in dataframes.items():
        linhas, colunas = df.shape
        print(f"""
================================
Tabela: {nome}
================================

Linhas: {linhas}
Colunas: {colunas}

Valores Nulos: 
{df.isnull().sum()}

Tipos das colunas: 
{df.dtypes}


""")