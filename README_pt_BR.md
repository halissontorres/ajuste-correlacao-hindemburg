# Correção de Correlação com Restrição de Faixa — Fórmula HM

Este projeto demonstra a implementação prática da fórmula **HM (Hindemburg Melão Jr.)** para correção da correlação de Pearson em casos com **restrição de faixa**, como amostras homogêneas ou limitadas, onde a correlação observada pode ser subestimada.

## 📘 Base Teórica

Este repositório é baseado no artigo:

**“A Superior Alternative to Thorndike and Schmidt—Hunter for Correcting Pearson’s Correlation”**  
📄 Autor: [Hindemburg Melão Jr](https://www.instagram.com/hindemburg.melao).  
🔗 Artigo completo: [SSRN ID 5237520](https://ssrn.com/abstract=5237520)  
🌐 Mais informações: [sigmasociety.net/hm](http://www.sigmasociety.net/hm)

> O autor propõe uma nova fórmula que resolve as limitações das correções de Thorndike (1949) e Schmidt & Hunter (1976, 1998), mantendo a correlação corrigida naturalmente dentro do intervalo [–1, 1] sem truncamentos artificiais.

## 🧠 Objetivo

Demonstrar, com dados simulados, a aplicação da **fórmula HM** para correção da correlação de Pearson e comparar:

- Correlação observada em amostras restritas;
- Correlação corrigida via HM;
- Correlação real na população total.

## 🧪 Funcionalidades

- Geração de dados simulados antropométricos (altura x pé);
- Cálculo da correlação de Pearson (`r`);
- Implementação da **fórmula HM**;
- Visualização gráfica comparando:
  - População total
  - Amostras restritas
  - Efeito do ruído

## 📈 Exemplos de Gráficos

Três amostras comparadas:

1. Crianças com altura < 1.20 m
2. Altura < 1.10 m (mais restrita)
3. Altura < 1.10 m + ruído adicional

A correlação aparente cai drasticamente, mas a fórmula HM recupera o valor real com precisão.

## 📦 Arquivos incluídos

- `correcao_hm_grafico.py` – Script Python
- `dados.csv` – Dados simulados para teste
- `README.md` – Este arquivo

## 🧠 Créditos

- **Artigo e Fórmula Original**: Hindemburg Melão Jr. - [SSRN ID 5237520](https://ssrn.com/abstract=5237520)  .  
- **Há trechos de códigos, sugeridos ou aperfeiçoados por IA**pt)

## 📄 Licença

Este projeto é distribuído com fins educacionais e demonstrativos, com base pública no artigo de Hindemburg Melão Jr. Consulte o autor original para fins de publicação ou redistribuição científica.
