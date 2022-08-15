import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="DAQ", page_icon="💾")
st.sidebar.header("Data Acquisition & Ingestion")

st.title("Data Acquisition & Ingestion")

st.write("##### Data for the Ads Measurement Products are coming from the following sources:")
st.markdown("""
            - Ad exposures (streaming TV ads, display ads, and search ads)
            - Purchase receipts
            - Device interactions
            - Customer behavior
            """)

st.image("figures/DAQ_animation.gif")

st.write("These rapidly growing complex data sets need to be monitored in real time to ensure the data quality. "
         "They also need to be transformed to find signals for intuitive measurements for advertisers to easily "
         "gain insights and take actions to manage their campaigns")


st.write("")
st.markdown(""" ###### © 2022 Xinjie Qiu ℠""")