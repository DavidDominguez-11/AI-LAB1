import pandas as pd
import random
import numpy as np

data = pd.read_csv("data.csv")

def guardar_a_csv(edad, salario, compro_producto):
    data = pd.DataFrame([{'edad': edad, 'salario': salario, 'compro_producto': compro_producto}])
    data.to_csv('data.csv', mode='a', index=False, header=False, lineterminator='\n')

def llenar_data(n):
    # rear lista de clases desbalanceadas 90 0 y 10 1
    clases = [0] * 90 + [1] * 10
    random.shuffle(clases)
    
    for i in range(n):
        edad = random.randint(18, 88)
        salario = random.randint(1000, 10000)
        compro_producto = clases[i]  # usar la lista desbalanceada
        
        # prob de poner NaN en edad
        if random.random() < 0.10:
            edad = np.nan
        
        guardar_a_csv(edad, salario, compro_producto)


# llenar_data(100)

print(f"NaN en edad: {data['edad'].isna().sum()}")
print(data['compro_producto'].value_counts())