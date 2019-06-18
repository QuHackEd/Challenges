from pyquil.api import WavefunctionSimulator, local_qvm
import math
import numpy as np

def test_measurement_run_results(results, num_shots):
    
    if not isinstance(results, np.ndarray):
        print('It doesn\'t look like the results are in the correct format.. did you use run?')
        
    else:
        results_shape = results.shape
        if not results_shape[1] == 2:
            print('It looks like the results array is the wrong size.')
            print('Did you measure more than two qubits??')
        else:
            try:
                   summed_results = np.sum(results, 0)
            except:
                  print('Something went wrong')
            if abs(summed_results[0] - num_shots/2) < 0.1*num_shots:
                print("Those statistics for the 3rd qubit look right, well done!")

                if abs(summed_results[1] - num_shots/2) < 0.1*num_shots:
                    print("The statistics for the 4th qubit look good as well, awesome!")
                else:
                    print("oops, those statistics don't look right... It could just be that you got a disproportionately high number of one outcome or another though. Try a couple more times.")

                    if num_shots < 50:
                        print('Maybe try a bigger number of  measurement shots..')

            else:
                print("oops, those statistics don't look right... It could just be that you got a disproportionately high number of one outcome or another though. Try a couple more times.")

                if num_shots < 50:
                     print('Maybe try a bigger number of  measurement shots..')
                 