import time

def encriptarMensagem(mensagem):
    encriptado = []
    for letra in mensagem:  
        if letra.isalpha() and letra.isascii():  
            encriptado.append((ord(letra) - ord('A') + 1))
        elif letra.isspace():
            encriptado.append('/')
        

    time.sleep(1)

    print(*encriptado)
    if '/' in encriptado:
        print("OBS: o '/' significa que a mensagem contém um espaço\nO programa ignora acentuação e caracteres especiais")

if __name__ == "__main__":
    mensagem = input("Digite a mensagem a ser encriptada: ")
    encriptarMensagem(mensagem)
