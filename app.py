import streamlit as st

from pages.qubit_playground import render_qubit_playground
from pages.bloch_sphere import render_bloch_sphere
from pages.entanglement_lab import render_entanglement_lab
from pages.algorithms import render_algorithms

st.set_page_config(
    page_title="Quantum Concepts Explorer",
    page_icon="⚛️",
    layout="wide",
)

PAGES = {
    "Home": None,
    "Qubit Playground": render_qubit_playground,
    "Bloch Sphere": render_bloch_sphere,
    "Entanglement Lab": render_entanglement_lab,
    "Algorithms": render_algorithms,
}

st.sidebar.title("Quantum Lab")
selection = st.sidebar.radio(
    "Navigate",
    list(PAGES.keys()),
)

if selection == "Home":
    st.title("Quantum Concepts Explorer")

    st.markdown(
        """
        Explore fundamental concepts in quantum computing through
        interactive simulations and visualizations.

        ### Modules

        - Qubit Playground
        - Bloch Sphere Visualization
        - Entanglement Lab
        - Quantum Algorithms

        ### Technologies

        - Python
        - Qiskit
        - Streamlit
        - Plotly
        """
    )

    st.info(
        "Day 1: Project structure and navigation setup." \
        "Day 2: Qubit Playground" \
        "Day 3: Bloch Sphere Viz."
    )
else:
    PAGES[selection]()