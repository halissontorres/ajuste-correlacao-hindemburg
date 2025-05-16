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
        r_star_corr = r_star / (correction_factor ** 0.5)

        r_hm = r_star_corr / (1 + r_star_corr)

        return r_hm