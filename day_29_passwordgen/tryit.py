import json

def aplicar_operaciones(num):
    operaciones = [abs, float]

    resultado = []
    for operacion in operaciones:
        resultado.append(operacion(num))
    print(resultado)
    datos = {
        'camaleon': {
            'lunes': 'puerco',
            'martes': 'tambien',
        }
    }
    with open('try.json', "w") as try_file:
        json.dump(datos, try_file)
    return resultado

aplicar_operaciones(-2)

# [2, -2.0]