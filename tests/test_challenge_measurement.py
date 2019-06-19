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

    return
                
def test_measurement_runandmeasure_results(results, num_shots):
    
    if not isinstance(results, dict):
        print('It doesn\'t look like the results are in the correct format.. did you use run_and_measure?')
        
    else:
        if not list(results.keys()) == [0, 1, 2, 7]:
            print('It doesn\'t seem like the right qubits have been measured? Did you use the correct chip?')
        else:
            if not results[0].all() == 1:
                print('Hmm, it doesn\'t look like the outcome from qubit 0 was always 1. Maybe try adding some gates?')
            else:
                     
                if not results[7].all() == 1:
                    print('Hmm, it doesn\'t look like the outcome from qubit 7 was always 1. Maybe try adding some gates?')  
                else: 
                    print('Good job!')
           
    return 
                      
                      
                      
                      
def test_measurement_challenge(results_list, num_shots):
    
    if not isinstance(results_list, list):
        print('*results_list* is not in a list format.')
    else:
        try:
            summed_results = sum(results_list)
        except:
            print('Something went wrong')
        if abs(summed_results - 3*num_shots/4) < 0.1*num_shots:
                print("Those statistics for look right, well done!")

        else:
            print("oops, those statistics don't look right... It could just be that you got a disproportionately high number of one outcome or another though. Try a couple more times.")

            if num_shots < 50:
                print('Maybe try a bigger number of measurement shots..') 
    return
                      
                      
                      
                      
                      
                      
                      
                      
            
                 