from pyquil import Program
from pyquil.api import get_qc, WavefunctionSimulator
from pyquil.gates import *
import os, inspect, sys
import numpy as np
from pyquil.noise import append_kraus_to_gate
from pyquil.quilbase import DefGate
from pyquil.parameters import Parameter


# Define the sequence of noisy clifford operations here.

def define_noisy_cliffords(circuit, p):
    p = Parameter('p')
    noisy_cliffords = []
    noisy_cliffords_defn = []
    corrupted_X = np.array([[0, 1-p], [1-p, 0]])
    corrupted_Z = np.array([[1, 0], [0, -1]])
    corrupted_H = (1/np.sqrt(2))*np.array([[1, 1-2*p], [1-2*p, 1]])

    gate_definition_X = DefGate('NOISY_X', corrupted_X, [p])
    NOISY_X = gate_definition_X.get_constructor()
    
    gate_definition_Z = DefGate('NOISY_Z', corrupted_Z)
    NOISY_Z = gate_definition_Z.get_constructor() 
    
    gate_definition_H = DefGate('NOISY_H', corrupted_H, [p])
    NOISY_H = gate_definition_H.get_constructor()

    noisy_cliffords.append(NOISY_X)
    noisy_cliffords.append(NOISY_Z)
    noisy_cliffords.append(NOISY_H)
    
#     noisy_cliffords_defn.append(gate_definition_X)
#     noisy_cliffords_defn.append(gate_definition_Z)
#     noisy_cliffords_defn.append(gate_definition_H)
    
    circuit += gate_definition_X
    circuit += gate_definition_Z
    circuit += gate_definition_H
    
    return circuit, noisy_cliffords

# def define_noisy_gates_in_circuit(circuit, noisy_cliffords_defn):
#     # Override noiseless clifford gates in circuit with dephased versions
#     # when they are applied
    
#     [gate_definition_X, gate_definition_Z, gate_definition_H] = noisy_cliffords_defn
#     circuit += gate_definition_X
#     circuit += gate_definition_Z
#     circuit += gate_definition_H
  
#     return circuit