import os
from organizer import organize_files
from tools import csv_to_json, calculate_stats
from web_bot import get_website_title

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        # clear_screen()
        print("\n" + "="*30)
        print("   ECLIPSE AUTOMATION CLI   ")
        print("="*30)
        print("1. Organizar Arquivos (por Extensão)")
        print("2. Converter CSV para JSON")
        print("3. Calcular Estatísticas de Números")
        print("4. Obter Título de um Site (Web)")
        print("0. Sair")
        print("="*30)
        
        choice = input("Escolha uma opção: ")
        
        if choice == '1':
            path = input("Digite o caminho da pasta: ")
            print(organize_files(path))
        
        elif choice == '2':
            csv_p = input("Caminho do arquivo CSV: ")
            json_p = input("Caminho de saída JSON: ")
            print(csv_to_json(csv_p, json_p))
            
        elif choice == '3':
            data = input("Digite os números separados por espaço: ")
            nums = data.split()
            print(calculate_stats(nums))
            
        elif choice == '4':
            url = input("Digite a URL do site: ")
            print(get_website_title(url))
            
        elif choice == '0':
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida!")
        
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()
