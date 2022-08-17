import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="Measurement", page_icon="🔬")
st.sidebar.header("Ads Measurement")

st.title("Ads Measurement")

st.write("Statistical models and analyses (effectiveness, sampling, survey and NLP)")
st.write("")


st.write("#### Choose an appropriate measurement method")

mcol1, mcol2, mcol3 = st.columns(3)
with mcol1:
    st.markdown("##### Experimental measurement")
    st.markdown("---")
    st.write("###### A/B Test")
    st.image("figures/ABTesting.png", width=170)
    st.write("Test variables like, audience, placement, creative, new RTB algorithm")
with mcol2:
    st.markdown("##### Quasi-experimental measurement")
    st.markdown("---")
    st.write("###### Geo based Matched Market Test")
    st.image("figures/GeoExperiment.png", width=210)
with mcol3:
    st.write("##### Observational measurement")
    st.markdown("---")
    st.write("###### Data-driven attribution (DDA)")
    st.image("figures/MTA.jpeg", width=200)

mcol1, mcol2, mcol3 = st.columns(3)
with mcol1:
    st.write("###### Incrementality")
    st.image("figures/Incrementality.png", width=170)
    st.markdown("""
                - Brand Lift Testing
                - Conversion Lift Testing
                """)
with mcol2:
    st.write("###### Time-series based Causal Impact Analysis")
    st.image("figures/CausalImpact.png", width=170)
    st.write("")
with mcol3:
    st.write("###### Marketing mix modeling (MMM)")
    st.image("figures/MMM.png", width=200)
    st.write("")

st.markdown("""
            Image credit:
            - [A/B tests](https://www.brillmark.com/ab-testing/)
            - [Incrementality](https://mackgrenfell.com/blog/conversion-lift-tests-are-dead-transitioning-to-geo-experiments)
            - [Matched Market Test](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/45950.pdf)
            - [CausalImpact](https://google.github.io/CausalImpact/CausalImpact.html)
            - [Data-driven attribution (DDA)](https://conversionmarketing.co.nz/google-adwords-conversion-paths/)
            """)

st.write("---")
st.markdown(""" ###### © 2022 Xinjie Qiu ℠""")


