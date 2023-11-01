import numpy as np

# Ejercicio 2
ogros_path = 'ogros.txt'
elfos_path = 'elfos.txt'

data_ogros = np.loadtxt(ogros_path, dtype=float)
data_elfos = np.loadtxt(elfos_path, dtype=float)

print(data_elfos)