import pandas as pd
import random
import numpy as np

ruta_data = "data.csv"

def guardar_a_csv(edad, salario, compro_producto):
    data = pd.DataFrame([{'edad': edad, 'salario': salario, 'compro_producto': compro_producto}])
    data.to_csv(ruta_data, mode='a', index=False, header=False, lineterminator='\n')

def llenar_data(n):
    print(f"Generando {n} filas de datos")
    
    # crear lista de clases desbalanceadas 90 0 y 10 1
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
    
    data = pd.read_csv(ruta_data)
    data.info()
    
    print(f"Datos generados: {n} filas")

def imputar_edad_con_promedio():
    print("\nImputando valores NaN")
    
    data = pd.read_csv(ruta_data)
    promedio_edad = round(data['edad'].mean())
    nans_encontrados = data['edad'].isna().sum()
    
    for i in range(len(data)):
        if pd.isna(data.loc[i, 'edad']):
            data.loc[i, 'edad'] = promedio_edad
    
    # dataset actualizado
    data.to_csv(ruta_data, index=False)

    print(f"NaN imputados: {nans_encontrados}")
    print(f"Promedio usado: {promedio_edad}")

"""
El promedio es una mala idea cuando tienes valores extremos o atípicos en tus datos. 
Por ejemplo, si hay edades de 25, 28, 30, 27 y 95, el promedio te es 41 años, 
pero eso no representa bien a la mayoría de personas que están cerca de los 27 años. 
La persona de 95 años distorsiona el resultado. 
En estos casos es mejor usar la mediana porque no se ve afectada por valores extremos 
y te da una mejor idea del valor "típico" o central de tus datos.
"""

def undersampling_manual():
    print("\nAplicando undersampling")
    
    data = pd.read_csv(ruta_data)
    
    # mantener todas las filas de la clase minoritaria 1
    clase_minoritaria = data[data['compro_producto'] == 1]
    
    # obtener todas las filas de la clase mayoritaria 0
    clase_mayoritaria = data[data['compro_producto'] == 0]
    
    # seleccionar aleatoriamente el mismo numero de filas de la clase mayoritaria
    num_minoritaria = len(clase_minoritaria)
    clase_mayoritaria_sample = clase_mayoritaria.sample(n=num_minoritaria, random_state=42)
    
    # crear el DataFrame balanceado
    data_balanceado = pd.concat([clase_minoritaria, clase_mayoritaria_sample], ignore_index=True)
    
    # mezclar las filas
    data_balanceado = data_balanceado.sample(frac=1, random_state=42).reset_index(drop=True)
    
    # guardar el dataset balanceado
    data_balanceado.to_csv('data_balanceado.csv', index=False)
    
    print(f"Total de filas balanceadas: {len(data_balanceado)}")
    print(f"Distribucion:\n{data_balanceado['compro_producto'].value_counts()}")

def ver_data(ruta):
    data = pd.read_csv(ruta)
    print(data)

if __name__ == "__main__":


    llenar_data(100)
    data = pd.read_csv("data.csv")
    print(f"NaN en edad: {data['edad'].isna().sum()}")
    print(data['compro_producto'].value_counts())

    imputar_edad_con_promedio()

    undersampling_manual()
    
    ver_data(ruta_data)
    ver_data("data_balanceado.csv")

    

    