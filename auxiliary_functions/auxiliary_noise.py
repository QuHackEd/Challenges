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
    corrupted_iH = (1j*1/np.sqrt(2))*np.array([[1, 1-2*p], [1-2*p, 1]])
    corrupted_minusiH = (-1j*1/np.sqrt(2))*np.array([[1, 1-2*p], [1-2*p, 1]])

    corrupted_I = np.array([[1 + p - p, 0], [0, 1 + p - p]])
    corrupted_iZ = np.array([[1j*(1-p+p), 0], [0, 1j*(-1 + p - p)]])
    
    corrupted_iX = 1j*np.array([[0, 1-p+p], [1-p+p, 0]])
    corrupted_minusiX = -1j*np.array([[0, 1-p+p], [1-p+p, 0]])

    corrupted_iY = np.array([[0, (-1j)*(1-2*p)], [(1j)*(1-2*p), 0]])
    corrupted_minusiY = np.array([[0, 1+p-p], [1+p-p, 0]])

    corrupted_phaseS = np.exp(-1j*np.pi/4)*np.array([[(1-p+p), 0], [0, 1j*(1+p - p)]])
    corrupted_phaseminusS = -np.exp(1j*np.pi/4)*np.array([[(1-p+p), 0], [0, 1j*(1+p - p)]])

    corrupted_phaseY = np.exp(-1j*np.pi/4)*np.array([[0, 1-2*p], [1j*(2*p-1), 0]])
    corrupted_phaseminusY = -np.exp(1j*np.pi/4)*np.array([[0, 1-2*p], [1j*(1-2*p), 0]])
    
    corrupted_10 = (1/np.sqrt(2))*np.array([[1, 1-2*p], [2*p-1, 1]])
    corrupted_11 = ( np.exp(-1j*np.pi/4)/np.sqrt(2))*np.array([[1, 1-2*p], [1j*(1+2*p), 1j]])
    
    corrupted_12 = (-np.exp(1j*np.pi/4)/np.sqrt(2))*np.array([[1, 1-2*p], [1j*(1-2*p), 1]])
    corrupted_13 = (1/np.sqrt(2))*np.array([[1, 1-2*p], [2*p-1, 1]])
    corrupted_14 = (1/np.sqrt(2))*np.array([[1, 1-2*p], [2*p-1, 1]])

    ########################################################

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
     
    gate_definition_minusiH = DefGate('NOISY_minusiH', corrupted_minusiH, [p])
    NOISY_minusiH = gate_definition_minusiH.get_constructor()
    
    gate_definition_I = DefGate('NOISY_I', corrupted_I, [p])
    NOISY_I = gate_definition_I.get_constructor()
    
    gate_definition_iZ = DefGate('NOISY_iZ', corrupted_iZ, [p])
    NOISY_iZ = gate_definition_iZ.get_constructor()
    
    gate_definition_iX = DefGate('NOISY_iX', corrupted_iX, [p])
    NOISY_iX = gate_definition_iX.get_constructor()
    
    gate_definition_minusiX = DefGate('NOISY_minusiX', corrupted_minusiX, [p])
    NOISY_minusiX = gate_definition_minusiX.get_constructor()
    
    gate_definition_iY = DefGate('NOISY_iY', corrupted_iY, [p])
    NOISY_iY = gate_definition_iY.get_constructor()
    
    gate_definition_minusiY = DefGate('NOISY_minusiY', corrupted_minusiY, [p])
    NOISY_minusiY = gate_definition_minusiY.get_constructor()
            
    gate_definition_phaseS = DefGate('NOISY_phaseS', corrupted_phaseS, [p])
    NOISY_phaseS = gate_definition_phaseS.get_constructor()
    
    gate_definition_phaseminusS = DefGate('NOISY_phaseminusS', corrupted_phaseminusS, [p])
    NOISY_phaseminusS = gate_definition_phaseminusS.get_constructor()
    
    gate_definition_phaseY = DefGate('NOISY_phaseY', corrupted_phaseY, [p])
    NOISY_phaseY = gate_definition_phaseY.get_constructor()
    
    gate_definition_phaseminusY = DefGate('NOISY_phaseminusY', corrupted_phaseminusY, [p])
    NOISY_phaseminusY = gate_definition_phaseminusY.get_constructor()
    
        
    gate_definition_10 = DefGate('NOISY_10', corrupted_10, [p])
    NOISY_10 = gate_definition_10.get_constructor()
    gate_definition_11 = DefGate('NOISY_11', corrupted_10, [p])
    NOISY_11 = gate_definition_11.get_constructor()   
    gate_definition_12 = DefGate('NOISY_12', corrupted_12, [p])
    NOISY_12 = gate_definition_12.get_constructor()
    
    gate_definition_13= DefGate('NOISY_13', corrupted_13, [p])
    NOISY_13 = gate_definition_13.get_constructor()
    gate_definition_14 = DefGate('NOISY_14', corrupted_14, [p])
    NOISY_14 = gate_definition_14.get_constructor()
    gate_definition_15 = DefGate('NOISY_15', corrupted_15, [p])
    NOISY_15 = gate_definition_15.get_constructor()
    gate_definition_16 = DefGate('NOISY_16', corrupted_16, [p])
    NOISY_16 = gate_definition_16.get_constructor()    
    ########################################################

    noisy_cliffords.append(NOISY_X)
    noisy_cliffords.append(NOISY_H)
    noisy_cliffords.append(NOISY_Z)
    noisy_cliffords.append(NOISY_Y)
    noisy_cliffords.append(NOISY_I)
    noisy_cliffords.append(NOISY_iZ)
    
    noisy_cliffords.append(NOISY_iH)
    noisy_cliffords.append(NOISY_minusiH)
    
    noisy_cliffords.append(NOISY_iX)
    noisy_cliffords.append(NOISY_minusiX)

    noisy_cliffords.append(NOISY_iY)
    noisy_cliffords.append(NOISY_minusiY)

    noisy_cliffords.append(NOISY_phaseS)
    noisy_cliffords.append(NOISY_phaseminusS)
    
    noisy_cliffords.append(NOISY_phaseY)
    noisy_cliffords.append(NOISY_phaseminusY)
    
    noisy_cliffords.append(NOISY_10)
    noisy_cliffords.append(NOISY_11)
    noisy_cliffords.append(NOISY_12)
    noisy_cliffords.append(NOISY_13)
    noisy_cliffords.append(NOISY_14)
    noisy_cliffords.append(NOISY_15)
    noisy_cliffords.append(NOISY_16)

   
    ########################################################
    
    noisy_cliffords_defn.append(gate_definition_X)
    noisy_cliffords_defn.append(gate_definition_H)
    noisy_cliffords_defn.append(gate_definition_Z)
    noisy_cliffords_defn.append(gate_definition_Y)
    noisy_cliffords_defn.append(gate_definition_I)
    noisy_cliffords_defn.append(gate_definition_iZ)
    
    noisy_cliffords_defn.append(gate_definition_iH)
    noisy_cliffords_defn.append(gate_definition_minusiH)

    noisy_cliffords_defn.append(gate_definition_iX)
    noisy_cliffords_defn.append(gate_definition_minusiX)

    noisy_cliffords_defn.append(gate_definition_iY)
    noisy_cliffords_defn.append(gate_definition_minusiY)

    noisy_cliffords_defn.append(gate_definition_phaseS)
    noisy_cliffords_defn.append(gate_definition_phaseminusS)

    noisy_cliffords_defn.append(gate_definition_phaseY)
    noisy_cliffords_defn.append(gate_definition_phaseminusY)

    noisy_cliffords_defn.append(gate_definition_10)
    noisy_cliffords_defn.append(gate_definition_11)
    noisy_cliffords_defn.append(gate_definition_12)
    noisy_cliffords_defn.append(gate_definition_13)
    noisy_cliffords_defn.append(gate_definition_14)
    noisy_cliffords_defn.append(gate_definition_15)
    noisy_cliffords_defn.append(gate_definition_16)


    return noisy_cliffords, noisy_cliffords_defn

