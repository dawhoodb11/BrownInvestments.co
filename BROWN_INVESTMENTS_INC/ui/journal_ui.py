import streamlit as st
from core.journal import Journal

def render_journal():
    st.title('Trading Journal')

    j = Journal()

    symbol = st.text_input('Symbol')
    direction = st.selectbox('Direction',['Buy','Sell'])
    result = st.selectbox('Result',['Win','Loss'])

    if st.button('Save'):
        j.log_trade(symbol,direction,result)
        st.success('Saved')
