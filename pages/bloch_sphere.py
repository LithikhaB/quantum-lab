import streamlit as st

from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector


def initialize_state() -> None:
    if "qubit_state" not in st.session_state:
        st.session_state.qubit_state = Statevector([1, 0])


def render_bloch_sphere() -> None:
    initialize_state()

    st.title("Bloch Sphere")

    st.write(
        "Visualize the current qubit state on the Bloch Sphere."
    )

    state = st.session_state.qubit_state

    fig = plot_bloch_multivector(state)

    st.pyplot(fig)