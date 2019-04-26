from pyquil import Program
from pyquil.api import get_qc
from pyquil.gates import H, MEASURE

"""
Implement a Hadamard gate on qubits [0, 1] of 
3q-qvm and measure ONLY these two qubits 100 times
"""
qvm_name = '3q-qvm'
as_qvm_value = True
num_shots = 100

def measurement_1(qvm_name, as_qvm_value, num_shots):
    """
        Args: 
            qvm_name [type:str]
            Name of the device on which to run the Program

            as_qvm_value [type : bool]
            True if device is a QVM, otherwise false

            num_shots [type : int]
            Number of shots to repeat measurement for

        Output:
            results [type : np.ndarray]
            Numpy array of measurement outcomes for all shots
    """
    qc = get_qc(qvm_name, as_qvm=as_qvm_value)
    circuit = Program()
    creg = circuit.declare("ro", "BIT", 2)
    circuit += H(0)
    circuit += H(1)
    circuit += MEASURE(0, creg[0])
    circuit += MEASURE(1, creg[1])

    circuit.wrap_in_numshots_loop(1000)
    executable = qc.compile(circuit)
    result = qc.run(executable)

    return result

results_1 = measurement_1(qvm_name, as_qvm_value, num_shots)
print(results_1)

"""
Implement a Hadamard gates on the first two available 
qubits [7, 0] of the Aspen-4-4Q-A and measure ALL qubits 
(use run_and_measure)
"""

qpu_name = 'Aspen-4-4Q-A'
as_qvm = True
num_shots = 100

def measurement_2(qpu_name, as_qvm_value, num_shots):
    """
        Args: 
            qpu_name [type : str]
            Name of the device on which to run the Program.

            as_qvm_value [type : bool]
            True if device is a QVM, otherwise false.

            num_shots [type : int]
            Number of shots to repeat measurement for.

        Output:
            results [type : dict]
            Dictionary, keys correspond to qubits, values are numpy arrays
            with measurement results. 
    """
    qc = get_qc(qpu_name, as_qvm=as_qvm_value)
    qubits = qc.qubits()
    circuit = Program()
    
    circuit += H(qubits[0])
    circuit += H(qubits[3])
    
    results = qc.run_and_measure(circuit, num_shots)
    
    return results

results_2 = measurement_2(qpu_name, as_qvm_value, num_shots)
print(results_2)