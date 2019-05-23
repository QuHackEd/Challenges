from challenges.challenge1_measurement import measurement_1, measurement_2
from pyquil.api import WavefunctionSimulator, local_qvm
import math
import numpy as np

def test_meas_outcome(results):
    print('fuck ya')
    if type(results) is not np.ndarray:
        print("Type Error: Did you measure in the correct way?")
    else: print('fuck ya')
