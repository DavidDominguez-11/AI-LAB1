# Laboratorio 1 - Inteligencia Artificial

Este repositorio contiene los task 2 y 3 del primer laboratorio de Inteligencia Artificial.

### Task 2: Manejo de Datos (task2.py)

Esta tarea se enfoca en el preprocesamiento de datos, incluyendo:
- Generación de datos sintéticos con desbalance de clases
- Manejo de valores faltantes (NaN)
- Técnicas de balanceo de datos (undersampling)
- Análisis de distribuciones de datos

#### Características implementadas:
- Generación de dataset con variables categóricas y numéricas
- Implementación de imputación de valores faltantes usando el promedio
- Técnica de undersampling para balancear clases desbalanceadas
- Visualización de distribuciones antes y después del procesamiento

### Task 3: Métricas de Evaluación (task3.py)

Implementación y comparación de métricas de evaluación para modelos de regresión:
- Error Cuadrático Medio (RMSE)
- Error Absoluto Medio (MAE)

#### Análisis:
- Comparación del comportamiento de RMSE vs MAE
- Impacto de valores atípicos en las métricas
- Aplicación práctica en contexto médico

## Estructura del Proyecto

```
AI-LAB1/
├── README.md               # Este archivo
├── task2.py               # Implementación de manejo de datos
├── task3.py               # Implementación de métricas de evaluación
├── data.csv               # Dataset generado
└── data_balanceado.csv    # Dataset después de aplicar balanceo
```

## Requisitos

- Python 3.6+
- pandas
- numpy

## Uso

1. Para ejecutar la tarea de manejo de datos:
   ```bash
   python task2.py
   ```

2. Para ejecutar la tarea de métricas de evaluación:
   ```bash
   python task3.py
   ```