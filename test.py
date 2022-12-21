import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

st.header('🌲 Forest conflict topics over time')
st.markdown('*Swedish media 2012-01-01 -- 2022-05-31 via Retriever.*')
st.markdown('- BERTopic model.\n- Topics manually selected, coded, and merged in to these selectable categories.')


def plot():
 
    df = pd.read_csv('forest.csv')
 
    clist = df['cat'].unique().tolist()
 
    cats = st.multiselect("Select topic categories", clist, default = "energy_transports")
    st.markdown("You selected: {}".format(", ".join(cats)))
 
    

    dfs = {cat : df[df['cat'] == cat] for cat in cats} 
    fig = go.Figure()
    for cat, df in dfs.items():
        fig = fig.add_trace(go.Scatter(x=df['date'], y=df['num'], name=cat))
 
    st.plotly_chart(fig, width = 1000)

plot()
