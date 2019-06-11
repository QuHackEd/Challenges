
# # Challenge: The Infamous Deutsch Josza Algorithm


# In this challenge, you will implement the Deutsch Josza Algorithm, one of the 
# first algorithms which was developed to show an exponential improvement over a classical 
# task.

# ### Problem:
# You are given a function, $f(x)$, and told that this function is either:
# * *constant* on all inputs x - Meaning $f(x) = 0$ **or** $f(x) = 1$, $\forall x \in \{0, 1\}^{n}$
# or
# * *balanced* -  Meaning $f(x) = 0$ for **exactly** half the inputs x, and $f(x) = 1$ for the other half.

# You have to determine which of the above describes the function $f$.
# (Note: Since you are given the promise, $f$ falls *exactly* into one of the categories above, it cannot be 
# anything else.)

## Step 1

# For this we must use $n$ qubits, and one extra qubit, an *ancilla*.

# The first $n$ qubits are initialised in the state $|0\rangle$, while the ancilla is in the 
# state $|1\rangle$.

# #### Task
# Prepare a circuit (program) which prepares the following state:
# $|0\rangle^{\otimes n}|1\rangle$

# (Take $n=5$ for this example)

#Import the required things you may need here

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

circuit = Program()

qc = get_qc('6q-qvm')

qubits = qc.qubits()

circuit += X(qubits[-1]) #Flip ancilla qubit