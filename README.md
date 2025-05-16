# Range Restriction Correlation Correction — HM Formula

This project demonstrates the practical implementation of the **HM (Hindemburg Melão Jr.) formula** for correcting Pearson's correlation in cases with **range restriction**, such as homogeneous or limited samples, where the observed correlation may be underestimated.


- [Leia-me em português do Brasil](README_pt_BR.md)
- [Readme](README_en_US.md)

---

### Basic usage (REST Service)

#### Dockerfile

1. Run the following command to build the image:

```shell
docker build -t hm-correlation-correction-rest .
```

2. Run the following command to run the container (dev mode):

```shell
docker run -e FLASK_ENV=dev -p 8080:5000 hm-correlation-correction-rest
```

3. Run the following command to run the container (production mode):

```shell 
docker run -p 8080:5000 hm-correlation-correction-rest
```

4. Run the following command to run the container (production mode, port 8000):

```shell 
docker run -e PORT=8000 -p 8080:8000 hm-correlation-correction-rest
```

#### Docker Compose

```shell
# Para produção
docker-compose up api

# Para desenvolvimento
docker-compose up api-dev
```

---

### Request sample

#### cURL

```shell
curl -X POST 'http://localhost:5000/plot' \
--form 'file=@"/path/to/file/dados.csv"' \
--form 'x_col="altura"' \
--form 'y_col="pe"' \
--form 'x_label="Altura (m)"' \
--form 'y_label="Tamanho do pé (m)"' \
--form 'figsize="10,6"' \
--form 'filter_condition="altura < 1.20"'
```

---

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![python](https://img.shields.io/badge/Python-3.12-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
