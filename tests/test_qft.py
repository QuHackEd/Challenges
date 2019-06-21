import numpy as np

from pyquil import Program
from pyquil.api import get_qc, WavefunctionSimulator, local_qvm
from pyquil.gates import *

import math
make_wf = WavefunctionSimulator()

def test_prep_comp_bitstring(circuit, bitstring):
    
    with local_qvm():
        wavefunc = make_wf.wavefunction(circuit)
    probs = wavefunc.get_outcome_probs()
    
    bitstring_as_str = "".join(str(x) for x in list(bitstring))[::-1]
    
    if probs[bitstring_as_str] != 1:
        print("It doens't look like the correct state was produced :( ")
    else: print("Congrats, you prepared the correct state!")
        
def test_zero_output_state(wavefunction):
  
    amp_plus  = 1/math.sqrt(2)
    amp_minus = -1/math.sqrt(2)
    
    if abs(wavefunction[0].real - amp_plus) < 0.0001:
        if abs(wavefunction[1].real - amp_plus) < 0.0001:
            print("\nCongratulations, this state is correct:")
            print("\nThis correponds to the phase exp(2\pi i * 0/2) = +1")
        else:
            print("oops, you built the state:")
            print(wavefunction)
            print("Perhaps an alternative unitary would work?\n")

    else:
        print("oops, you built the state:")
        print(wavefunction)
        print("Perhaps an alternative unitary would work?\n")

           
def test_one_output_state(wavefunction):
  
    amp_plus  = 1/math.sqrt(2)
    amp_minus = -1/math.sqrt(2)

    if abs(wavefunction[0].real - amp_plus) < 0.0001:
        if abs(wavefunction[1].real - amp_minus) < 0.0001:
            print("\nCongratulations, this state is correct:")
            print("\nThis correponds to the phase exp(2\pi i * 1/2) = -1")
  
        else:
            print("oops, you built the state:")
            print(wavefunction)
            print("Perhaps an alternative unitary would work?\n")

    else:
        print("oops, you built the state:")
        print(wavefunction)
        print("Perhaps an alternative unitary would work?\n")
