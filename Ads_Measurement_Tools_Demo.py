import streamlit as st

def run():
    st.set_page_config(
        page_title="Ads Measurement App",
        page_icon="⚙️",
        initial_sidebar_state="expanded"
    )

    st.sidebar.success("Select an Ad measurement component tool above.")

    st.title("Ads Measurement Self-service Data Science Tools")
    st.markdown(""" ##### © 2022 Xinjie Qiu ℠""")

    st.write("")
    st.write("")

    sp0, mcol1, sp1, mcol2, sp2 = st.columns([.5,2,.5,2,.5])
    with mcol1:
        st.markdown("##### Business Goal and KPI")
        st.image("figures/Goal.jpg", width=110)
        st.write("Align business goal to KPIs")

    with mcol2:

        st.markdown("""##### Data Acquisition""")
        st.image("figures/DAQ.jpg", width=110)
        st.write("Real time data quality monitoring on ingestion, transformation")

    sp0, mcol1, sp1, mcol2, sp2 = st.columns([.5,2,.5,2,.5])
    with mcol1:
        st.markdown("##### Ads Measurements")
        st.image("figures/Experiment.jpg", width=78)
        st.write("Experimentation and statistical analysis")

    with mcol2:
        st.markdown("##### Infer Causality")
        st.image("figures/Wrench.jpg", width=110)
        st.write("Generate insights and make data-driven recommendations")

    st.write("")
    st.markdown("""
                **👈 Select a demo from the sidebar** to see some examples
                of what the Ads Measurement Data Science Tools can do for your campaign!
                """)

    st.write("")
    st.write("")
    st.write("")
    st.markdown(""" ###### © 2022 Xinjie Qiu ℠""")

if __name__ == "__main__":
    run()