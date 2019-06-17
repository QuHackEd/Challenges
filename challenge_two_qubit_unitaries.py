from pyquil import Program
from pyquil.api import get_qc, WavefunctionSimulator
from pyquil.gates import *
import os, inspect, sys
import numpy as np
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from tests.test_two_qubit_unitaries import test_bell_state_unitary, test_two_qubit_reset, test_two_qubit_state_change

from auxiliary_functions.auxiliary_unitaries import two_qubit_prod_prep
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
print('\nThe wavefunction is:', wavefunction)

test_bell_state_unitary(circuit, 'phi+')

# Initialise an empty circuit: 

circuit = Program()

# The circuit now contains a quantum register in the 
# state |0>.
# Apply a unitary gate (or gates) such that the output state is 1/\sqrt(2)(|00>-|11>)
# Also known as one of the Bell States.

circuit += H(0)
circuit += CNOT(0, 1)
circuit += Z(1)

# You can check if the output state if correct by printing 
# out the wavefunction of the state using a simulator.
make_wf = WavefunctionSimulator()

wavefunction = make_wf.wavefunction(circuit)
print('\nThe wavefunction is:', wavefunction)

test_bell_state_unitary(circuit, 'phi-')


# Initialise an empty circuit: 

circuit = Program()

# The circuit now contains a quantum register in the 
# state |0>.
# Apply a unitary gate (or gates) such that the output state is 1/\sqrt(2)(|01>+|10>)
# Also known as one of the Bell States.

circuit += X(1)
circuit += H(0)
circuit += CNOT(0, 1)

# You can check if the output state if correct by printing 
# out the wavefunction of the state using a simulator.
make_wf = WavefunctionSimulator()

wavefunction = make_wf.wavefunction(circuit)
print('\nThe wavefunction is:', wavefunction)

test_bell_state_unitary(circuit, 'psi+')

#Initialise the state in the desired form

circuit =  Program()
circuit += two_qubit_prod_prep(np.pi/7)
print(make_wf.wavefunction(circuit))
# The circuit now contains a quantum register in the 
# state |phi> = (cos(theta/2)|0> + sin(theta/2)|1>) x |+> =
# 1/\sqrt(2)*(cos(\theta/2)|00> + cos(theta/2)|01> + sin(theta/2)|10> + sin(/2)|11> ),
# where theta = np.pi/7.

# Task 1:
# Apply a unitary gate (or gates) such that the output state is:
# 1/\sqrt(2)*(cos(\theta/2)|00> + cos(theta/2)|01> + sin(theta/2)|10> - sin(theta/2)|11> )

# Task 2:
# Now apply unitary gates to return the state to the |00> state.

circuit += CZ(0,1)

test_two_qubit_state_change(circuit)

# You can check if the output state if correct by printing 
# out the wavefunction of the state using a simulator.
make_wf = WavefunctionSimulator()

wavefunction = make_wf.wavefunction(circuit)
print('\nThe wavefunction is:', wavefunction)
 
# Now take the same state and return it to the |00> state
# Hint: First you will need to undo the last gate you applied

circuit += CZ(0,1)
circuit += H(1)
circuit += RY(-np.pi/7, 0)

test_two_qubit_reset(circuit)