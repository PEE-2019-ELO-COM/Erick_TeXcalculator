# TeXcalculator
## Resumo

 O projeto TeXcalculator é uma GUI desenvolvida em Python 3 que recebe entradas do ambiente matemático .tex do LaTeX e realizará cálculos diversos com ele, bem como poderá fazer um preview da entrada em LaTeX escrita pelo usuário. Ideal para quem quer fazer rápida conferência de símbolos matemáticos ou expressar melhor uma ideia/equação. Além disso, também pode auxiliar como consulta rápida nos estudos como uma calculadora avançada que pode ser consultada até mesmo sem internet.

## Motivação
 A motivação vem das várias vezes em que precisei expressar uma linha de raciocínio por meio de equações e não ter um ambiente rápido para compilar e nem calcular elas de forma que fosse clara para todos. Uma grande inspiração foi o  [Symbolab](https://pt.symbolab.com/), que aceita entradas em LaTeX e realiza inúmeros cálculos matemáticos com o auxílio da linguagem **Mathematica**. A ideia seria fazer algo ainda de ainda mais rápido acesso.

## Pré-requisitos

- Distribuição LaTeX ([TeX Live](https://www.tug.org/texlive/), [MiKTeX](https://miktex.org/) ..)
- Python 3
- sympy package
- regular expressions package
- tKinter package
- matplotlib package


## Funcionalidades
Até o momento, a calculadora tem as seguintes funções:

- Preview completo (todo o acervo da linguagem .TeX)
- Soma
- Subtração
- Divisão
- Exponencial
- Log
- Multiplicação
- Integral indefinida
- Derivada


## Turorial rápido

### Conceitos abordados

Os conceitos utilizados foram retirados dos seguintes tutoriais na internet:

- [Consulta de sintaxe Python](https://www.youtube.com/watch?v=N4mEzFDjqtA)
- [Como instalar ANTLR no Windows](https://www.youtube.com/watch?v=p2gIBPz69DM&t=3s)
- [Como usar ANTLR (gerador de compilador)](https://www.youtube.com/watch?v=UIQBavUvmXc&t=1351s)
- [Sympy examples tutorial](http://zetcode.com/python/sympy/)

### Como usar o programa (desenvolvimento atual)

#### Entradas
Há um campo de diálogo para o usuário chamado 'input', o qual o usuário deverá entrar com uma string no formato LaTeX sem precisar declarar o ambiente matemático ('$'). Para usar o programa, basta iniciar o arquivo latex_preview.py, que já está integrado com o código de operações calculator.py. Após isso, a GUI já aparecerá em uma janela separada para que o usuário possa usar.
#### Escolher operação

Após o usuário fornecer a entrada, basta que ele escolha uma das opções disponíveis: preview ou calcular.

- Preview: esta feature faz com que o usuário visualize o output do seu código para verificar se escreveu tudo certo. Essa função já está completamente implementada até o presente momento e conta com grande parte dos comandos disponíveis no ambiente matemático LaTeX. Para utilizar essa feature, o usuário deve entrar com o seu código entre dois pontos antecedido de 'preview'. Ou seja, se quiser visualizar o preview de 'a+b', o código de entrada deve ser **preview: a+b :**  
- Calcular: esta feature faz cálculos de algumas operações do ambiente matemático, que já foram mencionados anteriormente. O código já está implementado com as operações que foram descritas anteriormente. Para usar, bsta entrar a equação que deseja calcular diretamente na GUI.

#### Exemplo

Fotos de exemplos tanto da feature preview quanto da 'calcular' foram adicionadas ao repositório e podem ser acessadas como exemplo pelo seguinte [LINK](https://github.com/PEE-2019-ELO-COM/Erick_TeXcalculator/tree/master/imagens). Abaixo seguem alguns prints do funcionamento do código.

##### Preview

![preview_2](https://github.com/PEE-2019-ELO-COM/Erick_TeXcalculator/blob/master/imagens/preview_eq2.png?raw=true)

![preview_1](https://github.com/PEE-2019-ELO-COM/Erick_TeXcalculator/blob/master/imagens/preview_eq3.png?raw=true)

##### Calcular

![Simplificação](https://github.com/PEE-2019-ELO-COM/Erick_TeXcalculator/blob/master/imagens/calc_eq4.png?raw=true)

![Integral indefinida](https://github.com/PEE-2019-ELO-COM/Erick_TeXcalculator/blob/master/imagens/calc_eq2.png?raw=true)

## Fluxograma

![Fluxograma](https://github.com/PEE-2019-ELO-COM/Erick_TeXcalculator/blob/master/Fluxograma_TeXcalculator.png?raw=true)

## Diagrama UML

![Diagrama UML](https://github.com/PEE-2019-ELO-COM/Erick_TeXcalculator/blob/master/UML_texcalculator.png?raw=true)

## Futuras implementações

### Aprimoramento da GUI (esboço GUI)
O código cumpriu o seu propósito e agora o próximo passo é tornar a interface mais amigável por meiod e adição de atalhos de forma que iniciantes e leigos em LaTeX possam também usufruir da ferramenta ao máximo.
![Layout do programa feito no Adobe Illustrator](https://github.com/PEE-2019-ELO-COM/Erick_TeXcalculator/blob/master/main_layout.png?raw=true)

### Incluir mais funções

É desejável que em uma futura atualização sejam implementadas mais operações ao repertório da calculadora tais como operações vetoriais/ matriciais.

### Desenvolver um compilador

Tendo em vista o tamanho da síntaxe da linguagem LaTeX, que não existe um tradutor completo o suficiente que faça LaTeX -> Python e nem o contrário. No entanto, existem alguns já muito bons como os utilizados pelo site Symbolab (citado acima) e WolframAlpha (este até mesmo desenvolveu uma linguagem para abrangir inicalmente este propósito). A ideia seria abranger as possibilidades ao criar um compilador que simule um Parser confiávelLaTeX -> Python para as operações mais comuns. O código que foi desenvolvido, para atualmente para este projeto, foi todo feito por meio de manipulaçãp de strings.

