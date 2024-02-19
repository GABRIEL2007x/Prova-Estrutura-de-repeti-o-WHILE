def main():
    numeros = []
    while True:
        try:
            numero = int(input("Digite um número inteiro (0 para parar): "))
            if numero == 0:
                break
            numeros.append(numero)
        except ValueError:
            print("Por favor, digite apenas números inteiros.")

    quantidade_numeros = len(numeros)
    if quantidade_numeros > 0:
        soma = sum(numeros)
        media = soma / quantidade_numeros
        print(f"\nQuantidade de números digitados: {quantidade_numeros}")
        print(f"Soma dos números: {soma}")
        print(f"Média dos números: {media}")
    else:
        print("Nenhum número foi digitado.")


if __name__ == "__main__":
    main()
