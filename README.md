# TeXcalculator
## Resumo

 O projeto TeXcalculator é um site desenvolvido em Python 3 em conjunto com o framework Flask que receberá entradas do ambiente matemático .tex do LaTeX e realizará cálculos diversos com ele, bem como poderá fazer um preview da entrada em LaTeX escrita pelo usuário.  O programa contará com uma interface amigável até mesmo para quem não tem total domínio da linguagem.

## Motivação
 A motivação vem das várias vezes em que precisei expressar uma linha de raciocínio por meio de equações e não ter um ambiente rápido para compilar e nem calcular elas de forma que fosse clara para todos. Uma grande inspiração foi o  [Symbolab](https://pt.symbolab.com/), que aceita entradas em LaTeX e realiza inúmeros cálculos matemáticos com o auxílio da linguagem **Mathematica**. A ideia seria fazer algo ainda de ainda mais rápido acesso.

## Pré-requisitos

- Distribuição LaTeX ([TeX Live](https://www.tug.org/texlive/), [MiKTeX](https://miktex.org/) ..)
- Python 3
- ANTRL 4 (Parse generator) [LINK](https://www.antlr.org/)
- sympy package
- numpy package
- matplotlib package
- Flask 1.0

## Funcionalidades
Até o momento, a calculadora tem as seguintes funções:

- Preview completo (todo o acervo da linguagem .TeX)
- Soma
- Subtração
- Divisão
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
- [Curso de Flask](https://www.youtube.com/playlist?list=PL3BqW_m3m6a05ALSBW02qDXmfDKIip2KX)

### Como usar o programa (desenvolvimento atual)

#### Entradas
Há um campo de diálogo para o usuário chamado 'input', o qual o usuário deverá entrar com uma string no formato LaTeX sem precisar declarar o ambiente matemático ('$').
#### Escolher operação

Após o usuário fornecer a entrada, basta que ele escolha uma das opções disponíveis nos botões da interface.

- Preview: este botão fará com que o usuário entre com usuário possa visualizar o output do seu código para verificar se escreveu tudo certo. Essa função já está completamente implementada até o presente momento e conta com grande parte dos comandos disponíveis no ambiente matemático LaTeX
- Calcular: este botão faz cálculos de algumas operações do ambiente matemático, que já foram mencionados anteriormente. Até o momento só é possível entrar com strings mais simples porque o Parser que eu estou desenvolvendo no ANTLR 4 ainda não está completamente desenvolvido. Ou seja, pode-se integrar funções complexas se for a única atividade, mas o algoritmo teria dificuldade para integrar funções em forma de fração ou derivada incluídas, por exemplo.

#### Exemplo

##### Preview
|Input|Output  |
|--|--|
| \frac{a}{b} | $\frac{a}{b}$ |
| \int \sin(x)dx|$\int \sin(x)dx$ |

##### Calcular

|Input|Output  |
|--|--|
| \frac{6}{2} | $3$ |
| \int \sin(x)dx|$-\cos(x)$ |



## Fluxograma

![Fluxograma](https://github.com/PEE-2019-ELO-COM/Erick_TeXcalculator/blob/master/Fluxograma_TeXcalculator.png?raw=true)

## Diagrama UML

![Diagrama UML](https://github.com/PEE-2019-ELO-COM/Erick_TeXcalculator/blob/master/UML_texcalculator.png?raw=true)

## Esboço do layout
![Layout do programa feito no Adobe Illustrator](https://github.com/PEE-2019-ELO-COM/Erick_TeXcalculator/blob/master/main_layout.png?raw=true)
