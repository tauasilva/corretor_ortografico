import nltk
import argparse
import logging
import sys

nltk.download('punkt')

def separa_palavras(lista_tokens):
    lista_palavras = []
    for token in lista_tokens:
        if token.isalpha():
            lista_palavras.append(token)
    return lista_palavras

def normalizacao(lista_de_palavras):
    lista_normalizada = []
    for palavra in lista_de_palavras:
        lista_normalizada.append(palavra.lower())
    
    return lista_normalizada

def insere_caracter(fatias):
    novas_palavras = []
    letras = 'abcdefghijklmnopqrstuvwxyzàáâãèéêìíîòóôõùúûç'

    for E,D in fatias:
        for letra in letras:
            novas_palavras.append(E + letra + D)

    return novas_palavras

def deletando_caracter(fatias):
    
    novas_palavras = []

    for E,D in fatias:
        novas_palavras.append(E + D[1:])

    return novas_palavras

def troca_caracter(fatias):
    novas_palavras = []
    letras = 'abcdefghijklmnopqrstuvwxyzàáâãèéêìíîòóôõùúûç'

    for E,D in fatias:
        for letra in letras:
            novas_palavras.append(E + letra + D[1:])

    return novas_palavras    


def inverte_caracter(fatias):
    novas_palavras = []

    for E,D in fatias:
        if(len(D) > 1):
            novas_palavras.append(E + D[1] + D[0] +  D[2:])

    return novas_palavras

def gerador_palavras(palavra):

    fatias = []


    for i in range(len(palavra)+1):
        fatias.append((palavra[:i],palavra[i:]))

    palavras_geradas = insere_caracter(fatias)
    palavras_geradas += deletando_caracter(fatias)
    palavras_geradas += troca_caracter(fatias)
    palavras_geradas += inverte_caracter(fatias)
    
    return palavras_geradas







    

def corretor(palavra: str,lista_normalizada : list):
    '''
        function Corretor ortográfico

        palavra : palavra que vamos verificar 
    '''

    def probabilidade(palavra_gerada):
        total_de_palavras = len(lista_normalizada)
        frequencia = nltk.FreqDist(lista_normalizada)
        return frequencia[palavra_gerada]/total_de_palavras

    palavras_geradas = gerador_palavras(palavra)

    palavra_correta = max(palavras_geradas,key =probabilidade)

    return palavra_correta



def main():
    
    parser = argparse.ArgumentParser(description='Corretor Ortografico')
    
    parser.add_argument('--palavra', dest='palavra', type=str, help='Palavra')
    parser.add_argument('--base', dest='base', type=str, help='Base')
    
    args = parser.parse_args()

    logging.info(f'Args: {args}')
    print(args)

    with open(args.base, encoding="utf8") as f:
        artigos = f.read()

    lista_tokens = nltk.tokenize.word_tokenize(artigos)
    palavras_separadas = separa_palavras(lista_tokens)
    lista_normalizada = normalizacao(palavras_separadas)    

    return corretor(args.palavra,lista_normalizada)
    

if __name__ == "__main__":
    main()
