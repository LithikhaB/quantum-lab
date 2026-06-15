# Quantum Lab ⚛️

Quantum Lab is an interactive web application for exploring the fundamentals of quantum computing through simulations and visualizations.

The project is designed as a hands-on learning environment where users can experiment with qubits, quantum gates, entanglement, and foundational quantum algorithms without requiring access to real quantum hardware.

## Features

### Qubit Playground

* Create and manipulate qubit states
* Apply quantum gates (X, Y, Z, H, S, T)
* Observe state evolution and measurement probabilities

### Bloch Sphere Visualization

* Visualize qubit states on the Bloch Sphere
* Understand how quantum gates transform qubits

### Entanglement Lab

* Create Bell States
* Explore quantum entanglement
* Observe measurement correlations

### Quantum Algorithms

* Deutsch Algorithm
* Deutsch–Jozsa Algorithm
* Bernstein–Vazirani Algorithm

## Tech Stack

* Python
* Qiskit
* Streamlit
* Plotly

## Project Structure

```text
quantum-lab/

├── app.py
├── requirements.txt
├── README.md
│
├── pages/
│   ├── qubit_playground.py
│   ├── bloch_sphere.py
│   ├── entanglement_lab.py
│   └── algorithms.py
│
└── utils/
```

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/quantum-lab.git
cd quantum-lab
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment:

### Windows

```powershell
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## Learning Objectives

This project explores:

* Qubits and superposition
* Quantum gates and state transformations
* Measurement and probability amplitudes
* Entanglement and Bell States
* Fundamental quantum algorithms

## Future Enhancements

* Interactive circuit builder
* Quantum teleportation simulator
* Quantum Fourier Transform visualization
* Grover's Search visualization
* Real IBM Quantum backend integration
