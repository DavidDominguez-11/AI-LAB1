import numpy as np

y_real = np.array([100, 150, 200, 250, 300])
y_pred = np.array([110, 140, 210, 240, 500])

def rmse(real, pred): #sqrt( (1/n) * sum( (yi - y')^2 ) )
    n = len(real)
    mse = np.sum((pred - real)**2) / n
    rmse = np.sqrt(mse)
    return rmse

def mae(real, pred): #(1/n) * sum( |yi - y'| )
    n = len(real)
    mae = np.sum(np.abs(pred - real)) / n
    return mae

rmse_resultado = rmse(y_real, y_pred)
mae_resultado = mae(y_real, y_pred)

print(f"RMSE calulado: {rmse_resultado:.2f}")
print(f"MAE calulado: {mae_resultado:.2f}")

# Explicación final
print("\nComparacion")
print(f"La metrica que penalizo mas el error es el RMSE ({rmse_resultado:.2f}) en comparacion con el MAE ({mae_resultado:.2f}).")
print("Esto sucede porque el RMSE eleva las diferencias al cuadrado antes de promediarlas, lo que castiga mucho mas severamente las desviaciones grandes o valores atipicos.")
print("\nPara las dosis medicas, esto es muy importante porque un error demasiado grande en una dosis puede ser fatal. Preferimos una metrica como RMSE que nos alerte fuertemente sobre estos errores.")