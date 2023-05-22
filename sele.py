import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go


def plot():

    df = pd.read_csv("checkup.csv")

    clist = df["md"].unique().tolist()
    #st.write("1=สมภพ 2=ธีรนันท์ 3=ภาณุภัท 4=แพทย์ประจำบ้านหรือแพทย์อื่นๆ")
    mds = st.multiselect("เลือกแพทย์: 1=สมภพ 2=ธีรนันท์ 3=ภาณุภัท 4=แพทย์ประจำบ้าน/แพทย์อื่นๆ", clist)
    #st.header("ท่านได้เลือก: {}".format(", ".join(str(mds) for mds in clist)))

    dfs = {md: df[df["md"] == md] for md in mds}

    fig = go.Figure()
    for md, df in dfs.items():
        fig = fig.add_trace(go.Scatter(x=df["dat"], y=df["fu"], name=md))

    st.plotly_chart(fig)


plot()

