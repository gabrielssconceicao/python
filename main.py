import os
from pprint import pprint
# ANSI escape codes for colors
COLOR_BLUE = "\033[94m"
COLOR_RESET = "\033[0m"

def list_files2(directory):
    for item in os.listdir(directory):
        full_path = os.path.join(directory, item)
        if os.path.isfile(full_path):
            print(full_path)
        elif os.path.isdir(full_path):
            list_files(full_path)

def list_files(directory, accumulator=None, level=0):
    if accumulator is None:
        accumulator = []

    for item_name in os.listdir(directory):
        item_path = os.path.join(directory, item_name)
        if os.path.isfile(item_path):
            accumulator.append((level, item_name))
        elif os.path.isdir(item_path):
            accumulator.append((level, COLOR_BLUE + item_name + COLOR_RESET))
            list_files(item_path, accumulator, level + 1)  # Recursive call for subdirectory

    return accumulator



def mostrar():
    #arquivos = list_files("C:\Development\IDEs_Projects\VSCode")
    #directory = input("Enter the directory path: ")
    directory = "C:\Development\IDEs_Projects\VSCode"
    if os.path.exists(directory):
        files = list_files2(directory)
        if files:
            print("Files found:")
            for level, file in files:
                print("    " * level + file)
        else:
            print("No files found in this directory and subdirectories.")
    else:
        print("The specified directory does not exist.")


def menu():
    print("""Escolha uma opção:
    [1] Listar Diretórios
    [2] Sair
    """)
    
    while True:
        try:
            opcao = int(input("Sua opção: "))
            
            if opcao not in [1,2]:
                raise ValueError("Opção inválida")
            return opcao
        except ValueError as ve:
            print("Digite um número")
       

def main():
    while True:
        opcao = menu()
        
        if opcao == 1:
            mostrar()
        elif opcao == 2:
            break


if __name__ == "__main__":
    main()
