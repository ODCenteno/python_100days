
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def welcome():
    print(f'{logo}')
    print(f'\n\n{"*" * 100}\n\n')

def cipher():
    cifrando = True
    while cifrando:
        tarea = input("Escribe 'encode' para encriptar, excribe 'decode' para desencriptar: ").lower().strip()
        try:
            saltos = int(input(f'Escribe el numero de saltos para la criptografía: '))
            saltos = saltos % 26
        except ValueError:
            print("\n\nXX - Intenta de nuevo con un número - XX\n\n")
            cipher()
        texto_crudo = input(f'Escribe el texto a encriptar: ').lower()

        if tarea == 'decode':
            saltos *= -1
        texto_final = ''
        for letra in texto_crudo:
            if letra not in alphabet:
                texto_final += letra
                continue
            indice = alphabet.index(letra)
            texto_final += (alphabet[indice + saltos])
        print(f'\n\nEl texto {tarea} es: {texto_final}\n\n')

        resp = input(f'¿Quieres seguir cifrando/descifrando texto? (si / no): ')
        if resp == 'no':
            cifrando = False

if __name__ == '__main__':
    welcome()
    cipher()