# -*- coding: utf-8 -*-

from data_etu import * 
from pandas import * 
from numpy import * 
from matplotlib.pyplot import * 



# Generation de données vaec la fonction generate_data du fichier data_etu
dt = generate_data(11817049)
# print(dt )

# Transformation de dt  en dataframe

dt = DataFrame(dt)
# print(dt)
X = dt.pop('X')
print("X = ",X)
print("dt = ",dt)

moy_Y = mean_calcul(dt) # Calcul des moyennes des Y_i
print("moyenne des Y_i:",moy_Y)


# Travaille sur la colonne de plus grande moyenne

position, Y_k, mean_k, sd_k = description_Yk(dt)
print("Position :",position)
print( "Y_k:",Y_k)
print("la moyenne : ", mean_k, "L'ecart-type : ",sd_k)

# Calcul de l'integrale par la methonde de Monte Carlo

integrale = Monte_Carlo_integrate_Yk(dt, Y_k, -1, 1)
print("Intégrale = ",integrale)


print(dt[Y_k])



# Normalisation de Y_k
Z = normalisation_Yk( dt, Y_k)
print("Z = ", Z)



dt_new_column = DataFrame(Z, columns=['Z'])
print(dt_new_column)

