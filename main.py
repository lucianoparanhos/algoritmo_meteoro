# Luciano Paranhos (42324882)

import math
import os
from sys import platform

# variavel de controle para determinar o fim da execução
fim = False

# variável de controle para determinar quantas vezes cada opção foi selecionada
contar_opcao1 = 0
contar_opcao2 = 0
contar_opcao3 = 0
contar_opcao4 = 0

# variavel que armazena o comando usado para limpar a tela.
# considera linux ou macOS como sistema padrao. Somente se for windows
# o comando será trocado para cls
clear_cmd = "clear"
if platform == "win32":
    clear_cmd = "cls"

# variável que armazena as coordenadas X e Y da fazenda
fazenda_coordenada_x1 = 0
fazenda_coordenada_y1 = 0
fazenda_coordenada_x2 = 0
fazenda_coordenada_y2 = 0

# variável que armazena as coordenadas X e Y da sede
sede_coordenada_x1 = 0
sede_coordenada_y1 = 0
sede_coordenada_x2 = 0
sede_coordenada_y2 = 0

# variável que armazena as coordenadas X e Y da UPMCC
upmcc_coordenada_x = 0
upmcc_coordenada_y = 0

while not fim:
    os.system(clear_cmd)

    # apresentacao do Menu de opcoes
    print("-:: Sistema para Análise de Chuva de Meteoros ::-\n")

    print("1. Definir perímetro da propriedade e da edificação de interesse")
    print("2. Unificar sistemas de coordenadas de referência")
    print("3. Processar registros de chuva de meteoros")
    print("4. Apresentar estatísticas")
    print("5. Sair\n")

    # recebe a opcao que o usuário escolheu
    opcao = int(input("Escolha uma opção: "))

    # o programa verifica a opção escolhida
    if opcao == 1: # Definir perímetro da propriedade e da edificação de interesse
        os.system(clear_cmd)

        print("Informe as coordenadas da fazenda.")
        fazenda_coordenada_x1 = int(input("Primeira Coordenada X: "))
        fazenda_coordenada_y1 = int(input("Primeira Coordenada Y: "))
        fazenda_coordenada_x2 = int(input("Segunda Coordenada X: "))
        fazenda_coordenada_y2 = int(input("Segunda Coordenada Y: "))
        
        print("\nInforme a coordenada do prédio Sede.")
        sede_coordenada_x1 = int(input("Primeira Coordenada X: "))
        sede_coordenada_y1 = int(input("Primeira Coordenada Y: "))
        sede_coordenada_x2 = int(input("Segunda Coordenada X: "))
        sede_coordenada_y2 = int(input("Segunda Coordenada Y: "))

        os.system(clear_cmd)

        # Define o perímetro da fazenda
        if fazenda_coordenada_x1 <= fazenda_coordenada_x2:
            fazenda_min_x = fazenda_coordenada_x1
            fazenda_max_x = fazenda_coordenada_x2
        
        if fazenda_coordenada_x1 >= fazenda_coordenada_x2:
            fazenda_min_x = fazenda_coordenada_x2
            fazenda_max_x = fazenda_coordenada_x1
            
        if fazenda_coordenada_y1 <= fazenda_coordenada_y2:
            fazenda_min_y = fazenda_coordenada_y1
            fazenda_max_y = fazenda_coordenada_y2
        
        if fazenda_coordenada_y1 >= fazenda_coordenada_y2:
            fazenda_min_y = fazenda_coordenada_y2
            fazenda_max_y = fazenda_coordenada_y1

        # Define o perímetro da sede
        if sede_coordenada_x1 <= sede_coordenada_x2:
            sede_min_x = sede_coordenada_x1
            sede_max_x = sede_coordenada_x2

        if sede_coordenada_x1 >= sede_coordenada_x2:
            sede_min_x = sede_coordenada_x2
            sede_max_x = sede_coordenada_x1

        if sede_coordenada_y1 <= sede_coordenada_y2:
            sede_min_y = sede_coordenada_y1
            sede_max_y = sede_coordenada_y2

        if sede_coordenada_y1 >= sede_coordenada_y2:
            sede_min_y = sede_coordenada_y2
            sede_max_y = sede_coordenada_y1

        print("As Informações coletadas foram:\n")
        print("Fazenda")
        print(f" Canto superior. esquerdo: ({fazenda_min_x},{fazenda_max_y}), direito: ({fazenda_max_x},{fazenda_max_y})")
        print(f" Canto inferior. esquerdo: ({fazenda_min_x},{fazenda_min_y}), direito: ({fazenda_max_x},{fazenda_min_y})")

        print("\nSede")
        print(f" Canto superior. esquerdo: ({sede_min_x},{sede_max_y}), direito: ({sede_max_x},{sede_max_y})")
        print(f" Canto inferior. esquerdo: ({sede_min_x},{sede_min_y}), direito: ({sede_max_x},{sede_min_y})")

        input("\nAperte <Enter> para continuar")
        contar_opcao1 = contar_opcao1 + 1

    elif opcao == 2: # Unificar sistemas de coordenadas de referência
        os.system(clear_cmd)

        if fazenda_coordenada_x1 == 0 and fazenda_coordenada_y1 == 0:
            print("Impossível processar qualquer registro de queda no momento: localização da propriedade ainda não informada")
            input("Aperte <Enter> para continuar")
            continue
        
        print("Informe a localização da UPMCC. Será usado como referência do registro de meteoros")
        upmcc_coordenada_x = int(input("Digite a coordenada X da UPMCC: "))
        upmcc_coordenada_y = int(input("Digite a coordenada Y da UPMCC: "))

        print("As coordenadas polares serão convertidas em cartesianas.")
        print(f"Coordenadas ({upmcc_coordenada_x},{upmcc_coordenada_y}) definidas como ponto de origem.")

        input("\nAperte <Enter> para continuar")
        contar_opcao2 = contar_opcao2 + 1

    elif opcao == 3: # Processar registros de chuva de meteoros
        os.system(clear_cmd)

        if fazenda_coordenada_x1 == 0 and fazenda_coordenada_y1 == 0:
            print("Impossível processar qualquer registro de queda no momento: localização da propriedade ainda não informada")
            input("Aperte <Enter> para continuar")
            continue

        if upmcc_coordenada_x == 0 and upmcc_coordenada_y == 0:
            print("Impossível processar qualquer registro de queda no momento: localização da UPMCC ainda não informada")
            input("Aperte <Enter> para continuar")
            continue

        contar_opcao3 = contar_opcao3 + 1

    elif opcao == 4: # Apresentar estatísticas
        os.system(clear_cmd)

        if fazenda_coordenada_x1 == 0 and fazenda_coordenada_y1 == 0:
            print("Impossível processar qualquer registro de queda no momento: localização da propriedade ainda não informada")
            input("Aperte <Enter> para continuar")
            continue

        contar_opcao4 = contar_opcao4 + 1

    elif opcao == 5: # Sair
        fim = True
        
    else: # Qualquer número diferente dos números usados no menu
        os.system(clear_cmd)

        print("Opção inválida")
        input("Aperte <Enter> para continuar")

# O usuário escolheu a opção 5 e o programa foi finalizado
print("\nFim do programa")
print(f"Você selecionou a (Opcao 1): {contar_opcao1} vezes")
print(f"Você selecionou a (Opcao 2): {contar_opcao2} vezes")
print(f"Você selecionou a (Opcao 3): {contar_opcao3} vezes")
print(f"Você selecionou a (Opcao 4): {contar_opcao4} vezes")
