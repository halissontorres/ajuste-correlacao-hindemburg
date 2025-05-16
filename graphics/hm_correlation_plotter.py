import matplotlib.pyplot as plt
import seaborn as sns

class PlotterHM:

    @staticmethod
    def plot_hm(hm, title, xlabel, ylabel, cmap='viridis'):
        # Amostra restrita: altura < 1.20
        restrita = df[df["altura"] < 1.20]
        s_x = restrita["altura"].std()
        s_y = restrita["pe"].std()
        r_obs, _ = pearsonr(restrita["altura"], restrita["pe"])
        r_HM = hm_correlation(r_obs, s_x, s_y, s_xT, s_yT)

        # Gráfico
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=df, x="altura", y="pe", color="gray", alpha=0.2, label="População Total")
        sns.scatterplot(data=restrita, x="altura", y="pe", color="blue", label="Amostra Restrita")

        plt.title(f"Correlação Observada: {r_obs:.2f} | Correção HM: {r_HM:.2f} | Correlação Real: {r_true:.2f}")
        plt.xlabel("Altura (m)")
        plt.ylabel("Tamanho do Pé (m)")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()

        # Exibir o gráfico
        plt.show()