### Minimundo
Considerando 10 plantações ou 10 áreas de cultivo diferentes em uma plantação, é necessário o monitoramento da umidade dos solos para gerar informações sobre suas temperaturas. A temperatura ideal para a semeadura é entre 20º e 30º, tendo em média 25º. 
Deverá ser informado como aviso as temperaturas entre 25 e 30 graus e emitir um alerta acima de 30º. A entrada poderá ser feita através de um sensor de umidade, mas será simulado para este projeto.


## Requisitos
**Item 1**

[ ] Simular 10 objetos

**Item 2**

[ ] Item 2a - Criar uma função O(N)

[ ] Item 2b - coluna de identificação

[x] Item 2c - Método main (cliente e servidor)

**Item 2d**

[ ] Item 2d.1 - Geração randômica de dados dos sensores de forma paralela. Uma thread para cada dispositivo/pessoa simulada.

### Exemplificar os cenários:

**Cenário 1**
[ ] Transferir o item de maior complexidade da atividade anterior (item d.4) para o servidor;

[ ] N clientes envia para o servidor dados sensoriados e este último deverá processa-los;

**Cenário 2**
[ ] A rotina de maior complexidade deve ser deslocada para os N CLIENTES na BORDA, que devem realizar todo o processamento dos dados sensoriados.


**Item 3**

[ ] Não utilizar bibliotecas internas ou internas para automatizar o processo

**Item 4**

[ ] Entregar duas versões do código: Client & Server.
**Item 5**

[ ] Garantir perceptível melhoria da complexidade com a distribuição do processamento.

**Item 6**

[ ] Comentar o código utlizando a notação Big-O.

**Item 7**

[ ] Gravar vídeo
  - Quais foram as estratégias utilizadas que permitiram transferir processamento da NUVEM para a BORDA?
  - Quais são as conseqüências de tal mudança para a complexidade geral da solução?
