from pyquil.api import WavefunctionSimulator, local_qvm
import math

def test_bell_state_unitary(prog, flag):

    wf_sim = WavefunctionSimulator()

    with local_qvm():
        
        state = wf_sim.wavefunction(prog)

        amp_plus = 1/math.sqrt(2)
        amp_minus = -1/math.sqrt(2)

        if (flag == 'phi+'):
            if (abs(state[0].real - amp_plus) < 0.0001) and (abs(state[-1].real - amp_plus) < 0.0001):
                print("\nCongratulations, you built the state:")
                print(state)
            else:
                print("oops, you built the state:")
                print(state)
                print("Perhaps an alternative unitary would work?\n")

        elif (flag == 'phi-'):
            if (abs(state[0].real - amp_plus) < 0.0001) and (abs(state[-1].real - amp_minus) < 0.0001):
                print("\nCongratulations, you built the state:")
                print(state)
            else:
                print("oops, you built the state:")
                print(state)
                print("Perhaps an alternative unitary would work?\n")


        elif (flag == 'psi+'):
            if (abs(state[1].real - amp_plus) < 0.0001) and (abs(state[-2].real - amp_plus) < 0.0001):
                print("\nCongratulations, you built the state:")
                print(state)
            else:
                print("oops, you built the state:")
                print(state)
                print("Perhaps an alternative unitary would work?\n")

        elif (flag == 'psi-'):
            if (abs(state[1].real - amp_plus) < 0.0001) and (abs(state[-2].real - amp_minus) < 0.0001):
                print("\nCongratulations, you built the state:")
                print(state)
            else:
                print("oops, you built the state:")
                print(state)
                print("Perhaps an alternative unitary would work?\n")
        else: raise ValueError('The inputted flag choice is not supported')

def test_two_qubit_state_change(prog):

    wf_sim = WavefunctionSimulator()

    with local_qvm():
        
        state = wf_sim.wavefunction(prog)

        amp_cos = (1/math.sqrt(2))*math.cos(math.pi/14)
        amp_sin = (1/math.sqrt(2))*math.sin(math.pi/14)

        if (abs(state[0].real - amp_cos) < 0.0001) and (abs(state[-1].real + amp_sin) < 0.0001):
            print(state[1], 'sin is:', amp_sin)
            print(state[2], 'cos is:', amp_cos)
            if (abs(state[1].real - amp_sin) < 0.0001) and (abs(state[2].real - amp_cos) < 0.0001):
                print(state[1], 'sin is:', amp_sin)
                print(state[2], 'cos is:', amp_cos)
                print("\nNice one, you built the state:")
                print(state)
            else:
                print("oops, you built the state:")
                print(state)
                print("Try again...\n")
        else:
            print("oops, you built the state:")
            print(state)
            

def test_two_qubit_reset(prog):

    wf_sim = WavefunctionSimulator()

    with local_qvm():
        
        state = wf_sim.wavefunction(prog)

        amp = 1
        
        if (abs(state[0].real - amp) < 0.0001):
            print("\nGood job, you built the state:")
            print(state)
        else:
            print("Unfortunately, you built the state:")
            print(state)
            print("Possibly try some other unitary?\n")
            