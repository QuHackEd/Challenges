from pyquil import Program
from pyquil.api import get_qc, WavefunctionSimulator
from pyquil.gates import *
import numpy as np
import os, inspect, sys

module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from tests.test_single_qubit_unitaries import *

from auxiliary_functions.auxiliary_unitaries import plus_prep, minus_prep

# Initialise an empty circuit: 

circuit = Program()

# The circuit now contains a quantum register in the 
# state |0>.
# Apply a unitary gate (or gates) such that the output state is |1>

circuit += X(0)


# You can check if the output state if correct by printing 
# out the wavefunction of the state using a simulator.
make_wf = WavefunctionSimulator()

wavefunction = make_wf.wavefunction(circuit)
print('The wavefunction is:', wavefunction)

test_bit_flip_unitary(circuit)

# Initialise an empty circuit: 

circuit = Program()

# The circuit now contains a quantum register in the 
# state |0>.
# Apply a unitary gate (or gates) such that the output state is |+>
circuit += H(0)

test_superposition_unitary(circuit)


# Initialise a |+> state: 

circuit = plus_prep()

# The circuit now contains a quantum register in the 
# state |+>.
# Apply a unitary gate (or gates) such that the output state is |0>

circuit += H(0)

test_plus_input_to_zero(circuit)

# Initialise a |-> state: 

circuit = minus_prep()
print(circuit._instructions)
# The circuit now contains a quantum register in the 
# state |-> = 1/\sqrt(2)(|0> - |1>).
# Apply a unitary gate (or gates) such that the output state is |0>

circuit += H(0)
circuit += X(0)

test_minus_input_to_one(circuit)