import streamlit as st
from utils.entanglement_helpers import (create_bell_state, simulate_measurement)

def initialize_lab() -> None:
    if "bell_state" not in st.session_state:
        circuit, state = create_bell_state()
        st.session_state.bell_circuit = circuit
        st.session_state.bell_state = state

    if "measurement_result" not in st.session_state:
        st.session_state.measurement_result = None
    
def render_circuit() -> None:
    st.subheader("Bell State Circuit")

    st.code(
        """
q0: ──H────■──
           │
q1: ───────X──
        """
    )

def render_statevector() -> None:
    state = st.session_state.bell_state
    st.subheader("Quantum State")
    st.latex(r"\frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)")

def render_measurement() -> None:
    if st.button("Measure Entangled Pair"):
        st.session_state.measurement_result = simulate_measurement()
        st.rerun()

def render_results() -> None:
    result = st.session_state.measurement_result

    if result is None: return 
    qa, qb = result

    st.subheader("Measurement Results")
    col1, col2 = st.columns(2)

    col1.metric("Qubit A", qa)
    col2.metric("Qubit B", qb)

    st.success("The measurements are perfectly correlated because the qubits are entangled.")

def render_reset() -> None:
    if st.button("Reset Lab"):
        circuit, state = create_bell_state()

        st.session_state.bell_circuit = circuit
        st.session_state.bell_state = state
        st.session_state.measurement_result = None

        st.rerun()

def render_entanglement_lab() -> None:
    initialize_lab()
    st.title("Entanglement Lab")
    st.write("""
Explore Bell States and quantum entanglement.

A Bell State is created using:

1. Hadamard Gate
2. CNOT Gate

The resulting qubits become entangled.
             """)
    
    render_circuit()
    st.divider()

    render_statevector()
    st.divider()

    render_measurement()
    render_results()
    st.divider()

    render_reset()


render_entanglement_lab()