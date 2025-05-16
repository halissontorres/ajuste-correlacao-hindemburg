import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from core.hm_correlation import HMCorrelation

class HMCorrelationPlotter:

    def __init__(self, csv_data, x_col, y_col, filter_condition=None,
                 x_label="X", y_label="Y", title=None, figsize=(10, 6)):
        """
        Parâmetros:
        - csv_data: caminho do CSV ou objeto pd.DataFrame
        - x_col, y_col: nomes das colunas numéricas
        - filter_condition: string de condição (pandas query) para filtrar a amostra restrita
        - x_label, y_label: rótulos dos eixos
        - title: título customizado (opcional)
        """
        self.figsize = figsize
        self.x_col = x_col
        self.y_col = y_col
        self.filter_condition = filter_condition
        self.x_label = x_label
        self.y_label = y_label
        self.custom_title = title

        self.df_total = None

        if isinstance(csv_data, pd.DataFrame):
            self.df_total: pd.DataFrame = csv_data.copy()
        else:
            self.df_total = pd.read_csv(csv_data)

        if not {x_col, y_col}.issubset(self.df_total.columns):
            raise ValueError(f"As colunas '{x_col}' e '{y_col}' não existem no DataFrame.")

        if isinstance(csv_data, pd.DataFrame):
            self.df_total = csv_data.copy()
        else:
            self.df_total = pd.read_csv(csv_data)

        self.df_restrita: pd.DataFrame = self.df_total.query(filter_condition) if filter_condition else self.df_total

        self.results = HMCorrelation.from_dataframes(self.df_total, self.df_restrita, x_col, y_col)

    def plot(self):
        title = self.custom_title or (
            f"Correlação Observada: {self.results['r_obs']:.2f} | "
            f"Correção HM: {self.results['r_hm']:.2f} | "
            f"Correlação Real: {self.results['r_true']:.2f}"
        )

        plt.figure(figsize=self.figsize)
        sns.scatterplot(data=self.df_total, x=self.x_col, y=self.y_col, color="gray", alpha=0.2, label="População Total", marker='x')
        sns.scatterplot(data=self.df_restrita, x=self.x_col, y=self.y_col, color="blue", label="Amostra Restrita", marker='x')

        plt.title(title)
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.legend()
        plt.grid(True)
        plt.tight_layout()