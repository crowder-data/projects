import streamlit as st

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


view = st.radio(
    "View",
    ["Yearly Histograms", "Raw Heatmap", "Percent Heatmap"]
)


if view == "Yearly Histograms":
    year = st.selectbox(
        "Year",
        sorted(df_long["Year"].unique())
    )

    st.pyplot(yearly_histogram(df_long, year))


elif view == "Raw Heatmap":
    st.pyplot(heatmap_raw(heatmap_data.T.iloc[::-1]))


elif view == "Percent Heatmap":
    st.pyplot(heatmap_pct(heatmap_data_pct.T.iloc[::-1]))
