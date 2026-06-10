import streamlit as st
from ui.dashboard import render_dashboard
from ui.smc_dashboard import render_smc
from ui.risk_dashboard import render_risk
from ui.journal_ui import render_journal

st.set_page_config(page_title='BROWN INVESTMENTS INC', layout='wide')

st.sidebar.title('BROWN INVESTMENTS INC')

menu = st.sidebar.selectbox('NAVIGATION', [
    'Dashboard',
    'SMC Engine',
    'Risk Management',
    'Trading Journal'
])

if menu == 'Dashboard':
    render_dashboard()
elif menu == 'SMC Engine':
    render_smc()
elif menu == 'Risk Management':
    render_risk()
elif menu == 'Trading Journal':
    render_journal()
