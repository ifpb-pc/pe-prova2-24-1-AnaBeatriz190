from collections import Counter
from typing import List
def q1a(nums):

    '''Dado um array inteiro nums, retorne verdadeiro se algum valor aparecer pelo menos 
    duas vezes no array e retorne falso se cada elemento for distinto. Crie duas funções 
    (q1a e q1b) que resolvam este problemas utilizando apenas as listas e outra que utilize 
    dicionários.'''
    duas_vezes = []
    for num in nums:
        if num in duas_vezes:
            return True
        duas_vezes.append(num)
    return False

def q1b(nums):
    seen = {}
    for num in nums:
        if num in seen:
            return True
        seen[num] = True
    return False



def q2(s: str, t: str) -> bool:
    '''Dadas duas strings s e t, 
    retorne verdadeiro se t for um anagrama de s, 
    e falso caso contrário.'''
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)
    s = ""
    t = ""
    print(s, t)


def q3() -> int:
    '''Leia um arquivo CSV chamado estoque.csv, contendo informações 
    de produtos em estoque (Nome, Quantidade, Preço). Atualize o arquivo 
    CSV, multiplicando o preço de todos os produtos por 1.1 
    (aumento de 10%). Além de atualizar o arquivo, sua função 
    deve retornar o valor total em estoque (soma da quantidade de cada produto x preço).'''

    import pandas as pd

    df = pd.read_csv(arquivo)
    df['Preço'] = df['Preço'] * 1.1
    df['Valor Total'] = df['Quantidade'] * df['Preço']
    return total_estoque
    

def q4():
    '''Você deverá ler valores numéricos até o usuário digitar 0. 
    Use uma função ler_valores() para retornar os valores deverão ser 
    passados para uma função processa_lista(lista) que irá retornar 2 
    listas, uma lista para valores pares e uma lista para ímpares. 
    O tamanho máximo de cada uma das listas é de 5. Logo, cada vez que 
    uma das listas ficar cheia você deve substituir os valores mais 
    antigos pelos valores novos. Após executar a função, você deve 
    imprimir o conteúdo em cada uma das listas.'''

    


if __name__=="__main__":
    # teste sua questão manualmente aqui
    pass