import streamlit as st

from utils.algorithms_helpers import (deutsch_algorithm, bernstein_vazirani)

def render_algorithms() -> None:
    st.title("Quantum Algorithms")

    tab1, tab2 = st.tabs(["Deutsch", "Bernstein-Vazirani"])

    with tab1:
        st.subheader("Deutsch Algorithm")
        st.write("Determine whether a function is constant or balanced using quanum computation.")
        if st.button("Run Deutsch Algorithm"):
            result = deutsch_algorithm()
            st.success(result)

    with tab2:
        st.subheader("Bernstein-Vazirani Algorithm")
        secret = st.text_input("Secret Binary String", value="1011")

        if st.button("Recover Secret String"):
            result = bernstein_vazirani(secret)
            st.success(f"Recovered: {result}")

render_algorithms()