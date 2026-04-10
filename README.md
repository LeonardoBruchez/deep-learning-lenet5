# Projeto LeNet-5 com PyTorch

Este repositório contém a implementação passo a passo e o treinamento da clássica rede neural convolucional **LeNet-5**. O modelo foi desenvolvido utilizando a linguagem Python com o ecossistema PyTorch e é empregado para resolver o problema de classificação de dígitos manuscritos utilizando a base de dados MNIST.

# 🗂️ NAVEGANDO PELO PROJETO

Diferente de um projeto de software tradicional, o conteúdo principal não está dividido em vários arquivos e módulos, mas centralizado de forma didática e sequencial no arquivo:

* **[`lenet5.ipynb`](./lenet5.ipynb)**: Seu ponto de partida. Trata-se de um Jupyter Notebook que documenta a aplicação da rede neural e as visualizações de dados.

Dentro da pasta do projeto, você também vai encontrar:
* `pyproject.toml` e `uv.lock`: Arquivos do gerenciador de pacotes e dependências em Python, que garantem que as versões do PyTorch, Matplotlib e Torchvision sejam instaladas corretamente usando o `uv`.
* `.venv/`: A pasta equivalente ao ambiente virtual local que isola os pacotes restritos deste projeto.
* `data/`: Diretório criado automaticamente que hospeda os artefatos de dados locais baixados do MNIST.
* `.gitignore` e `main.py`: Arquivos bases para o repositório e execuções alternativas de scripts soltos.

# 🧠 COMO FUNCIONA O CÓDIGO?

O Notebook (`lenet5.ipynb`) atua como um laboratório completo de Machine Learning, documentando a implementação da arquitetura em passos claros. Para que você entenda o que cada "pedaço" do projeto faz:

1. **Definição da Arquitetura do Modelo**: É ali que o modelo matemático toma forma ao herdar da classe `nn.Module`. Mapeamos minuciosamente as camadas Conv2d, as funções de ativação (ReLU) não lineares, e as camadas "fully connected" (Linear).
2. **Visualização de Filtros**: Código dedicado a separar e extrair os pesos da primeira camada `conv1` para entender seus estados não-treinados.
3. **Download e Lotes (DataLoader)**: Utilizando pacotes nativos do formato de pesquisa do MNIST, dividimos os dados em "batches" para alimentar o modelo eficientemente. 
4. **Visualização de Feature Maps**: Uma análise incrível exploratória onde acompanhamos uma imagem através do primeiro estágio algébrico do modelo e visualizamos no que o modelo está prestando atenção.
5. **Loop de Treinamento**: Processo no qual ensinamos as features do MNIST à IA, aplicando inferência progressiva, comparando com o erro final (Loss/Cross Entropy) na propagação pra trás (`backward`) rodando com os benefícios da GPU.
6. **Avaliação (Acurácia Global)**: Fase derradeira de submeter a rede a dados inteiramente novos extraindo a métrica final em porcentagem de precisão percentual (Acurácia >98% tipicamente).

# 🚀 PRÉ-REQUISITOS E CONCEITOS

Para acompanhar as lógicas técnicas aqui apresentadas com tranquilidade, é recomendável que as seguintes disciplinas façam parte da sua jornada:

- **Redes Neurais Convolucionais**: Entender que CNNs resolvem tarefas de visão extraindo atributos por blocos bidimensionais (como janelas de textura num campo receptivo usando "Kernels") diminuindo através de poolings, ao invés de forçar redes totalmente conectadas gigantes na imagem.
- **Ecossistema PyTorch**: Familiaridade em operar em cima dos `Tensors` no ecossistema e executar otimizadores e backpropagation em um loop padrão.
- **Jupyter Notebooks**: Saber navegar os resultados visuais contidos e executar "células" interativas com atalhos base.

# 🛠️ COMO EXECUTAR O REPOSITÓRIO

1. Clone o repositório/baixe a pasta base em sua máquina local.
2. Ative as dependências do ambiente virtual Python (via `uv` ou scripts).
3. Abra o repositório em uma IDE como o **Visual Studio Code** e certifique-se de iniciar o Kernel do Python 3 (fornecido pela instalação da pasta `.venv`).
4. Rode a primeira célula do `lenet5.ipynb`.
