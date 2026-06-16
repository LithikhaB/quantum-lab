from qiskit.quantum_info import Statevector
from qiskit import QuantumCircuit

def apply_gate(state: Statevector, gate: str) -> Statevector:
    qc = QuantumCircuit(1)

    gateMap = {
        "X": qc.x, "Y": qc.y, "Z": qc.z,
        "H": qc.h, "S": qc.s, "T": qc.t
    }
    gateMap[gate](0)
    return state.evolve(qc)

def measurement_probabilities(state: Statevector) -> dict:
    probs = state.probabilities_dict()

    return {
        "0": probs.get("0", 0.0), "1": probs.get("1", 0.0)
    }

def format_state(state: Statevector) -> str:
    data = state.data
    alpha, beta = data[0], data[1]

    return (
        f"({alpha.real:.3f}"
        f"{alpha.imag:+.3f}i)|0⟩ + "
        f"({beta.real:.3f}"
        f"{beta.imag:+.3f}i)|1⟩"
    )

