from scipy import matrix, rand
from time import perf_counter
from random import randint
from matplotlib import pyplot as plt
import numpy as np
tiempo = [[],[],[],[],[],[],[],[],[],[]]#en cada lista(10) dentro de esta lista se agregan los tiempos en correr matrices de distintas dimensiones
nm = [2, 5, 10,12, 15, 20,30, 40, 45, 50, 55,60, 75, 100,125, 160, 200,250, 350, 500,
600, 800, 1000,2000, 5000, 10000]
 #dimension de matrices

for i in range(0,10):
    for N in nm:
        A = matrix(rand(N,N))


        t1 = perf_counter()
        C = np.linalg.inv(A)
        t2 = perf_counter()


        dt = t2 - t1
        tiempo[i].append(dt)
    print("ronda lista",i)
print(tiempo) #se imprime lista con todos los tiempos(10 veces con todas las matrices)
#grafica
plt.plot(nm,tiempo[0],nm,tiempo[1],nm,tiempo[2],nm,tiempo[3],nm,tiempo[4],nm,tiempo[5],nm,tiempo[6],nm,tiempo[7],nm,tiempo[8],nm,tiempo[9])
#etiqueta ejes
plt.xlabel("Dimension matriz N")
plt.ylabel("Tiempo transcurrido (s)")
#Titulo
plt.title("Rendimiento inv(A)")
#malla
plt.grid(True)
#mostrar grafico
plt.show()
