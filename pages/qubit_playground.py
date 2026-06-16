import streamlit as st
from qiskit.quantum_info import Statevector

from utils.quantum_helpers import(apply_gate, measurement_probabilities, format_state)

def initialize_state() -> None:
    if "qubit_state" not in st.session_state:
        st.session_state.qubit_state = Statevector([1, 0])

def render_gate_buttons() -> None:
    gates = ["X", "Y", "Z", "H", "S", "T"]
    cols = st.columns(len(gates))

    for col, gate in zip(cols, gates):
        if col.button(gate, use_container_width=True):
            st.session_state.qubit_state = apply_gate(
                st.session_state.qubit_state,
                gate,
            )
            st.rerun()

def render_state() -> None:
    state = st.session_state.qubit_state 
    st.subheader("Current State")
    st.code(format_state(state), language="text")

def render_probabilities() -> None:
    state = st.session_state.qubit_state
    probs = measurement_probabilities(state)

    st.subheader("Measurement Probabilities")

    st.metric("P(0)", f"{probs['0']:.4f}")
    st.metric("P(1)", f"{probs['1']:.4f}")

def render_reset() -> None:
    if st.button("Reset Qubit"):
        st.session_state.qubit_state = Statevector([1, 0])
        st.rerun()

def render_qubit_playground() -> None:
    initialize_state()

    st.title("Qubit Playground")
    st.write("Apply quantum gates and observe how the qubit state changes.")

    render_gate_buttons()
    st.divider()

    render_state()
    st.divider()

    render_probabilities()
    st.divider()

    render_reset()