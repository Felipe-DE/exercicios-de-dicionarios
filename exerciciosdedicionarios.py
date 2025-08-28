# 1. Criando um dicionário simples
aluno = {"nome": "Gabriel", "idade": 20, "nota": 9.5}
print("1) Dicionário aluno:", aluno)


# 2. Acessando valores
produto = {"nome": "Caneta", "preço": 2.5, "estoque": 100}
print("\n2) Produto:", produto["nome"])
print("   Estoque:", produto["estoque"])


# 3. Adicionando novos pares chave-valor
pessoa = {"nome": "Carlos", "idade": 30}
pessoa["cidade"] = "São Paulo"
print("\n3) Pessoa com cidade:", pessoa)


# 4. Removendo elementos
carro = {"marca": "Ford", "modelo": "Fiesta", "ano": 2010}
del carro["ano"]
print("\n4) Carro sem ano:", carro)


# 5. Verificando existência de uma chave
contato = {"nome": "Ana", "email": "ana@email.com"}
print("\n5) 'telefone' existe em contato?", "telefone" in contato)


# 6. Contando frequência de palavras
def contar_palavras(lista):
    frequencia = {}
    for palavra in lista:
        frequencia[palavra] = frequencia.get(palavra, 0) + 1
    return frequencia

palavras = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]
print("\n6) Frequência de palavras:", contar_palavras(palavras))


# 7. Invertendo um dicionário
d = {"a": 1, "b": 2, "c": 3}
invertido = {valor: chave for chave, valor in d.items()}
print("\n7) Dicionário invertido:", invertido)


# 8. Dicionário com listas
notas_alunos = {
    "Ana": [7, 8, 9],
    "Pedro": [6, 5, 7],
    "Maria": [10, 9, 8]
}
print("\n8) Médias dos alunos:")
for aluno, notas in notas_alunos.items():
    media = sum(notas) / len(notas)
    print(f"   {aluno} - Média: {media:.2f}")


# 9. Mesclando dois dicionários
def mesclar_dicts(d1, d2):
    resultado = d1.copy()
    resultado.update(d2)
    return resultado

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
print("\n9) Mescla de dicionários:", mesclar_dicts(d1, d2))


# 10. Ordenando dicionário por valor
pontuacoes = {"João": 50, "Maria": 80, "Pedro": 70}
ordenado = dict(sorted(pontuacoes.items(), key=lambda item: item[1], reverse=True))
print("\n10) Pontuações ordenadas:", ordenado)
