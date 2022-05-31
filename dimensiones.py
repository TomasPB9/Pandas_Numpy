#crea array de 5 dimensiones
array_challenge = np.array([1,2,3,4,5], ndmin = 5)
print(array_challenge, array_challenge.ndim)

#Sumar 1 dimension en algun eje
array_increased = np.expand_dims(np.array(array_challenge), axis = 0)
print(array_increased, array_increased.ndim)

#borrar dimensiones que no se usan
exact_array = np.squeeze(array_challenge)
print(exact_array, exact_array.ndim)