import os
import shutil

def organize_files(directory):
    """Organiza arquivos em pastas baseadas em suas extensões."""
    if not os.path.exists(directory):
        return f"Erro: O diretório {directory} não existe."

    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    count = 0
    for file in files:
        ext = file.split('.')[-1].lower() if '.' in file else 'outros'
        target_folder = os.path.join(directory, ext.upper())
        
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
            
        shutil.move(os.path.join(directory, file), os.path.join(target_folder, file))
        count += 1
        
    return f"Sucesso! {count} arquivos organizados por extensão."

if __name__ == "__main__":
    # Teste rápido
    test_dir = "./test_folder"
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)
        open(os.path.join(test_dir, "teste.txt"), 'w').close()
        open(os.path.join(test_dir, "foto.jpg"), 'w').close()
    print(organize_files(test_dir))
