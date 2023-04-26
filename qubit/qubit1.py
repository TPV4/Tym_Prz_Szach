import numpy as np
import qiskit.quantum_info as q
import qiskit.visualization as qv

ket0 = np.array([1, 0])
ket1 = np.array([0, 1])

X = q.Operator([ [0,1],[1,0] ])
Y = q.Operator([ [0,-1.j],[1.j,0] ])
Z = q.Operator([ [1,0],[0,-1] ])
H = q.Operator([ [1/np.sqrt(2),1/np.sqrt(2)],[1/np.sqrt(2),-1/np.sqrt(2)] ])
S = q.Operator([ [1,0],[0,1.j] ])
T = q.Operator([ [1,0],[0,(1+1.j)/np.sqrt(2)] ])
TYMON=q.Operator([[np.sqrt(3)/3,np.sqrt(6)/3],[np.sqrt(6)/3,-np.sqrt(3)/3]])
operators=[X,Y,Z,H,S,T]

v=q.Statevector(ket1)
# for i in operators:
#     v=v.evolve(i)
v=v.evolve(TYMON)
# v=v.evolve(H)
# print(v.measure())
statistics = v.sample_counts(1000)
print(statistics)
