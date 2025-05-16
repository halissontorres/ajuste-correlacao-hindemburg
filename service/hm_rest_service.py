import io
import matplotlib.pyplot as plt
import pandas as pd
from flask import Flask, request, jsonify, send_file

from graphics.hm_correlation_plotter import HMCorrelationPlotter

app = Flask(__name__)

@app.route("/plot", methods=["POST"])
def generate_plot():
    if "file" not in request.files:
        return jsonify({"Error": "Arquivo CSV não informado."}), 400

    file = request.files["file"]
    if not file.filename.endswith(".csv"):
        return jsonify({"Error": "Formato de arquivo inválido. formato suportado: CSV"}), 400

    try:
        df = pd.read_csv(file)
    except Exception as e:
        return jsonify({"error": f"Failed to read CSV: {str(e)}"}), 400

    x_col = request.form.get("x_col")
    y_col = request.form.get("y_col")

    if not x_col or not y_col:
        return jsonify(f"As colunas '{x_col}' e '{y_col}' não existem no DataFrame."), 400

    filter_condition = request.form.get("filter_condition")
    x_label = request.form.get("x_label", x_col)
    y_label = request.form.get("y_label", y_col)
    title = request.form.get("title")
    figsize = request.form.get("figsize", "10,6")

    try:
        figsize = tuple(map(float, figsize.split(",")))
    except:
        figsize = (10, 6)

    try:
        plotter = HMCorrelationPlotter(
            csv_data=df,
            x_col=x_col,
            y_col=y_col,
            filter_condition=filter_condition,
            x_label=x_label,
            y_label=y_label,
            title=title,
            figsize=figsize
        )

        fig = plt.figure(figsize=figsize)
        plotter.plot()
        buf = io.BytesIO()
        plt.savefig(buf, format="png")
        buf.seek(0)
        plt.close(fig)
        return send_file(buf, mimetype="image/png", download_name="correlacao_hm.png")
    except Exception as e:
        return jsonify({"error": f"Houve um erro ao tentar atender à solicitação: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)