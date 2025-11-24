import numpy as np


### creazione array e print del tipo con dtype
arr = np.arange(10, 49 + 1)
print("array con int fra 10 e 49: ", arr)
print("tipo: ", arr.dtype)

### Cambio del tipo con astype e print del tipo con dtype
arr_float = arr.astype(float)
print("array con decimali fra 10 e 49: ", arr_float)
print("tipo: ", arr_float.dtype)

##
print("shape: ", arr.shape)
arr_reshaped = arr.reshape((10,4))
print("shape: ", arr_reshaped.shape)
print("array con forma (10,4), 10 righe x 4 colonne: ", arr_reshaped)


arr = np.arange(10, 49 + 1, dtype = "float") #   specificare il tipo in fase di definizione