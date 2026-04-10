import json

file_path = 'lenet5.ipynb'

with open(file_path, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

markdown_contents = [
    [
        "## Definição da Arquitetura do Modelo\n",
        "Implementação da rede neural convolucional LeNet-5 utilizando PyTorch."
    ],
    [
        "## Extração e Visualização de Filtros\n",
        "Extração dos pesos da camada conv1 para visualização do estado inicial dos filtros."
    ],
    [
        "## Carregamento de Dados\n",
        "Download, transformação em tensores e estruturação do dataset MNIST em lotes para treinamento."
    ],
    [
        "## Geração de Feature Maps\n",
        "Execução do forward pass de uma imagem na camada conv1 para visualização dos mapas de características resultantes."
    ],
    [
        "## Loop de Treinamento\n",
        "Configuração de hiperparâmetros, otimizador, função de custo e execução do treinamento ao longo de múltiplas épocas."
    ],
    [
        "## Avaliação do Modelo\n",
        "Inferência do modelo treinado no conjunto de dados de teste para cálculo da acurácia global."
    ]
]

# We will remove any existing markdown cells just in case to avoid duplicates
cleaned_cells = [cell for cell in notebook['cells'] if cell['cell_type'] != 'markdown']

new_cells = []
md_index = 0

for cell in cleaned_cells:
    if cell['cell_type'] == 'code' and md_index < len(markdown_contents):
        new_cells.append({
            "cell_type": "markdown",
            "metadata": {},
            "source": markdown_contents[md_index]
        })
        md_index += 1
    new_cells.append(cell)

notebook['cells'] = new_cells

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1)
