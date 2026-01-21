import pandas as pd
import random

data = pd.read_csv("data.csv")

def guardar_a_csv(edad, salario, compro_producto):
    data = pd.DataFrame([{'edad': edad, 'salario': salario, 'compro_producto': compro_producto}])
    data.to_csv('data.csv', mode='a', index=False, header=False, lineterminator='\n')

def llenar_data(n):

    for i in range(n):
        edad = random.randint(18, 88)
        salario = random.randint(1000, 10000)
        compro_producto = random.randint(0,1)

        guardar_a_csv(edad, salario, compro_producto)
    
llenar_data(10)


