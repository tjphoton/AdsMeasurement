import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="Measurement", page_icon="🔬")
st.sidebar.header("Ads Measurement")

st.title("Ads Measurement")

# st.write("#### Choose an appropriate measurement method")

st.markdown(
    """
        <style>
        .streamlit-expanderHeader {
            font-size: x-large;
            font-weight: bold;
            ~~~ font-family: Didot;
            ~~~ color: rgb(83,36,118,1);
        }
        </style>
    """,
    unsafe_allow_html=True,
)

with st.expander("Experimental measurement", expanded=True):
    mcol1, mcol2 = st.columns(2)
    with mcol1:
        st.write("###### A/B Test")
        st.image("figures/ABTesting.png", width=180)
        st.write("Test variables like, audience, placement, creative, ad format, bidding strategy, etc.")
    with mcol2:
        st.write("###### Incrementality")
        st.image("figures/Incrementality.png", width=170)
        st.markdown("""
                    - Brand Lift Testing (upper funnel metric)
                    - Conversion Lift Testing (lower funnel metric)
                    """)

with st.expander("Quasi-experimental measurement", expanded=True):
    mcol1, mcol2 = st.columns(2)
    with mcol1:
        st.write("###### Geo based Matched Market Test")
        st.image("figures/GeoExperiment.png", width=210)
        st.write("Measure the impact of online advertising on offline sales. Geo matching is used "
                 "instead of a randomized assignment of geos to treatment and control.")
    with mcol2:
        st.write("###### Time-series based Causal Impact Analysis")
        st.image("figures/CausalImpact.png", width=170)
        st.write("Predicts the time series of the counterfactual market response, "
                 "directly estimate the cumulative causal effect. Applicable to "
                 "smaller market with limited number of geos")

with st.expander("Observational measurement", expanded=True):
    mcol1, mcol2 = st.columns(2)
    with mcol1:
        st.write("###### Data-driven attribution (DDA)")
        st.image("figures/MTA.jpeg", width=200)
        st.write("Systematically determine the appropriate campaign(s) receiving conversion credit "
                 "after ad exposure or engagement.")
    with mcol2:
        st.write("###### Marketing mix modeling (MMM)")
        st.image("figures/MMM.png", width=200)
        st.write("Measure the effectiveness of advertising spend from aggregate historical time series data. "
                 "Metrics such as return on advertising spend (ROAS) and optimized "
                 "budget allocations across channels can be derived from the output of these models")


st.write("---")
st.markdown(""" ###### © 2022 Xinjie Qiu ℠""")

st.markdown("""
            Image credit:
            - [A/B tests](https://www.brillmark.com/ab-testing/)
            - [Incrementality](https://mackgrenfell.com/blog/conversion-lift-tests-are-dead-transitioning-to-geo-experiments)
            - [Matched Market Test](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/45950.pdf)
            - [CausalImpact](https://google.github.io/CausalImpact/CausalImpact.html)
            - [Data-driven attribution (DDA)](https://conversionmarketing.co.nz/google-adwords-conversion-paths/)
            """)




