# Range Restriction Correlation Correction — HM Formula

This project demonstrates the practical implementation of the **HM (Hindemburg Melão Jr.) formula** for correcting Pearson's correlation in cases with **range restriction**, such as homogeneous or limited samples, where the observed correlation may be underestimated.

## 📘 Theoretical Basis

This repository is based on the article:

**"A Superior Alternative to Thorndike and Schmidt—Hunter for Correcting Pearson's Correlation"**  
📄 Author: [Hindemburg Melão Jr](https://www.instagram.com/hindemburg.melao).  
🔗 Full article: [SSRN ID 5237520](https://ssrn.com/abstract=5237520)  
🌐 More information: [sigmasociety.net/hm](http://www.sigmasociety.net/hm)

> The author proposes a new formula that resolves the limitations of Thorndike (1949) and Schmidt & Hunter (1976, 1998) corrections, naturally keeping the corrected correlation within the [–1, 1] interval without artificial truncations.

## 🧠 Objective

Demonstrate, with simulated data, the application of the **HM formula** for correcting Pearson's correlation and compare:

- Observed correlation in restricted samples;
- Correlation corrected via HM;
- Real correlation in the total population.

## 🧪 Features

- Generation of simulated anthropometric data (height x foot);
- Calculation of Pearson's correlation (`r`);
- Implementation of the **HM formula**;
- Graphical visualization comparing:
  - Total population
  - Restricted samples
  - Noise effect

## 📈 Graph Examples

[Here](assets/README.md), the apparent correlation drops dramatically, but the HM formula recovers the real value with precision.

## 📦 Included Files

- [hm_correlation.py](core/hm_correlation.py) – Correlation script
- [hm_correlation_plotter.py](graphics/hm_correlation_plotter.py) - Graph plotting script
- [hm_rest_service.py](service/hm_rest_service.py) - REST service
- [dados.csv](assets/dados.csv) - Simulated test data

## 🧠 Credits

- **Original Article and Formula**: Hindemburg Melão Jr. - [SSRN ID 5237520](https://ssrn.com/abstract=5237520).  
- **Contains code snippets suggested or improved by AI**

## 📄 License

This project is distributed for educational and demonstrative purposes, based publicly on Hindemburg Melão Jr.'s article. Consult the original author for scientific publication or redistribution purposes.