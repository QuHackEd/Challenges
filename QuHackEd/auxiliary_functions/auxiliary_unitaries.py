from pyquil import Program
from pyquil.api import get_qc, WavefunctionSimulator
from pyquil.gates import *
import os, inspect, sys


def plus_prep():
    state = Program()

    state += H(0)

    return state


def minus_prep():
    state = Program()
    
    state += X(0)
    state += H(0)
    
    return state