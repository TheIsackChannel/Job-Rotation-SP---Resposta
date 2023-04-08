# Resolução 2 - Sequência de Fibonacci
def verificar_fibonacci(numero):
    a, b = 0, 1
    while a <= numero:
        if a == numero:
            return True
        a, b = b, a + b
    return False

# Resolução 3 - Valor de Faturamento Mensal
import json

# Exemplo de dados em formato JSON
dados_faturamento = '''
{
    "faturamento_diario": [25000, 35000, 18000, 42000, 30000, 26000, 28000, 31000],
    "dias_no_mes": 30
}
'''

dados_faturamento = json.loads(dados_faturamento)
faturamento_diario = dados_faturamento["faturamento_diario"]
dias_no_mes = dados_faturamento["dias_no_mes"]

menor_valor = min(faturamento_diario)
maior_valor = max(faturamento_diario)
media_mensal = sum(faturamento_diario) / dias_no_mes

dias_acima_da_media = sum(1 for valor in faturamento_diario if valor > media_mensal)

# Resolução 4 - Percentual de Representação por Estado
faturamento_por_estado = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

total_mensal = sum(faturamento_por_estado.values())

percentual_por_estado = {estado: (faturamento / total_mensal) * 100 for estado, faturamento in faturamento_por_estado.items()}

# Resolução 5 - Inversão de Caracteres em uma String
def inverter_string(string):
    lista_caracteres = list(string)
    tamanho = len(lista_caracteres)
    for i in range(tamanho // 2):
        lista_caracteres[i], lista_caracteres[tamanho - 1 - i] = lista_caracteres[tamanho - 1 - i], lista_caracteres[i]
    return "".join(lista_caracteres)

# Exemplo de uso
numero = 34
print(f"O número {numero} {'pertence' if verificar_fibonacci(numero) else 'não pertence'} à sequência de Fibonacci.")
print(f"O menor valor de faturamento ocorrido em um dia do mês foi: R${menor_valor:.2f}")
print(f"O maior valor de faturamento ocorrido em um dia do mês foi: R${maior_valor:.2f}")
print(f"Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: {dias_acima_da_media}")
print("Percentual de representação por estado:")
for estado, percentual in percentual_por_estado.items():
    print(f"{estado}: {percentual:.2f}%")
print(f"A string original: 'Hello, world!'")
print(f"A string invertida: '{inverter_string('Hello, world!')}'")