import matplotlib.pyplot as plt


def carte_candidat(df, gdf_limite, nom_candidat):
    """
    Génère une carte de score pour un candidat donné.
    """
    data = df[df['candidat'].str.contains(nom_candidat)].copy()
    data_map = gdf_limite.merge(data, left_on='INSEE_DEP', right_on='code_departement')

    fig, ax = plt.subplots(figsize=(8, 8))
    data_map.plot(column='score_departement',
                  legend=True,
                  cmap='RdBu_r',
                  ax=ax)

    ax.set_title(f'Score de {nom_candidat} : % par rapport moyenne nationale')
    ax.set_axis_off()
    return fig
