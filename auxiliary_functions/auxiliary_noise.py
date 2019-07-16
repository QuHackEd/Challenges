from pyquil import Program
from pyquil.api import get_qc, WavefunctionSimulator
from pyquil.gates import *
import os, inspect, sys
import numpy as np
from pyquil.noise import append_kraus_to_gate
from pyquil.quilbase import DefGate
from pyquil.parameters import Parameter


# Define the sequence of noisy clifford operations here.

def define_noisy_cliffords(p):
    p = Parameter('p')
    noisy_cliffords = []
    noisy_cliffords_defn = []
    
    corrupted_X = np.array([[0, 1-p], [1-p, 0]])
    corrupted_Y = np.array([[0, (-1j)*(1-2*p)], [(1j)*(1-2*p), 0]])
    corrupted_Z = np.array([[1-p+p, 0], [0, -1 + p - p]])
    corrupted_H = (1/np.sqrt(2))*np.array([[1, 1-2*p], [1-2*p, 1]])
    corrupted_iH = (-1j*1/np.sqrt(2))*np.array([[1, 1-2*p], [1-2*p, 1]])

    corrupted_I = np.array([[1 + p - p, 0], [0, 1 + p - p]])
    corrupted_iZ = np.array([[1j*(1-p+p), 0], [0, 1j*(-1 + p - p)]])
    corrupted_iX = np.array([[0, 1-p], [1-p, 0]])

    corrupted_iY = np.array([[0, (-1j)*(1-2*p)], [(1j)*(1-2*p), 0]])

    corrupted_phaseS = np.array([[np.exp(-1j*np.pi/4)(1-p+p), 0], [0, np.exp(-1j*np.pi/4)*1j*(1+p - p)]])
    corrupted_phaseminusS = np.array([[np.exp(1j*np.pi/4)(1-p+p), 0], [0, -np.exp(1j*np.pi/4)*1j*(1+p - p)]])

    gate_definition_X = DefGate('NOISY_X', corrupted_X, [p])
    NOISY_X = gate_definition_X.get_constructor()

    gate_definition_Y = DefGate('NOISY_Y', corrupted_Y, [p])
    NOISY_Y = gate_definition_Y.get_constructor()

    gate_definition_Z = DefGate('NOISY_Z', corrupted_Z, [p])
    NOISY_Z = gate_definition_Z.get_constructor() 

    gate_definition_H = DefGate('NOISY_H', corrupted_H, [p])
    NOISY_H = gate_definition_H.get_constructor()
     
    gate_definition_iH = DefGate('NOISY_iH', corrupted_iH, [p])
    NOISY_iH = gate_definition_iH.get_constructor()
    
    gate_definition_I = DefGate('NOISY_I', corrupted_I, [p])
    NOISY_I = gate_definition_I.get_constructor()
    
    gate_definition_iZ = DefGate('NOISY_iZ', corrupted_iZ, [p])
    NOISY_iZ = gate_definition_iZ.get_constructor()
    
    gate_definition_iX = DefGate('NOISY_iX', corrupted_iX, [p])
    NOISY_iX = gate_definition_iX.get_constructor()
    
    gate_definition_iY = DefGate('NOISY_iY', corrupted_iY, [p])
    NOISY_iY = gate_definition_iY.get_constructor()
        
    gate_definition_phaseS = DefGate('NOISY_phaseS', corrupted_phaseS, [p])
    NOISY_phaseS = gate_definition_phaseS.get_constructor()
    
    gate_definition_phaseminusS = DefGate('NOISY_phaseminusS', corrupted_phaseminusS, [p])
    NOISY_phaseminusS = gate_definition_phaseminusS.get_constructor()
    
    
    noisy_cliffords.append(NOISY_X)
    noisy_cliffords.append(NOISY_H)
    noisy_cliffords.append(NOISY_Z)
    noisy_cliffords.append(NOISY_Y)
    noisy_cliffords.append(NOISY_I)
    noisy_cliffords.append(NOISY_iZ)
    noisy_cliffords.append(NOISY_iH)
    noisy_cliffords.append(NOISY_iX)
    noisy_cliffords.append(NOISY_iY)

    noisy_cliffords.append(NOISY_phaseS)
    noisy_cliffords.append(NOISY_phaseminusS)

    noisy_cliffords_defn.append(gate_definition_X)
    noisy_cliffords_defn.append(gate_definition_H)
    noisy_cliffords_defn.append(gate_definition_Z)
    noisy_cliffords_defn.append(gate_definition_Y)
    noisy_cliffords_defn.append(gate_definition_I)
    noisy_cliffords_defn.append(gate_definition_iZ)
    noisy_cliffords_defn.append(gate_definition_iH)
    noisy_cliffords_defn.append(gate_definition_iX)
    noisy_cliffords_defn.append(gate_definition_iY)

    noisy_cliffords_defn.append(gate_definition_phaseS)
    noisy_cliffords_defn.append(gate_definition_phaseminusS)

    return noisy_cliffords, noisy_cliffords_defn

def add_noisy_gates_to_circ(circuit, noisy_cliffords_defn, p):
    [gate_definition_X,
     gate_definition_H,
     gate_definition_Z,
     gate_definition_Y, 
     gate_definition_I, 
     gate_definition_iZ,
     gate_definition_iH,
     gate_definition_iX,
     gate_definition_iY,
     gate_definition_phaseS] = noisy_cliffords_defn
    
    circuit += gate_definition_X
    circuit += gate_definition_H
    circuit += gate_definition_Z
    circuit += gate_definition_Y
    circuit += gate_definition_I
    circuit += gate_definition_iZ
    circuit += gate_definition_iH
    circuit += gate_definition_iX
    circuit += gate_definition_iY
    circuit += gate_definition_phaseS

    return circuit


