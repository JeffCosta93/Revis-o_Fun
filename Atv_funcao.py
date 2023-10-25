def calcular_media(lista_numeros):
    if not lista_numeros:
        return None
    soma = sum(lista_numeros)
    media = soma / len(lista_numeros)
    return media

numeros = [10, 20, 30, 40, 50]
media_resultante = calcular_media(numeros)

print(f'A média dos números é: {media_resultante:.2f}')
