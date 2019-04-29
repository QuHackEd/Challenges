from pyquil.api import WavefunctionSimulator, local_qvm
import math

def test_state(prog):

    wf_sim = WavefunctionSimulator()

    with local_qvm():
        
        state = wf_sim.wavefunction(prog)

        amp = 1 / math.sqrt(2)

        if abs(state[0].real - amp) < 0.0001 and abs(state[1].real - amp) < 0.0001:
            print("Congratulations, you built the state")
            print(state)
        else:
            print("oops, you built the state")
            print(state)

def test_flips(result):

    sum = 0

    try:
        for i in range(100):
            sum += result[0][i]
    except IndexError:
        print("An error occurred. Did you run 100 trials?")
    else:
        if abs(sum - 50) < 10:
            print("Congratulations, that looks like a random coin flip. You got " + str(sum) + " tails and " + str(100 - sum) + " heads.")
        else:
            print("oops, those statistics don't look right... I could just be that you got a disproportionately high number of heads or tails though. Try a couple more times.")
