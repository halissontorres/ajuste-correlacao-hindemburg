# Range Restriction Correlation Correction — HM Formula

This project demonstrates the practical implementation of the **HM (Hindemburg Melão Jr.) formula** for correcting Pearson's correlation in cases with **range restriction**, such as homogeneous or limited samples, where the observed correlation may be underestimated.

## 📘 Theoretical Basis

This repository is based on the article:

**"A Superior Alternative to Thorndike and Schmidt—Hunter for Correcting Pearson's Correlation"**  
📄 Author: [Hindemburg Melão Jr](https://www.instagram.com/hindemburg.melao).  
🔗 Full article: [SSRN ID 5237520](https://ssrn.com/abstract=5237520)  
🌐 More information: [sigmasociety.net/hm](http://www.sigmasociety.net/hm)

> The author proposes a new formula that addresses the limitations of Thorndike (1949) and Schmidt & Hunter (1976, 1998) corrections, naturally keeping the corrected correlation within the [–1, 1] interval without artificial truncations.

## 🧠 Objective

To demonstrate, with simulated data, the application of the **HM formula** for correcting Pearson's correlation and compare:

- Observed correlation in restricted samples;
- Correlation corrected via HM;
- Actual correlation in the total population.

## 🧪 Features

- Generation of simulated anthropometric data (height x foot);
- Calculation of Pearson's correlation (`r`);
- Implementation of the **HM formula**;
- Graphical visualization comparing:
  - Total population
  - Restricted samples
  - Noise effect

## 📈 Graph Examples

Three compared samples:

1. Children with height < 1.20 m
2. Height < 1.10 m (more restricted)
3. Height < 1.10 m + additional noise

The apparent correlation drops dramatically, but the HM formula recovers the real value with precision.

## 📦 Included Files

- `correcao_hm_grafico.py` – Python script
- `dados.csv` – Simulated test data
- `README.md` – This file

## 🧠 Credits

- **Original Article and Formula**: Hindemburg Melão Jr. - [SSRN ID 5237520](https://ssrn.com/abstract=5237520)  
- **There are code snippets, suggested or improved by AI**

## 📄 License

This project is distributed for educational and demonstrative purposes, based publicly on Hindemburg Melão Jr.'s article. Consult the original author for publication or scientific redistribution purposes.