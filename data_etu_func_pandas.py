# -*- conding: utf-8 -*-
import numpy as np
import pandas as pd

def generate_data(num_etu):
    """
    Permet la creation des données à partir d'un numéro d'etudiant

    """

    np.random.seed(num_etu);
    col = ['X'];
    for i in range(10):
        col.append('Y_'+str(i));
    data = pd.DataFrame(np.column_stack([np.linspace(-1,1,num_etu),-1+2*np.random.random([num_etu,10])]),columns=col);
    data['Y_'+str(int((num_etu%10+num_etu%100/10)%10))] += np.exp(-(data['X']-0.0001*(num_etu%10000))**2/(0.01*(num_etu%100))**2);
    return data



# Fonction calculant la moyenne sur un dataframe
def mean_calcul(X):
    return X.mean()

def description_Yk(X):
    """
    Cette fonction prend en entrée une pandas colonne est fait sa description
    """
    for ind, column in enumerate(X.columns):
        # print(ind, column)
        if( X[column].mean() > 0.05 ):
            position = ind
            X_k = column
    mean_k = X[X_k].mean()
    sd_k = X[X_k].std()
    return ([position, X_k, mean_k, sd_k])

def Monte_Carlo_integrate_Yk(X,colonne,a,b):
    """
    La methode  de monte carlo permet de calculer une integrale en utilation la moyenne 
    sur ensemble discret obtenu par le calcul de la fonction sur un interval discret.
    ici les extermites sont a et b

    """

    k_mean = X[colonne].mean()
    result = (b-a)*k_mean
    return result

# Fonction de normalisation

def normalisation_Yk(X,colon):
    Z_k = ( X[colon] - X[colon].mean()  )/( X[colon].std() )
    return Z_k


