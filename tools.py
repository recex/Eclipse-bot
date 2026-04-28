import json
import csv
import os

def csv_to_json(csv_path, json_path):
    """Converte um arquivo CSV para JSON."""
    try:
        data = []
        with open(csv_path, encoding='utf-8') as csvf:
            csv_reader = csv.DictReader(csvf)
            for rows in csv_reader:
                data.append(rows)
        
        with open(json_path, 'w', encoding='utf-8') as jsonf:
            jsonf.write(json.dumps(data, indent=4))
        return f"Conversão concluída: {json_path}"
    except Exception as e:
        return f"Erro na conversão: {str(e)}"

def calculate_stats(numbers):
    """Realiza cálculos básicos em uma lista de números."""
    if not numbers:
        return "Nenhum dado para calcular."
    
    try:
        nums = [float(n) for n in numbers]
        stats = {
            "soma": sum(nums),
            "media": sum(nums) / len(nums),
            "max": max(nums),
            "min": min(nums),
            "quantidade": len(nums)
        }
        return stats
    except ValueError:
        return "Erro: A lista deve conter apenas números."

if __name__ == "__main__":
    print("Módulo de ferramentas carregado.")
    print(f"Cálculo teste: {calculate_stats([10, 20, 30])}")
