# Análise valor Dólar Real por Presidentes

Nesse projeto desenvolvemos uma visualização baseada no curso [Storytelling Data Visualization on Exchange Rates](www.dataquest.io). Nela selecionamos o valor Dólar-Real de 1996 até maio de 2022, apontando as crises que ocorreram ao longo do tempo e também os presidentes no período.
## Dados
Os dados do Dólar foram coletados no Portal Brasileiro de Dados Abertos e as informações destacadas foram coletadas na Wikipedia.
O data set com os dados possue informações do valor que o dólar foi fechado em cada dia, contudo para melhorar a visualização optamos por fazer a média mensal desses valores e suavizamos o gráfico utlizando o método `rolling(3)`. Após isso selecionamos os períodos dos presidentes que foram:
- Fernando Henrique Cardoso de 01/1995 até 01/2003;
- Lula                      de 01/2003 até 01/2011;
- Dilma Rousseff            de 01/2011 até 08/2016;
- Michel Temer              de 08/2016 até 01/2019;
- Jair Bolsonaro            de 01/2019 até 05/2022.

## Visualização
a visualização consiste em gráficos de linhas que representam o valor do dolár temporalmente, eles são divididos em cores cada cor se refere ao presidente daquele período, alguns presidentes possuem pouco tempo de mandato o que acabou dificultando a organização da figura. Além dissos a figura dispõe de algumas linhas verticais e cada cor representa o início de uma crise no Brasil de acordo com [Lista de crises econômicas no Brasil](https://pt.wikipedia.org/wiki/Lista_de_crises_econ%C3%B4micas_no_Brasil).