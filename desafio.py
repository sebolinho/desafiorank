import random
vitorias = 0
derrotas = 0
pontos = 0

def Regras():
    nome = validar_nome()
    print("Olá", nome)
    print("Esté é um jogo de Somas Matemáticas")
    regrasBasicas()
    avançadas = input("Deseja ver as regras avançadas? (s/n)")
    if avançadas == "s" or avançadas == "S" or avançadas == "sim" or avançadas == "Sim":
        regrasAvancadas()
        print("Vamos começar")
    else:
        print("Vamos começar")
    return nome

def dificuldade():
    while True:
        dificuldade = input("Escolha a dificuldade do jogo: \n1. Fácil\n2. Médio\n3. Difícil\n")
        if dificuldade == "1":
            return 1
        elif dificuldade == "2":
            return 5
        elif dificuldade == "3":
            return 10
        else:
            print("Digite uma opção válida.")

    




def regrasBasicas():
    print("=== Regras Básicas ===")
    print("1. Você terá que responder a soma de dois números.")
    print("2. Se você acertar, você ganha pontos.")
    print("3. Se você errar, você perde pontos.")
    print("4. Não existe empate.")
    print("=======================\n")
    

def regrasAvancadas():
    print("=== Regras Avançadas ===")
    print("1. Se você jogar mais de 10 partidas, você ganha um bônus de 1.3 pontos por vitória.")
    print("2. Se você jogar 5 partidas ou menos, você ganha um bônus de 2 pontos por vitória.")
    print("3. Se você jogar 3 partidas ou menos, você ganha um bônus de 3.3 pontos por vitória.")
    print("4. Se você acertar uma resposta, você ganha 5 pontos multiplicados pelo bônus de partidas.")
    print("5. Cada vitória aumenta seu bônus de pontos de acordo com o numero de vitórias.")
    print("6. ou seja se voce acerta 2 resposta seguidas voce ganha 10 pontos x o bonus de quantidade de partidas")
    print("7. Se você errar uma resposta, você perde 5 x numero de partidas jogadas pontos e todo bonus de partidas")
    print("7. Quanto mais acertos você tiver, mais pontos você acumula.")
    print("8. Não existe empate. Você acumula vitórias ou derrotas.")
    print("========================\n")

def validar_nome():
    while True:
        nome = input("Digite seu nome: ")
        if nome.isalpha():  # Verifica se o nome contém apenas letras
            return nome
        else:
            print("Digite um nome válido (apenas letras).")
        

def numeros():
    while True:
        numeroDePartiras = input("Digite Quantas partidas você deseja jogar: ")
        if numeroDePartiras.isdigit():
            return int(numeroDePartiras)
        else:
            print("Digite um número válido (apenas números).")


   

def perguntas(num1, num2, difi):
    
    if difi == 1:
        resposta = input(f"Quanto é {num1} + {num2}? ")
    elif difi == 5:
        resposta = input(f"Quanto é {num1} / {num2}? ")
    elif difi == 10:
        resposta = input(f"Quanto é {num1} * {num2}? ")
    return int(resposta)



def soma(num1, num2, dificuldade):
    if dificuldade == 1:
        return num1 + num2
    elif dificuldade == 5:
        return num1 / num2
    elif dificuldade == 10:
        return num1 * num2
    

def fimDeJogo(difi, name):
    global vitorias
    menssagem = f"O Matematico {name} tem de saldo de {vitorias} vitórias e esta no rank de {classes()} com {pontos} pontos na dificuldade {difi}"
    return menssagem

    

def classes():
    global pontos
    if pontos >= 50:
        return "Ouro"
    elif pontos >= 30:
        return "Prata"
    elif pontos >= 20:
        return "Bronze"
    elif pontos >= 10:
        return "Ferro"
    else:
        return "Sucata"
    

def geradorDeNumeros(difi):
    if difi == 1:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
    elif difi == 5:
        num1 = random.randint(10, 50)
        num2 = random.randint(10, 50)
    elif difi == 10:
        num1 = random.randint(50, 100)
        num2 = random.randint(50, 100)
    return num1, num2


def jogo(difi):
    global pontos
    global vitorias
    global derrotas
    numeroDePartiras = numeros()
    for i in range (numeroDePartiras):
            num1, num2 = geradorDeNumeros(difi)
            resposta = perguntas(num1, num2, difi)
            resultado = soma(num1, num2, difi)
            if resposta == resultado:
                print("Você acertou")
                vitorias += 1
                if numeroDePartiras >= 10:
                    multiplicador = 1.3333
                    print(f"Você ganhou ganha a multiplação de {multiplicador} pontos por estar jogando mais de 10 partidase {difi} de dificuldade")
                elif numeroDePartiras <= 5:
                    multiplicador = 2
                    print(f"Você ganhou ganha a multiplação de {multiplicador} pontos por estar jogando menos de 5 partidas e {difi} de dificuldade")
                elif numeroDePartiras <= 3:
                    multiplicador = 3.3333
                    print(f"Você ganhou ganha a multiplação de {multiplicador} pontos por estar jogando menos de 3 partidas e {difi} de dificuldade")    
                multi = vitorias * multiplicador
                print(f"Você ganhou {5}x{multi} Bonus de pontos")
                pontos += 5 * multi * difi
                print(f"Você tem {pontos} pontos")
            else:
                derrotas += 1
                pontos -= 5 * derrotas * difi
                print(f"Você errou perdeu 5 x o numero de derrotas {derrotas} x o nivel de dificuldade {difi} pontos")
                
                print(f"Você tem {pontos} pontos")




def main():
    
    difi = dificuldade()
    name = Regras()
    jogo(difi)
    if difi == 1:
        difi = "Fácil"
    elif difi == 5:
        difi = "Médio"
    elif difi == 10:
        difi = "Difícil"

    print(fimDeJogo(difi, name))

main()



   

    
