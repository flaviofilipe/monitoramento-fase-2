### Minimundo
1. O mini-mundo seja na área de sensoriamento. Exemplo: um programa que realiza o processamento de dados sobre a temperatura corporal de pacientes sendo monitorados ou que consiga realizar cálculos sobre o número de pessoas entrando em um recinto através de várias catracas;
2. O sensoriamento deve ocorrer sobre algum dispositivo claramente definido. Exemplos: sensores de temperatura, sensores de batimentos cardíacos, catracas, etc.;
3. O mini-mundo deve realizar alguma computação sobre valores numéricos. Considerando os exemplos citados, respectivamente, valores de temperatura em celsius e total de pessoas que passaram pelas catracas;
4. O programa do mini-mundo deve gerar automaticamente seus próprios dados para testes. Exemplo: o programa de monitoramento de pacientes deve gerar uma coleção de dados de leituras de temperaturas de cada um dos pacientes, enquanto o programa das catracas pode gerar uma lista de pessoas que entraram pelas catracas.


### Instruções Gerais
- A linguagem escolhida deverá ter suportes a Threads, excluindo as linguagens Javascript e Typtescript
- Fazer captura de tela de até 10 minutos explicando:
  - O tema escolhido e aprovado
  - Como realizar as configuraçãoes iniciais e executar o programa
  - Visualização do resutado de execução
  - Pode ser enviado para o Youtube ou Google Drive
- Suporte até o dia 29/03/2024

## Critérios de aceite
1. Devem ser simulados os monitoramentos de 10 pessoas/equipamentos da forma já especificada durante a primeira avaliação (AVALIAÇÃO I). Exemplo: 10 pacientes ou 10 catracas;
2. As seguintes funcionalidades (funções ou métodos) devem ser implementadas: 
  
   a. Gerar automaticamente (randomicamente) os dados dos sensores para qualquer quantidade N de dispositivos monitorados, 
   
   b. Os dados gerados devem conter, obrigatoriamente, um coluna de identificação tanto para cada objeto, pessoa ou animal sendo monitorado,
   
   c. (c) um método main, principal, tanto na aplicação CLIENTES quanto na aplicação SERVIDOR, a partir do qual todas as funcionalidades possam ser executadas/testadas
   
   d. permitir os seguintes processamentos sobre os dados gerados no passo 2.1:
      - geração randômica de dados dos sensores (simulados) de forma paralelizada, através de Threads ou qualquer outro recurso que permita execução paralelizadas, na razão de UMA Thread por cada um das pessoas/equipamentos monitorados. As Threads serão utilizadas, neste caso, para simular dispositivos remotos capturando e enviando dados sensoriados de pessoas/equipamentos;
      - exemplificar e avaliar DOIS cenários através de programas distintos: 
        - CENÁRIO 1 – uma solução CLIENTE x SERVIDOR, na qual N CLIENTES envia para o SERVIDOR os dados sensoriados e este último deve acumulá-los e processá-los. O processamento deve ocorrer sobre os dados considerando a rotina de maior complexidade desenvolvida durante a AVALIAÇÃO I (ou seja, item d.4 da AVALIAÇÃO I) concentrada inteiramente no SERVIDOR;
        - CENÁRIO 2 – a rotina de maior complexidade deve ser deslocada para os N CLIENTES na BORDA, que devem realizar todo o processamento dos dados sensoriados, “desafogando” o SERVIDOR na NUVEM de uma sobrecarga de processamentos.
            
3. Não podem ser usadas bibliotecas externas ou internas da linguagem para automatizar as impressões, filtragens, ordenações e acumulações pedidas. Ou seja, devem ser criados ou pesquisados e adicionados ao programa códigos completos de todos os algoritmos envolvidos na automação das funcionalidades.

4. Devem ser entregues DUAS versões do código fonte, uma considerando o CENÁRIO 1 e outra considerando o CENÁRIO 2. Os códigos devem estar divididos em DOIS projetos ou DUAS pastas distintas e deve ser possível executar cada um dos CENÁRIOS de forma independente. Para cada cenário, dois programas devem ser entregues, um para representar os N CLIENTES e outro para representar o SERVIDOR;

5. A mudança do código-fonte entre os CENÁRIOS 1 e 2 devem refletir uma tentativa perceptível de melhoria da complexidade do programa através da distribuição do processamento de dados. 
Exemplos: 
  (a) transferir acumulações, filtragens e ordenações do SERVIDOR na NUVEM para os CLIENTES na BORDA
  (b) adição de processamento inteligente que evita o envio e acumulo demasiado de dados dos CLIENTES para o SERVIDOR.

6. O código deve estar comentado. Cada comentário sobre cada método ou função deve informar qual é a complexidade do algoritmo envolvido na operação (ATENÇÃO: utilize a notação Big-O);

7. Durante a captura do vídeo de demonstração, o desenvolvedor deve narrar e demonstrar o uso de todas as funcionalidades, com seus resultados impressos. Além disso, dever ocorrer uma discussão sobre o que muda do CENÁRIO 1 para o CENÁRIO 2. 
  - Quais foram as estratégias utilizadas que permitiram transferir processamento da NUVEM para a BORDA?
  - Quais são as conseqüências de tal mudança para a complexidade geral da solução?