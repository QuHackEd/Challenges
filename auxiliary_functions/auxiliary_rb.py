from pyquil import Program
from pyquil.api import get_qc, WavefunctionSimulator
from pyquil.gates import *
import os, inspect, sys
import numpy as np
from pyquil.noise import append_kraus_to_gate

def define_cliffords_part1():
    clifford_gates = []

    clifford_gates.append(H)
    clifford_gates.append(X)
    clifford_gates.append(Y)
    clifford_gates.append(Z)
    
    return clifford_gates

def dephasing_kraus_map(p):
    return [np.sqrt(1-p)*np.eye(2), np.sqrt(p)*np.diag([1, -1])]

def define_cliffords_part2():
    clifford_gates = []

    clifford_gates.append(H)
    clifford_gates.append(X)
    clifford_gates.append(Y)
    clifford_gates.append(Z)
    
    return clifford_gates

def define_noisy_cliffords(p):
    # We only use some of the clifford for this 
    noisy_clifford_gates = []

    corrupted_H = append_kraus_to_gate(dephasing_kraus_map(p), 1/np.sqrt(2)*np.array([ [1, 1],[1, -1] ]) )
    corrupted_X = append_kraus_to_gate(dephasing_kraus_map(p), np.array([[0, 1], [1, 0]]) )
    corrupted_Y = append_kraus_to_gate(dephasing_kraus_map(p), np.array([[0, -1j], [1j, 0]]) )
    corrupted_Z = append_kraus_to_gate(dephasing_kraus_map(p), np.array([[1, 0], [0, -1]]) )

    noisy_clifford_gates.append(corrupted_H)
    noisy_clifford_gates.append(corrupted_X)
    noisy_clifford_gates.append(corrupted_Y)
    noisy_clifford_gates.append(corrupted_Z)


    return noisy_clifford_gates

def add_noisy_gates_to_circ(circuit, noisy_clifford_gates):
    [corrupted_H,
     corrupted_X,
     corrupted_Y, 
     corrupted_Z] = noisy_clifford_gates
    
    circuit.define_noisy_gate('H', [0], corrupted_H)
    circuit.define_noisy_gate('X', [0], corrupted_X)
    circuit.define_noisy_gate('Y', [0], corrupted_Y)
    circuit.define_noisy_gate('Z', [0], corrupted_Z)

    return circuit


