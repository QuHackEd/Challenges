from pyquil import Program
from pyquil.api import get_qc, WavefunctionSimulator
from pyquil.gates import *
import os, inspect, sys
import numpy as np
from pyquil.noise import append_kraus_to_gate

# Define function to return the operators sqrt(p)I, sqrt(1-p)Z
def dephasing_kraus_map(p):

    return [np.sqrt(1-p)*np.eye(2), np.sqrt(p)*np.diag([1, -1])]

# Define the sequence of noisy clifford operations here.

def define_noisy_cliffords(p):
    noisy_cliffords = []
    corrupted_X = append_kraus_to_gate(dephasing_kraus_map(p), np.array([[0, 1], [1, 0]]))
    corrupted_Z = append_kraus_to_gate(dephasing_kraus_map(p), np.array([[1, 0], [0, -1]]))
    corrupted_H = append_kraus_to_gate(dephasing_kraus_map(p), 1/np.sqrt(2)*np.array([[1, 1], [1, -1]]))

    noisy_cliffords.append(corrupted_X)
    noisy_cliffords.append(corrupted_Z)
    noisy_cliffords.append(corrupted_H)

    return noisy_cliffords

def override_cliffords_in_circuit(circuit, noisy_cliffords):
    # Override noiseless clifford gates in circuit with dephased versions
    # when they are applied
    
    [corrupted_X, corrupted_Z, corrupted_H] = noisy_cliffords
    noisy_x =  circuit.define_noisy_gate("X", [0], corrupted_X)
    noisy_z =  circuit.define_noisy_gate("Z", [0], corrupted_Z)
    noisy_h =  circuit.define_noisy_gate("H", [0], corrupted_H)

    return circuit