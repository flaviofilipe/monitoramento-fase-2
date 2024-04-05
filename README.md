### Minimundo
Considerando 10 plantações ou 10 áreas de cultivo diferentes em uma plantação, é necessário o monitoramento da umidade dos solos para gerar informações sobre suas temperaturas. A temperatura ideal para a semeadura é entre 20º e 30º, tendo em média 25º. 
Deverá ser informado como aviso as temperaturas entre 25 e 30 graus e emitir um alerta acima de 30º. A entrada poderá ser feita através de um sensor de umidade, mas será simulado para este projeto.


## Requisitos
**Item 1**

[X] Simular 10 objetos: `main.leitura_das_plantacoes`

**Item 2**

[X] Item 2a - Criar uma função O(N): `src.sensores.sensoriamento.gerar`

[X] Item 2b - coluna de identificação: `src.models.Temperatura`

[X] Item 2c - Método main: `main.main`

**Item 2d**

[X] Item 2d.1 - Imprimir a lista de plantações: `src.operacoes.imprimir_plantacao`

[X] Item 2d.2 - Imprimir a lista de letura por cada objeto: `src.operacoes.imprimir_temperatura`

[X] Item 2d.3 - Ordernação crescente: `src.operacoes.sort_temperaturas`

[X] Item 2d.4 - Adicionar uma complexidade O(N^3): `src.operacoes.imprimir_status`

**Item 3**

[X] Não utilizar bibliotecas internas ou internas para automatizar o processo

**Item 4**

[X] Funcionalidade 4.4 diferente dos itens 4.1, 4.2, 4.3

**Item 5**

[X] Comentar o código utilizando a notação Big-O

**Item 6**

[X] Ao comentar o código da funcionalidade 4.4, deve ser adicionada uma observação sobre se é possível que o algoritmo gere alguma situação de necessidade de processamento via brute force (força bruta). O comentário deve descrever qual(is) é(são) a(s) situação(ões);

**Item 7**

[ ] Gravar o vídeo demostrando as funcionalidades, resultados impressos e explicar a classe de complexidade de cada uma.


# Sobre

O intuíto deste projeto é demonstrar as complexidades de cada função utilizando as notações Big-O. Para isto, no arquivo `src.operacoes.py` estará as funções python demonstrando cada complexidade e uma breve explicação de como ela está sendo utilizada.

Neste projeto simularemos o monitoramento da temperatura de N Plantações. Para cada plantação teremos X leituras de temparaturas na qual utilizaremos para fazer nossos testes e análises.

Portanto, uma leitura de uma plantação teremos a *Plantação { nome }* e *Temperatura { value }*. Elas irão compor juntas uma lista de [(Plantação, temperatura)], classificada internamente como uma tupla nomeda = PlantacaoTemperatura (`src/operacoes.py`).

### Requisitos
- Python3.9+

## Organização
- main.py: Arquivo principal para executar a aplicação.
- src/ : está todo código da aplicação
- src/domain : Se encontra o domínio da aplicação, como os models e interfaces
- src/sensores : Para simular a entrada de dados através de sensores foi necessário **gerar** os dados através do método `src/sensores/sensoriamento/gerar()`. Já na classe `src/sensores/temperatura/SensorTemperatura`, nós podemos simular o sensor, no qual captura a temperatura atual. Para esta simulação, os valores são criados aleatóriamente utilizando a função `get_mock_temperatura()` neste mesmo arquivo.
- src/models.py : Aqui está as classes utilizadas para montar os objetos referente às plantações e temperaturas.
- src/operacoes.py : Aqui está todas as implementações das funções responsáveis por processar os dados recebidos pelos sensores.


## Execução

Para executar a aplicação basta executar o arquivo `main.py`:

    `python3  main.py`

Será impresso no terminal a saída das funções utilizadas e o tempo final de execução.

Para testar com mais valores, poderá ser passado por parâmetro para a função `leitura_das_plantacoes(quant_pantacoes=X, quant_leituras=Y)`. O primeiro parâmetro será a quantidade de plantações monitoradas e o segundo a quantidade de leitura vindas do sensor.

As seguintes funções serão executadas:

    fase_1_plantacoes(plantacoes)
    fase_2_temperaturas_desordenadas(plantacoes)
    fase_2_1_temperaturas_ordenadas(plantacoes)
    fase_3_status(plantacoes)

Para visualizar a saída e o tempo de execução apenas de uma delas, as outras poderão ser comentadas:

    fase_1_plantacoes(plantacoes)
    # fase_2_temperaturas_desordenadas(plantacoes)
    # fase_2_1_temperaturas_ordenadas(plantacoes)
    # fase_3_status(plantacoes)

