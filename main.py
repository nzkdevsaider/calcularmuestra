# Programa para calcular la muestra necesaria para un estudio
# Autor: Sebastián Morales
# Universidad Tecnologica de Panamá
# Facultad de Ingeniería en Sistemas Computacionales
# Curso: Probabilidad y Estadística
# Profesora: Edna Bouche
# Grupo: 2IF121

def muestra(N, Z, e, p, q):
    muestra = ((Z**2)*p*q*N) / (N*(e**2) + (Z**2)*p*q)
    muestra = round(muestra)
    print("La muestra necesaria es de: ", muestra)
    return muestra

N = float(input("Introduce la cantidad universal: "))
Z = float(input("Introduce el nivel de confianza: "))
e = float(input("Introduce el grado de error: "))
p = float(input("Introduce la probabilidad de ocurrencia: "))
q = float(input("Introduce la probabilidad de no ocurrencia: "))
muestra(N, Z, e, p, q)