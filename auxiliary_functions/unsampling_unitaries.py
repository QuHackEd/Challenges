from pyquil import Program
from pyquil.api import get_qc, WavefunctionSimulator, local_qvm
from pyquil.gates import *
from pyquil.parameters import Parameter, quil_sin, quil_cos
from pyquil.quilbase import DefGate
import numpy as np

def state_one_prep(state, qubits):
    if not isinstance(state, Program):
        print("The input *state* must be in the form of a PyQuil Program")
              
    state += H(qubits[0])
    state += CNOT(qubits[0], qubits[1])

    return state
              
def state_two_prep(state, qubits):
    if not isinstance(state, Program):
        print("The input *state* must be in the form of a PyQuil Program")
    # Define the new gate from a matrix
    theta = Parameter('theta')
    crtest = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, quil_cos(theta / 2), -quil_sin(theta / 2)],
        [0, 0, quil_sin(theta / 2), quil_cos(theta / 2)]
    ])

    gate_definition = DefGate('CRTEST', crtest, [theta])
    CRTEST = gate_definition.get_constructor()

    state += gate_definition
    state += H(qubits[0])
    state += Z(qubits[0])
    state += CRTEST(np.pi/42)(qubits[0], qubits[1])
    
    return state

def state_three_prep(state,qubits):
    if not isinstance(state, Program):
        print("The input *state* must be in the form of a PyQuil Program")
    
    state += RX(4/9, qubits[0])
    state += H(qubits[1])
    state += CPHASE(np.pi/6, qubits[0], qubits[1])
    
    return state