"""FarmTech Solutions - Fase 5 (Google Colab / Python Script)

Este script unifica toda a solução em um único arquivo Python, para ser executado
via Colab (ou localmente) sem depender de notebooks. Basta garantir que:

1) O arquivo `crop_yield.csv` esteja no mesmo diretório.
2) As dependências de `requirements.txt` estejam instaladas.

Exemplo (Colab):

!pip install -r requirements.txt
!python FarmTech_Solutions_Fase5_Colab.py

"""

import os
import sys

try:
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    from sklearn.preprocessing import StandardScaler
    from sklearn.model_selection import train_test_split
    from sklearn.cluster import KMeans
    from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
    from sklearn.linear_model import LinearRegression, Ridge
    from sklearn.svm import SVR
    from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
    from sklearn.decomposition import PCA
except ImportError as e:
    print("Biblioteca ausente:", e)
    print("Execute: pip install -r requirements.txt")
    sys.exit(1)


def main():
    # --- 1) Carregar e inspecionar dados
    csv_file = "crop_yield.csv"
    if not os.path.exists(csv_file):
        raise FileNotFoundError(f"Arquivo não encontrado: {csv_file}. Coloque-o no mesmo diretório.")

    df = pd.read_csv(csv_file)
    print("\n--- DADOS CARREGADOS ---")
    print(f"Dimensões: {df.shape}")
    print(df.head())
    print("\nTipos:")
    print(df.dtypes)
    print("\nMissing values por coluna:")
    print(df.isnull().sum())

    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    if "Yield" not in numeric_cols:
        raise ValueError("O dataset precisa conter a coluna 'Yield' como variável alvo.")

    preditoras = [c for c in numeric_cols if c != "Yield"]

    # --- 2) EDA rápido
    print("\n--- ESTATÍSTICAS DESCRITIVAS ---")
    print(df[numeric_cols].describe())

    # Plots (apenas se estiver em ambiente com display)
    try:
        plt.figure(figsize=(12, 8))
        df[numeric_cols].hist(bins=20, figsize=(12, 8))
        plt.suptitle("Distribuição das Variáveis Numéricas")
        plt.tight_layout()
        plt.show()
    except Exception:
        pass

    # Correlação
    corr = df[numeric_cols].corr()
    print("\n--- CORRELAÇÃO (Pearson) ---")
    print(corr)

    # --- 3) Clustering (K-Means)
    X_clustering = df[preditoras].copy()
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_clustering)

    inertia = []
    k_range = range(1, 8)
    for k in k_range:
        km = KMeans(n_clusters=k, random_state=42, n_init=10)
        km.fit(X_scaled)
        inertia.append(km.inertia_)

    try:
        plt.figure(figsize=(8, 5))
        plt.plot(k_range, inertia, marker="o")
        plt.xlabel("Número de clusters (K)")
        plt.ylabel("Inércia")
        plt.title("Método do Cotovelo - Escolhendo K")
        plt.grid(True)
        plt.show()
    except Exception:
        pass

    k_optimo = 3
    kmeans = KMeans(n_clusters=k_optimo, random_state=42, n_init=10)
    df["Cluster"] = kmeans.fit_predict(X_scaled)

    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)

    try:
        plt.figure(figsize=(10, 6))
        scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=df["Cluster"], cmap="viridis", alpha=0.7)
        plt.xlabel("Componente Principal 1")
        plt.ylabel("Componente Principal 2")
        plt.title("Clusters (PCA)")
        plt.colorbar(scatter)
        plt.show()
    except Exception:
        pass

    print("\n--- Estatísticas por Cluster (médias) ---")
    print(df.groupby("Cluster")[numeric_cols].mean())

    # --- 4) Detecção de Outliers (IQR)
    def outliers_iqr(series):
        q1 = series.quantile(0.25)
        q3 = series.quantile(0.75)
        iqr = q3 - q1
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr
        return series[(series < lower) | (series > upper)], lower, upper

    print("\n--- Detecção de Outliers (IQR) ---")
    outlier_counts = {}
    for col in numeric_cols:
        out, lo, hi = outliers_iqr(df[col])
        outlier_counts[col] = (len(out), lo, hi)
        print(f"{col}: {len(out)} outliers (limites [{lo:.2f}, {hi:.2f}])")

    df_clean = df.copy()
    for col in numeric_cols:
        out, lo, hi = outliers_iqr(df_clean[col])
        df_clean = df_clean[~df_clean.index.isin(out.index)]

    print(f"\nAmostras originais: {len(df)}")
    print(f"Amostras após remoção de outliers: {len(df_clean)}")

    # --- 5) Modelos preditivos
    X = df_clean[preditoras]
    y = df_clean["Yield"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    scaler_model = StandardScaler()
    X_train_scaled = scaler_model.fit_transform(X_train)
    X_test_scaled = scaler_model.transform(X_test)

    models = {
        "Linear Regression": LinearRegression(),
        "Ridge Regression": Ridge(alpha=1.0),
        "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42),
        "Gradient Boosting": GradientBoostingRegressor(n_estimators=100, random_state=42),
        "SVR": SVR(kernel="rbf", C=1.0),
    }

    results = {}

    for name, model in models.items():
        if name in ["Random Forest", "Gradient Boosting"]:
            model.fit(X_train, y_train)
            preds = model.predict(X_test)
        else:
            model.fit(X_train_scaled, y_train)
            preds = model.predict(X_test_scaled)

        results[name] = {
            "MSE": mean_squared_error(y_test, preds),
            "MAE": mean_absolute_error(y_test, preds),
            "R2": r2_score(y_test, preds),
        }

    results_df = pd.DataFrame(results).T
    print("\n--- Resultados dos Modelos ---")
    print(results_df)

    try:
        plt.figure(figsize=(10, 6))
        bars = plt.bar(results_df.index, results_df["R2"], color=["blue", "green", "red", "purple", "orange"])
        plt.xlabel("Modelo")
        plt.ylabel("R²")
        plt.title("Comparação de R²")
        plt.ylim(min(0, results_df["R2"].min() - 0.05), 1)
        for bar, value in zip(bars, results_df["R2"]):
            plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.01, f"{value:.3f}", ha="center")
        plt.xticks(rotation=45)
        plt.grid(axis="y", alpha=0.3)
        plt.tight_layout()
        plt.show()
    except Exception:
        pass

    best = results_df["R2"].idxmax()
    print(f"\nMelhor modelo: {best} (R² = {results_df.loc[best, 'R2']:.4f})")


if __name__ == "__main__":
    main()