def add_noisy_gates_to_circ(circuit, noisy_cliffords_defn, p):
    [gate_definition_X,
     gate_definition_H,
     gate_definition_Z,
     gate_definition_Y, 
     gate_definition_I, 
     gate_definition_iZ,
     gate_definition_iH,
     gate_definition_iminusH,
     gate_definition_iX,
     gate_definition_minusiX,
     gate_definition_iY,
     gate_definition_minusiY,
     gate_definition_phaseS,
     gate_definition_phaseminusS,
     gate_definition_phaseY,
     gate_definition_phaseminusY,
     gate_definition_10, 
     gate_definition_11, 
     gate_definition_12] = noisy_cliffords_defn
    
    circuit += gate_definition_X
    circuit += gate_definition_H
    circuit += gate_definition_Z
    circuit += gate_definition_Y
    circuit += gate_definition_I
    circuit += gate_definition_iZ
    circuit += gate_definition_iH
    circuit += gate_definition_iminusH

    circuit += gate_definition_iX
    circuit += gate_definition_minusiX
    
    circuit += gate_definition_iY
    circuit += gate_definition_minusiY

    circuit += gate_definition_phaseS
    circuit += gate_definition_phaseminusS
    
    circuit += gate_definition_phaseY
    circuit += gate_definition_phaseminusY
    
    circuit += gate_definition_10
    circuit += gate_definition_11
    circuit += gate_definition_12
    circuit += gate_definition_13


    return circuit


