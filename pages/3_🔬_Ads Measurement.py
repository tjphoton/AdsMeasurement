import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="Measurement", page_icon="🔬")
st.sidebar.header("Ads Measurement")

st.title("Ads Measurement")

st.write("Statistical models and analyses (effectiveness, sampling, survey and NLP)")
st.write("[CausalImpact](https://google.github.io/CausalImpact/CausalImpact.html)")


st.write("#### Measurement methods")

mcol1, mcol2, mcol3 = st.columns(3)
with mcol1:
    st.write("##### Observational  ")
    st.write("###### Data-driven attribution (DDA)")
    st.image("figures/MTA.jpeg", width=200)
    st.write("")
with mcol2:
    st.markdown("##### Experimental  ")
    st.write("###### A/B tests")
    st.image("figures/ABTesting.png", width=150)
    st.write("May be used to test variables like, audience, placement, creative, new smart bidding algorithm")
with mcol3:
    st.markdown("##### Pseudo-experimental ")
    st.write("###### Geo based Matched Market Test")
    st.image("figures/GeoExperiment.png", width=200)
    st.write("")

mcol1, mcol2, mcol3 = st.columns(3)
with mcol1:
    st.write("###### Marketing mix modeling (MMM)")
    st.image("figures/MMM.png", width=200)
    st.write("")
with mcol2:
    st.write("###### Incrementality")
    st.image("figures/Incrementality.png", width=200)
    st.markdown("""
                - Brand Lift Testing
                - Conversion Lift Testing
                """)
with mcol3:
    st.write("###### Time-series based Causal Impact Analysis")
    st.image("figures/CausalImpact.png", width=170)
    st.write("")


st.markdown(""" ###### © 2022 Xinjie Qiu ℠""")