# CNOT

from qiskit.quantum_info import Statevector, Operator
from numpy import sqrt
from qiskit import QuantumCircuit

H = Operator([[1,1],[1,-1]]/sqrt(2))
I = Operator([[1,0],[0,1]])
IH = I.tensor(H)
fi = Statevector([1,-1,1.j,-1.j])
CZ = ([[1,0,0,0],
       [0,1,0,0],
       [0,0,1,0],
       [0,0,0,-1]
      ])

fi2 = fi.evolve(IH)
print(fi2)
fi3 = fi2.evolve(CZ)
print(fi3)
fi3.evolve(IH)
print(fi3)

# --------------------------------------------------------------
# CNOT

# from qiskit.quantum_info import Statevector, Operator
# from numpy import sqrt
# from qiskit import QuantumCircuit

# fi = Statevector([1,-1,1.j,-1.j])

# circuit = QuantumCircuit(2)
# circuit.h(0)
# circuit.cz(1,0)
# circuit.h(0)
# #circuit.draw()

# fi.evolve(circuit)