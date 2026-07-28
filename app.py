import streamlit as st
import pandas as pd

from goosebumps import (
    load_data,
    create_heatmap_data,
    create_heatmap_data_percents,
    yearly_histogram,
    heatmap_raw,
    heatmap_pct
)


df_long = load_data('data/Goosebumps.csv')

heatmap_data = create_heatmap_data(df_long)
heatmap_data_pct = create_heatmap_data_percents(heatmap_data)

st.title("Goosebumps Mileage Analysis")

view = st.radio(
    "View",
    ["Yearly Histograms", "Raw Heatmap", "Percent Heatmap"]
)


if view == "Yearly Histograms":

    df_long["Year"] = pd.to_numeric(df_long["Year"])

    years = sorted(df_long["Year"].unique())

    years = [y for y in years if y != 2020]

    year = st.select_slider(
        "Year",
        options=years,
        value=max(years)
    )

    st.pyplot(yearly_histogram(df_long, year))


elif view == "Raw Heatmap":
    st.pyplot(heatmap_raw(heatmap_data.T.iloc[::-1]))


elif view == "Percent Heatmap":
    st.pyplot(heatmap_pct(heatmap_data_pct.T.iloc[::-1]))
