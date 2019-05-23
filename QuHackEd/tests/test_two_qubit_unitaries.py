from pyquil.api import WavefunctionSimulator, local_qvm
import math

def test_bit_flip_unitary(prog):

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

def test_superposition_unitary(prog):
    wf_sim = WavefunctionSimulator()
   
    with local_qvm():
        
        state = wf_sim.wavefunction(prog)

        amp = 1 / math.sqrt(2)

        if abs(state[0].real - amp) < 0.0001 and abs(state[1].real - amp) < 0.0001:
            print("\nGood job, you built the superposition state:")
            print(state)
        else:
            print("\nhmm, you built the state:")
            print(state)
            print("Maybe try a different gate?\n")

def test_plus_input_to_zero(prog):

    wf_sim = WavefunctionSimulator()

    with local_qvm():
        
        state = wf_sim.wavefunction(prog)

        amp = 1

        if abs(state[0].real - amp) < 0.0001:
            print("\nExcellent! You built the state:")
            print(state)

        else:
            print("oops, you built the state:")
            print(state)
            print("Perhaps an alternative unitary would work?\n")

def test_minus_input_to_zero(prog):

    wf_sim = WavefunctionSimulator()

    with local_qvm():
        
        state = wf_sim.wavefunction(prog)
        dir(prog)
        amp = 1

        if abs(state[0].real - amp) < 0.0001:
            print("\nExcellent! You built the state:")
            print(state)
        elif abs(state[1].real - amp) < 0.0001 and len(prog._instructions) < 4:
            print("\nAh shucks, you made:")
            print(state)
            print("Maybe you need more gates?")
        else:
            print("oops, you built the state:")
            print(state)
            print("Perhaps an alternative unitary would work?\n")
