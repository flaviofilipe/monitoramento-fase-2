# Minimundo
Considerando 10 plantações ou 10 áreas de cultivo diferentes em uma plantação, é necessário o monitoramento da umidade dos solos para gerar informações sobre suas temperaturas. A temperatura ideal para a semeadura é entre 20º e 30º, tendo em média 25º. 
Deverá ser informado como aviso as temperaturas entre 25 e 30 graus e emitir um alerta acima de 30º. A entrada poderá ser feita através de um sensor de umidade, mas será simulado para este projeto.

# Instalação

**Criação do ambiente virtual**
```
   python -m venv venv
```

**Ativação do ambiente virtual no Unix**
```
   source venv/bin/activate
```

**Ativação do ambiente virtual no Windows**
```
   ./venv/Scripts/Activate
```

**Instalação das bibliotecas**
```
   pip install -r requirements.txt
``` 

# Execução

## Cenário 01

**Iniciar Servidor**

```
   python cenario01/server/client_server.py
```

**Executar cliente**
```
   python cenario01/main_client.py
```

## Cenário 02

**Iniciar Servidor**

```
   python cenario02/server/client_server.py
```

**Executar cliente**
```
   python cenario02/main_client.py
```


## Requisitos
**Item 1**

[x] Simular 10 objetos

**Item 2**

[x] Item 2a - Criar uma função O(N)

[x] Item 2b - coluna de identificação

[x] Item 2c - Método main (cliente e servidor)

**Item 2d**

[x] Item 2d.1 - Geração randômica de dados dos sensores de forma paralela. Uma thread para cada dispositivo/pessoa simulada.

### Exemplificar os cenários:

**Cenário 1**
[x] Transferir o item de maior complexidade da atividade anterior (item d.4) para o servidor;

[x] N clientes envia para o servidor dados sensoriados e este último deverá processa-los;

**Cenário 2**
[x] A rotina de maior complexidade deve ser deslocada para os N CLIENTES na BORDA, que devem realizar todo o processamento dos dados sensoriados.


**Item 3**

[x] Não utilizar bibliotecas internas ou internas para automatizar o processo

**Item 4**

[x] Entregar duas versões do código: Client & Server.
**Item 5**

[X] Garantir perceptível melhoria da complexidade com a distribuição do processamento.

Resposta:

Sim, é possível perceber uma melhoria significativa na complexidade do sistema ao mover o processamento de dados do servidor para os clientes, distribuindo a carga de trabalho. Vamos analisar como isso impacta a complexidade computacional nos dois cenários.

### Cenário 1: Processamento no Servidor

No Cenário 1, o servidor recebe dados brutos de múltiplos clientes e realiza todo o processamento, o que inclui acumulação, filtragem e categorização dos dados sensoriados. A complexidade de processamento está concentrada no servidor, o que pode levar a um aumento exponencial da carga de trabalho à medida que o número de clientes e leituras de sensores aumenta.

#### Complexidade no Servidor:

1. **Recepção de Dados:**
   - O servidor recebe dados de múltiplos clientes. 
   - Complexidade: O(N), onde N é o número total de leituras enviadas por todos os clientes.

2. **Processamento de Dados:**
   - O servidor processa cada leitura para determinar a categoria/região.
   - Complexidade: O(N * M), onde M é o número de regiões.

#### Resumo de Complexidade:
- **Total Complexidade no Servidor:** O(N * M)

### Cenário 2: Processamento nos Clientes

No Cenário 2, cada cliente realiza o processamento dos dados sensoriados localmente antes de enviá-los ao servidor. O servidor agora apenas armazena e gerencia os dados já processados, reduzindo significativamente a carga de trabalho e complexidade.

#### Complexidade nos Clientes:

1. **Geração de Dados:**
   - Cada cliente gera leituras de sensores.
   - Complexidade: O(K), onde K é o número de leituras geradas por cada cliente.

2. **Processamento Local de Dados:**
   - Cada cliente processa suas próprias leituras para determinar a categoria/região.
   - Complexidade: O(K * M) por cliente.

3. **Envio de Dados Processados:**
   - Cada cliente envia dados processados ao servidor.
   - Complexidade: O(K) por cliente.

#### Complexidade no Servidor:

1. **Recepção de Dados Processados:**
   - O servidor recebe dados processados de múltiplos clientes.
   - Complexidade: O(N), onde N é o número total de leituras enviadas por todos os clientes.

#### Resumo de Complexidade:

- **Total Complexidade em cada Cliente:** O(K * M)
- **Total Complexidade no Servidor:** O(N)

### Comparação de Melhoria de Complexidade

- **Cenário 1 (Servidor):** O(N * M)
- **Cenário 2 (Clientes e Servidor):**
  - Clientes: O(K * M) por cliente
  - Servidor: O(N)

Ao distribuir o processamento para os clientes, a carga de trabalho no servidor é significativamente reduzida. Cada cliente processa seus próprios dados localmente, e o servidor apenas gerencia a recepção e armazenamento dos dados processados, resultando em uma complexidade linear em relação ao número de leituras recebidas.

