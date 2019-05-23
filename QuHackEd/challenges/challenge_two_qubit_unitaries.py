from pyquil import Program
from pyquil.api import get_qc, WavefunctionSimulator
from pyquil.gates import *
import os, inspect, sys

module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from tests.test_two_qubit_unitaries import *

from auxiliary_functions.auxiliary_unitaries import plus_prep, minus_prep

# Initialise an empty circuit: 

circuit = Program()

# The circuit now contains a quantum register in the 
# state |0>.
# Apply a unitary gate (or gates) such that the output state is 1/\sqrt(2)(|00>+|11>)
# Also known as one of the Bell States.

circuit += H(0)
circuit += CNOT(0, 1)

# You can check if the output state if correct by printing 
# out the wavefunction of the state using a simulator.
make_wf = WavefunctionSimulator()

wavefunction = make_wf.wavefunction(circuit)
print('The wavefunction is:', wavefunction)

test_bell_state_unitary(circuit)