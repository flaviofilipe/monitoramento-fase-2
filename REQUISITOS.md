### Minimundo
1. O mini-mundo seja na área de sensoriamento. Exemplo: um programa que realiza o processamento de dados sobre a
temperatura corporal de pacientes sendo monitorados ou que consiga realizar cálculos sobre o número de pessoas
entrando em um recinto através de várias catracas;
2. O sensoriamento deve ocorrer sobre algum dispositivo claramente definido. Exemplos: sensores de temperatura, sensores
de batimentos cardíacos, catracas, etc.;
3. O mini-mundo deve realizar alguma computação sobre valores numéricos. Considerando os exemplos citados,
respectivamente, valores de temperatura em celsius e total de pessoas que passaram pelas catracas;
4. O programa do mini-mundo deve gerar automaticamente seus próprios dados para testes. Exemplo: o programa de
monitoramento de pacientes deve gerar uma coleção de dados de leituras de temperaturas de cada um dos pacientes,
enquanto o programa das catracas pode gerar uma lista de pessoas que entraram pelas catracas.


### Instruções Gerais
- A linguagem escolhida deverá ter suportes a Threads, excluindo as linguagens Javascript e Typtescript
- Fazer captura de tela de até 10 minutos explicando:
  - O tema escolhido e aprovado
  - Como realizar as configuraçãoes iniciais e executar o programa
  - Visualização do resutado de execução
  - Pode ser enviado para o Youtube ou Google Drive
- Suporte até o dia 29/03/2024

## Critérios de aceite
1. Devem ser simulados os monitoramentos de 10 objetos, pessoas ou animais com seus respectivos dispositivos/equipamentos. Exemplo: sensores de batimentos de 10 pacientes ou 10 catracas;
2. As seguintes funcionalidades (funções ou métodos) devem ser implementadas: 
  
   a. Gerar automaticamente (randomicamente) os dados dos sensores para qualquer quantidade N de dispositivos monitorados, 
   
   b. Os dados gerados devem conter, obrigatoriamente, um coluna de identificação tanto para cada objeto, pessoa ou animal sendo monitorado,
   
   c. Um método main, principal, a partir do qual todas as funcionalidades possam ser executadas/testadas, 
   
   d. permitir os seguintes processamentos sobre os dados gerados no passo 2.1:
      - imprimir a lista de objetos, pessoas ou animais sobre os quais ocorre o monitoramento;
      - imprimir a lista das leituras por cada objeto, pessoa ou animal sobre o qual ocorre o monitoramento. 
            
      **ATENÇÃO:** deve ficar claro quais leituras pertencem a cada um;

      - ordenação crescente dos dados considerando os valores lidos dos sensores para cada coisa monitorada;
      - deve ser adicionada, a **critério do desenvolvedor**, uma funcionalidade extra, relativa ao mini-mundo escolhido, cuja complexidade seja ou **O(N^3)** ou **O(2^N)** ou **O(N!)**.
        
        **ATENÇÃO:** a funcionalidade de “busca de padrão” ilustrada no exemplo da sala de aula NÃO pode ser repetida no seu programa.
        
3. Não podem ser usadas bibliotecas externas ou internas da linguagem para automatizar as impressões, filtragens, ordenações e acumulações pedidas. Ou seja, devem ser criados ou pesquisados e adicionados ao programa códigos completos de todos os algoritmos envolvidos na automação das funcionalidades 4.1, 4.2, 4.3 e 4.4 acima;

4. Especificamente, para a funcionalidade, 4.4, deve ser pesquisado ou desenvolvido um algoritmo completamente diferente dos que foram criados para os itens, 4.1, 4.2 e 4.3;

5. O código deve estar comentado. Cada comentário sobre cada método ou função deve informar qual é a complexidade do algoritmo envolvido na operação (ATENÇÃO: utilize a notação Big-O). Além de informar qual é a complexidade, deve dizer a razão, ou justificativa, de ser aquela complexidade e informar também quais são as consequências da complexidade para o código caso a entrada de dados seja muito grande;

6. Ao comentar o código da funcionalidade 4.4, deve ser adicionada uma observação sobre se é possível que o algoritmo gere alguma situação de necessidade de processamento via brute force (força bruta). O comentário deve descrever qual(is) é(são) a(s) situação(ões);

7. Durante a captura do vídeo de demonstração, o desenvolvedor deve narrar e demonstrar o uso de todas as funcionalidades, com seus resultados impressos, e explicar qual é a classe de complexidade de cada uma.