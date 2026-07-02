# Pipeline e-commerce

## Objetivo do projeto

Este projeto tem como objetivo construir um pipeline de dados para processar, transformar e armazenar informações de e-commerce em um fluxo organizado e reutilizável. A ideia é reunir dados brutos, aplicar transformações, preparar a base para análises e, futuramente, apoiar dashboards e relatórios de negócio.

## Tecnologias utilizadas

As tecnologias previstas e/ou utilizadas neste projeto incluem:

- Python para ingestão e processamento dos dados
- Pandas para manipulação e transformação de datasets
- SQL para modelagem e consultas no banco de dados
- PostgreSQL como banco de dados relacional
- Docker e Docker Compose para facilitar a execução do ambiente
- Git/GitHub para versionamento do projeto

## Arquitetura do pipeline

A arquitetura proposta para o pipeline segue o fluxo abaixo:

1. Coleta de dados brutos
   - Os dados são armazenados na pasta data/raw.
2. Processamento e transformação
   - Scripts em Python realizam limpeza, normalização e enriquecimento dos dados.
3. Armazenamento estruturado
   - Os dados processados são salvos em arquivos intermediários ou carregados em um banco de dados relacional.
4. Consultas e análise
   - Arquivos SQL podem ser usados para criar tabelas, views e consultas analíticas.

Em uma versão mais completa, esse fluxo pode evoluir para incluir automação, agendamento e orquestração de jobs.

## Estrutura de pastas

```text
Pipeline-e-commerce/
├── data/
│   ├── raw/              # dados brutos
│   └── processed/        # dados processados
├── sql/                  # scripts SQL
├── src/                  # scripts Python e lógica do pipeline
├── docker-compose.yml    # configuração do ambiente com containers
├── Dockerfile            # imagem do projeto
├── requirements.txt      # dependências Python
└── README.md             # documentação do projeto
```

## Como executar o projeto

Como o projeto ainda está em desenvolvimento, a execução pode variar conforme as partes forem sendo implementadas. A seguir, há um fluxo básico para rodar o ambiente localmente:

### 1. Clonar o repositório

```bash
git clone <url-do-repositorio>
cd Pipeline-e-commerce
```

### 2. Criar e ativar o ambiente virtual

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Subir os containers (quando a configuração estiver pronta)

```bash
docker-compose up -d
```

### 5. Executar os scripts do pipeline

Os scripts Python localizados em src/ podem ser executados conforme a implementação for adicionada ao projeto.

> Observação: algumas funcionalidades podem ainda estar em fase de implementação, então o fluxo completo pode exigir adaptações conforme o desenvolvimento avançar.

## Próximos passos

- Implementar a ingestão dos dados brutos
- Criar os scripts de transformação
- Definir o modelo de dados no banco
- Automatizar a execução do pipeline
- Adicionar testes e documentação complementar
