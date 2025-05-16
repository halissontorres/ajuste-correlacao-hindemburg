from scipy.stats import pearsonr
import numpy as np

class HMCorrelation:
    """
    Classe para cálculos de correção da correlação de Pearson em casos com restrição de faixa,
    como amostras homogêneas ou limitadas, onde a correlação observada pode ser subestimada.
    """

    @staticmethod
    def apply(r_obs, s_x, s_y, s_xT, s_yT):
        """
        Aplica a fórmula HM de correção da correlação de Pearson com restrição de faixa.

        Parâmetros:
        - r_obs: correlação observada na amostra restrita
        - s_x: desvio padrão da variável x na amostra restrita
        - s_y: desvio padrão da variável y na amostra restrita
        - s_xT: desvio padrão da variável x na população total (ou amostra completa)
        - s_yT: desvio padrão da variável y na população total (ou amostra completa)

        Retorna:
        - r_hm: correlação corrigida usando a fórmula de Hindemburg Melão Jr.
        """
        if abs(r_obs) >= 1:
            raise ValueError("r_obs deve estar estritamente entre -1 e 1")

        r_star = r_obs / (1 - abs(r_obs))
        correction_factor = (s_x ** 2 / s_xT ** 2) * (s_y ** 2 / s_yT ** 2)
        r_star_corr = r_star / np.sqrt(correction_factor)
        r_HM = r_star_corr / (1 + r_star_corr)

        return r_HM

    @staticmethod
    def from_dataframes(df_total, df_restrita, x_col, y_col):
        """
        Calcula r_obs, r_true e r_hm a partir dos DataFrames.

        Retorna um dicionário com:
        - r_obs
        - r_true
        - r_hm
        - s_x, s_y (restritos)
        - s_xT, s_yT (totais)
        """
        s_xT = df_total[x_col].std()
        s_yT = df_total[y_col].std()

        # Aplica filtro: amostra restrita (ex: altura < 1.20)
        restrita = df_total[df_total[x_col] < 1.20]

        s_x = df_restrita[x_col].std()
        s_y = df_restrita[y_col].std()

        r_obs, _ = pearsonr(df_restrita[x_col], df_restrita[y_col])
        r_true, _ = pearsonr(df_total[x_col], df_total[y_col])
        r_hm = HMCorrelation.apply(r_obs, s_x, s_y, s_xT, s_yT)

        return {
            "r_obs": r_obs,
            "r_true": r_true,
            "r_hm": r_hm,
            "s_x": s_x, "s_y": s_y,
            "s_xT": s_xT, "s_yT": s_yT
        }