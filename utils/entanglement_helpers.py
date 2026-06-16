from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
import random

def create_bell_state() -> tuple[QuantumCircuit, Statevector]:
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)

    state = Statevector.from_instruction(qc)
    return qc, state

def simulate_measurement() -> tuple[int, int]:
    res = random.choice([0, 1])
    return res, res