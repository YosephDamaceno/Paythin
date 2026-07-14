# Projeto Paynthin

## Equipe

**Nome da equipe:**  NordesteCoders

**Integrantes:**

- Yoseph dos Santos Damaceno
- Jayk Abreu de Santana Santos
- Luciano Davi Martins de Santana Silva

## Descrição do Sistema
O **Paythin** é um software de desenho desenvolvido em Python com interface gráfica (Tkinter), 
estruturado segundo o padrão de arquitetura **MVC (Model-View-Controller)**. 

Ele permite ao usuário desenhar diversas formas geométricas — linha, rabisco (traço livre), 
retângulo, oval, círculo, triângulo, pentágono e hexágono — diretamente em um canvas, escolhendo 
a cor da borda e do preenchimento de cada figura.

- **Model** (`model/classes.py`): define a classe base `Figura` e suas subclasses (uma para cada 
  forma geométrica), além da classe `Desenho`, responsável por gerenciar a coleção de figuras 
  desenhadas.
- **View** (`View/view.py`): monta a interface gráfica (janela, canvas, menus e botões de seleção 
  de cor) usando Tkinter.
- **Controller** (`Controller/controller.py`): captura os eventos do mouse no canvas (clique, 
  arraste e soltar) e coordena as atualizações entre a View e o Model.

O sistema também conta com **persistência de dados**: os desenhos podem ser salvos e carregados 
em formato **JSON**, através das opções **"Salvar"** e **"Abrir"** no menu **Arquivo**.

## Dados da documentação 
- **Número de classes documentadas:**  
- **Número de metódos documentados:**

## Como Visualizar a Documentação
A documentação HTML do sistema já foi gerada com a ferramenta **Pydoc** e está disponível nos arquivos:
- `Paynthin.model.classes.html`
- `Paynthin.View.view.html`
- `Paynthin.Controller.controller.html`

Para visualizar:
1. Localize os arquivos `.html` mencionados acima na pasta do projeto.
2. Dê duplo clique em qualquer um deles (ou clique com o botão direito → "Abrir com" → seu navegador de preferência).
3. A documentação será exibida no navegador, mostrando as classes, métodos e docstrings de cada módulo.

