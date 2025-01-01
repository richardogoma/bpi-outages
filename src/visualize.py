import streamlit as st
import pandas as pd
from heapq import nlargest


def display_outages(outages):
    st.title("Outage Visualization")
    st.write("Longest Outages")
    longest_outages = nlargest(10, outages, key=lambda x: x[2])
    df = pd.DataFrame(longest_outages, columns=["Start", "End", "Duration"])
    st.table(df)

    st.write("Outage Durations (in minutes)")
    df["Duration"] = (
        pd.to_numeric(df["Duration"], errors="coerce") / 1e9 / 60
    )  # Convert nanoseconds to minutes
    st.bar_chart(df.set_index("Start")["Duration"])
