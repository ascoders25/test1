import streamlit as st

if st.button('Circle'):
    st.write('まる')

elif st.button('Rect'):
    st.write('四角')

else:
    st.write('それ以外')