### Conclusão

- **Melhoria de Complexidade:** A mudança do processamento para os clientes distribui a carga de trabalho, resultando em uma complexidade mais gerenciável e escalável. O servidor não precisa mais realizar operações pesadas de processamento, o que alivia sua carga e melhora a eficiência do sistema como um todo.
- **Vantagens Adicionais:** Além da melhoria de complexidade, essa abordagem também reduz a latência e a dependência da conectividade constante, uma vez que os clientes podem operar de forma mais independente.

Essa distribuição de processamento reflete uma tentativa perceptível de melhorar a complexidade do programa, alinhando-se com os exemplos fornecidos, como a transferência de acumulações e filtragens para os clientes.

**Item 6**

[x] Comentar o código utlizando a notação Big-O.

**Item 7**

[ ] Gravar vídeo
  - Quais foram as estratégias utilizadas que permitiram transferir processamento da NUVEM para a BORDA?
  - Quais são as conseqüências de tal mudança para a complexidade geral da solução?

Resposta:

### Quais foram as estratégias utilizadas que permitiram transferir processamento da NUVEM para a BORDA?

1. **Processamento Local dos Dados:**
   - **Estratégia:** O processamento dos dados sensoriados foi deslocado do servidor (na nuvem) para os clientes (na borda). Cada cliente agora é responsável por processar seus próprios dados antes de enviá-los ao servidor.
   - **Implementação:** A função de processamento, que anteriormente categorizava as leituras de temperatura no servidor, foi movida para os clientes. Isso envolveu a criação de uma função `processar_dados` que realiza a categorização das leituras de temperatura localmente em cada cliente.

2. **Redução de Dados Enviados ao Servidor:**
   - **Estratégia:** Em vez de enviar todas as leituras brutas de temperatura para o servidor, os clientes agora enviam apenas os dados já processados, o que reduz a quantidade de dados transmitidos e a necessidade de processamento no servidor.
   - **Implementação:** A função `enviar_dados` foi adaptada para enviar os dados processados, categorizados por região, ao invés das leituras brutas de temperatura.

3. **Distribuição de Tarefas Computacionais:**
   - **Estratégia:** A carga de trabalho foi distribuída entre vários clientes, diminuindo a sobrecarga em um único ponto (o servidor). Isso aproveita a capacidade de processamento de múltiplos dispositivos, melhorando a escalabilidade e a resiliência do sistema.
   - **Implementação:** Cada cliente agora executa a lógica de processamento localmente, usando a função `leitura_das_plantacoes` para gerar e processar os dados, e `enviar_dados` para transmitir os resultados processados ao servidor.

### Quais são as consequências de tal mudança para a complexidade geral da solução?

1. **Redução da Complexidade no Servidor:**
   - **Antes:** No Cenário 1, o servidor precisava processar todas as leituras brutas recebidas de todos os clientes, resultando em uma complexidade de O(N * M), onde N é o número de leituras e M é o número de categorias/regiões.
   - **Depois:** No Cenário 2, o servidor apenas armazena os dados processados, resultando em uma complexidade de O(N), onde N é o número de leituras processadas recebidas dos clientes.

2. **Aumento da Complexidade nos Clientes:**
   - **Antes:** No Cenário 1, os clientes apenas geravam e enviavam dados brutos, com uma complexidade de O(K) por cliente, onde K é o número de leituras geradas por cliente.
   - **Depois:** No Cenário 2, os clientes geram, processam e enviam os dados, aumentando a complexidade para O(K * M) por cliente.

3. **Distribuição de Carga:**
   - **Consequência Positiva:** A carga de processamento é distribuída entre todos os clientes, reduzindo o gargalo no servidor. Isso permite que o sistema escale melhor com o aumento do número de clientes e leituras de sensores.
   - **Conseqüência Negativa:** Cada cliente precisa ter capacidade computacional suficiente para processar seus próprios dados, o que pode ser uma limitação em dispositivos com recursos limitados.

4. **Redução de Latência e Uso de Banda:**
   - **Consequência Positiva:** Menos dados brutos são enviados pela rede, pois os dados são processados localmente e somente os resultados são enviados. Isso reduz o uso de banda e potencialmente a latência da comunicação entre clientes e servidor.
   - **Conseqüência Negativa:** Pode haver uma pequena latência adicional no lado do cliente devido ao tempo necessário para processar os dados localmente antes de enviá-los.

### Resumo

As estratégias utilizadas envolvem a transferência do processamento de dados do servidor para os clientes, resultando em uma redução significativa da complexidade computacional no servidor (de O(N * M) para O(N)) e uma redistribuição da complexidade para os clientes (de O(K) para O(K * M)). Essa mudança melhora a escalabilidade do sistema e reduz a sobrecarga do servidor, ao mesmo tempo que potencialmente aumenta a carga computacional nos clientes.