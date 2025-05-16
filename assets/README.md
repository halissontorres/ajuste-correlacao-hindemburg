# Correção de Correlação com Restrição de Faixa — Fórmula HM

## 📈 Exemplos de Gráficos

- Círculos azuis representam a amostra restrita (altura < 1,20 m).
- Círculos cinzas representam a população total.

> O título compara:

- Correlação observada na amostra restrita;
- Correção HM aplicada;
- Correlação real com todos os dados.

![correlation.png](correlation.png)

## 🧪 A correlação estabelece:

- Se há relação: uma variável tende a aumentar quando a outra aumenta?
- Quão forte é essa relação
- Se é positiva ou negativa

### 1. Pontos cinzas (População Total)

- Representam todas as 500 crianças simuladas, com alturas entre aproximadamente 1.0 m e 2.0 m.
  - A correlação entre altura e pé nessa população foi:

    - Correlação real = ~0,97
    - Isso indica uma relação fortemente positiva: quanto maior a altura, maior o pé. É o que esperamos fisiologicamente.

### 2. Pontos azuis (Amostra Restrita - altura < 1,20 m)

- Crianças menores.
  - Como a variação de altura e de pé é pequena nesse grupo, a dispersão dos dados aparenta ser mais aleatória.
  - A correlação observada foi:
  - r_obs = ~0.72 
    - Ou seja, a relação ainda é positiva, mas parece bem mais fraca, justamente porque o intervalo de dados é restrito — o fenômeno chamado restrição de faixa.

### 3. Correção HM (destacada no título do gráfico)
    
- A fórmula de Hindemburg corrige esse efeito matematicamente e estima qual seria a correlação verdadeira se a amostra tivesse a mesma variabilidade que a população.
  - Resultado: Correção HM = ~0,97
    - Ou seja, quase igual à correlação real da população — mostrando que a distorção causada pela amostra restrita foi corrigida com sucesso.