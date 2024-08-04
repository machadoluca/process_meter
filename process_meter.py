from src.process_exec import process_exec
from src.time_reducer import time_reducer


# laço principal
def main() -> None:
    print("Bem vindo ao medidor de tempo de execução!\n")

    # cria as váriaveis de controle para o usuário inserir
    try:
        aliquot = float(input("Insira a aliquota de tempo de programa: "))
        process_timeout = float(input("Insira o timeout de execução do binário: "))
    except ValueError:
        print("Insira valores válidos")
        exit()

    # enquanto a aliquota for maior que 0
    while aliquot > 0:
        try:
            # insere o comando
            command = str(input("\nDigite o nome do binário ou aperte Q para sair: "))
            #condição para sair do programa
            if command == "q" or command == "Q":
                break
            
            # chama a função de executar o processo a partir do commando
            cpu_time = process_exec(command, process_timeout)
            # retorna o cálculo da aliquota 
            aliquot = time_reducer(aliquot, cpu_time)
        except FileNotFoundError:
            print("comando incorreto!")

        # termina o programa
        if aliquot < 0:
            print("Programa finalizado! Sua Aliquota de uso passou do limite!")

if __name__ == "__main__":
    main()
