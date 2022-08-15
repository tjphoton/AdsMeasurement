import streamlit as st
import datetime
import pandas as pd
import altair as alt

st.set_page_config(page_title="Goal", page_icon="🎯")
st.sidebar.header("Business Goal & KPI")

st.title("Business Goal & KPI")
st.markdown("""
            ##### Determine your SMART business goal
            ###### (specific, measurable, achievable, relevant and time-bound)
            """)

mcol1, mcol2, mcol3, mcol4 = st.columns(4)
with mcol1:
    biz_goal = st.selectbox("To increase",
                            ("Brand awareness", "Consideration", "Intention",
                             "Online sales", "In store sales", "Total revenue", "lifetime value of customers"))
with mcol2:
    st.number_input('by', 1, 20, 5, 1, "%d")
    st.write("percentage points or more")
with mcol3:
    st.date_input("between", datetime.date(2022, 10, 1))
    st.date_input("and", datetime.date(2022, 12, 31))
with mcol4:
    st.date_input("compared to between", datetime.date(2021, 10, 1))
    st.date_input("and", datetime.date(2021, 12, 31))


st.write("")
st.write("##### Establish your campaign KPIs")
container1 = st.container()
container2 = st.container()

if biz_goal == "Brand awareness":
    KPI1 = container1.radio(f"Based on your business goal ({biz_goal}), we recommend to measure one of the following Primary KPIs:",
                   ("Unaided brand awareness", "Aided brand awareness", "Impressions"))
    KPI2 = container2.radio(f"Based on your business goal ({biz_goal}), we recommend to measure one of the following Secondary KPIs:",
                   ("Aided brand awareness", "Unaided brand awareness", "Impressions"))

if biz_goal == "Consideration":
    KPI1 = container1.radio(f"Based on your business goal ({biz_goal}), we recommend to measure one of the following Primary KPIs:",
                   ("Site visit sessions", "Engagement (View) rate", "Click-through rate (CTR)"))

    KPI2 = container2.radio(f"Based on your business goal ({biz_goal}), we recommend to measure one of the following Secondary KPIs:",
                   ("Click-through rate (CTR)", "Site visit sessions", "Engagement (View) rate"))

if biz_goal == "Online sales":
    KPI1 = container1.radio(f"Based on your business goal ({biz_goal}), we recommend to measure one of the following Primary KPIs:",
                    ("Return on Ad Spend (ROAS)", "Transactions", "Average Order Value (AOV)", "Cost per Acquisition (CpAC)"))
    KPI2 = container2.radio(f"Based on your business goal ({biz_goal}), we recommend to measure one of the following Secondary KPIs:",
                    ("Transactions", "Average Order Value (AOV)", "Cost per Acquisition", "Return on Ad Spend (ROAS)"))

KPI1_bench = container1.text_input(f"Your Primary KPI ({KPI1}) benchmark (default value pulled from the most "
                                   f"recent campaign, if available). Feel free to modify:")
KPI2_bench = container2.text_input(f"Your Primary KPI ({KPI2}) benchmark (default value pulled from the most "
                                   f"recent campaign, if available). Feel free to modify:")

st.write("")
st.write("")
st.write("##### Feasibility Estimation for Primary KPI _(may not be a good idea to show this info)_")
st.write("Based on your historical campaign performance, creative performance, market dynamics, industry benchmark, "
         "and other data sources, our statistical model(s) estimate the probability to achieve the business goal "
         "at 95% confidence level is:")
st.latex("76\%^{+8\%}_{-6\%}")
st.write("You may adjust the percentage number in business goal to fine tune the feasibility probability shown above.")

st.write("")
st.write("")
st.markdown(""" ###### © 2022 Xinjie Qiu ℠""")