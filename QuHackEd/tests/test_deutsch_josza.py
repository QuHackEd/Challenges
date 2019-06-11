from pyquil.api import WavefunctionSimulator, local_qvm
import math

def test_initial_state(prog):

    wf_sim = WavefunctionSimulator()

    with local_qvm():
        
        state = wf_sim.wavefunction(prog)

        amp = 1

        if abs(state[1].real - amp) < 0.0001:
            print("\nCongratulations, you built the state:")
            print(state)
        else:
            print("oops, you built the state:")
            print(state)
            print("Perhaps an alternative unitary would work?\n")
