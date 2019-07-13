from pyquil.api import WavefunctionSimulator, local_qvm
import math
import numpy as np

def test_bit_flip_unitary(prog):

    wf_sim = WavefunctionSimulator()

    with local_qvm():
        if len(prog._instructions) == 0:
            print("Hmm, I'm not sure you have any gates applied to the state. Better add some..") 
        else:    
            state = wf_sim.wavefunction(prog)

            if abs(state[1].real - 1) < 0.0001:
                print("\nCongratulations, you built the state:")
                print(state)
            else:
                print("oops, you built the state:")
                print(state)
                print("Perhaps an alternative unitary would work?\n")

def test_superposition_unitary(prog):
    wf_sim = WavefunctionSimulator()
   
    with local_qvm():
        if len(prog._instructions) == 0:
            print("Hmm, I'm not sure you have any gates applied to the state. Better add some..") 
        else:    
            state = wf_sim.wavefunction(prog)

            amp_plus    = 1 / math.sqrt(2)
            amp_minus   = - 1 / math.sqrt(2)
            if abs(state[0].real - amp_plus) < 0.0001 and abs(state[1].real - amp_plus) < 0.0001:
                print("\nGood job! You built the superposition state:")
                print(state)

            elif abs(state[0].real - amp_plus) < 0.0001 and abs(state[1].real - amp_minus) < 0.0001:
                print("\nNot quite :(, you built a different superposition state:")
                print(state)

            elif abs(state[0].real - amp_minus) < 0.0001 and abs(state[1].real - amp_plus) < 0.0001:
                print("\nNot quite :(, you built a different superposition state:")
                print(state)

            elif abs(state[0].real - amp_minus) < 0.0001 and abs(state[1].real - amp_minus) < 0.0001:
                print("\nNot quite :(, you built a different superposition state:")
                print(state)
                print("This state is actually physically indistinguisable from the correct state up to a global phase. However, it's still not quite right.")

            else:
                print("\nHmm, you built the state:")
                print(state)
                print("Maybe try a different gate?\n")

def test_plus_input_to_zero(prog):

    wf_sim = WavefunctionSimulator()

    with local_qvm():
        if len(prog._instructions) == 0:
            print("Hmm, I'm not sure you have any gates applied to the state. Better add some..") 
        else:    
            state = wf_sim.wavefunction(prog)
            if abs(state[0].real - 1) < 0.0001:
                print("\nExcellent! You built the state:")
                print(state)

            else:
                print("oops, you built the state:")
                print(state)
                print("Perhaps an alternative unitary would work?\n")

                
def test_minus_input_to_zero(prog):

    wf_sim = WavefunctionSimulator()

    with local_qvm():
        if len(prog._instructions) == 0:
            print("Hmm, I'm not sure you have any gates applied to the state. Better add some..") 
        else:    
            state = wf_sim.wavefunction(prog)

            if abs(state[0].real - 1) < 0.0001:
                print("\nExcellent! You built the state:")
                print(state)

            else:
                print("oops, you built the state:")
                print(state)
                print("Perhaps an alternative unitary would work?\n")
                
def test_minus_input_to_one(prog):

    wf_sim = WavefunctionSimulator()

    with local_qvm():
        if len(prog._instructions) == 0:
            print("Hmm, I'm not sure you have any gates applied to the state. Better add some..") 
        else:    
            state = wf_sim.wavefunction(prog)
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
                
                
def test_one_phase(prog):
    
    wf_sim = WavefunctionSimulator()

    with local_qvm():
        if len(prog._instructions) == 0:
            print("Hmm, I'm not sure you have any gates applied to the state. Better add some..") 
        else:    
            state = wf_sim.wavefunction(prog)

            amp = -1
            if abs(state[1].real - amp) < 0.0001:
                print("\nCongratulations, you built the state:")
                print(state)
            else:
                print("oops, you built the state:")
                print(state)
                print("Perhaps an alternative unitary would work?\n")

def test_pi_three_phase(prog):
    
    wf_sim = WavefunctionSimulator()
    print('This is happening')
    with local_qvm():
        if len(prog._instructions) == 0:
            print("Hmm, I'm not sure you have any gates applied to the state. Better add some..") 
        else:    
            state = wf_sim.wavefunction(prog)

            amp_plus    = 1 / math.sqrt(2)
            amp_phase   = np.exp(1j*np.pi/3) / math.sqrt(2)

            if abs(state[0].real - amp_plus) < 0.0001 and abs(state[1].real - amp_phase.real) < 0.0001 and abs(state[1].imag - amp_phase.imag) < 0.0001:
                print("\nGood job! You built the state with the relative phase:")
                print(state)

            else:
                print("\nHmm, you built the state:")
                print(state)
                print("Maybe try a different gate?\n")