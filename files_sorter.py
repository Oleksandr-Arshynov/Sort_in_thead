import os
import shutil
from concurrent.futures import ThreadPoolExecutor
"""
Ця програма призначена для сортування файлів у вказаній вихідній папці (`source_folder`)
за їхніми розширеннями та переміщення їх у відповідні папки у папці призначення
(`destination_folder`). Процес сортування паралелізований за допомогою ThreadPoolExecutor
для покращення продуктивності.
"""
def move_file(source_path, destination_path):
    
    """move_file(source_path, destination_path): Переміщує файл із вихідного шляху на
    шлях призначення. Виводить повідомлення про успішне переміщення, якщо переміщення
    відбулось успішно, та виводить повідомлення про помилку, якщо виникла яка-небудь
    виняткова ситуація під час переміщення."""
    
    try:
        shutil.move(source_path, destination_path)
        print(f"Moved {source_path} to {destination_path}")
    except Exception as e:
        print(f"Error moving {source_path}: {e}")


def process_folder(folder_path, destination_folder):
    
    """- process_folder(folder_path, destination_folder): Обробляє кожен файл у вказаній
    папці. Для кожного файлу визначається розширення, та файл переміщується у відповідну
    папку призначення."""
    
    try:
        for root, _, files in os.walk(folder_path):
            for file in files:
                source_path = os.path.join(root, file)
                extension = file.split('.')[-1].lower()
                destination_path = os.path.join(destination_folder, extension, file)

                with ThreadPoolExecutor() as executor:
                    executor.submit(move_file, source_path, destination_path)
    except Exception as e:
        print(f"Error processing folder {folder_path}: {e}")

if __name__ == "__main__":
    source_folder = "/Users/oleksandrarshinov/Desktop/Documents/Repository/Sort_in_thead/Garbage3" 
    destination_folder = "/Users/oleksandrarshinov/Desktop/Documents/Repository/Sort_in_thead/venv/SORTED"  

    # створює папки для кожного унікального розширення файлів у вхідній папці source_folder.
    for ext in set(file.split('.')[-1].lower() for _, _, files in os.walk(source_folder) for file in files):
        os.makedirs(os.path.join(destination_folder, ext), exist_ok=True)

    # Використання ThreadPoolExecutor для паралельної обробки кожної папки у вхідній папці. 
    with ThreadPoolExecutor() as executor:
        executor.submit(process_folder, source_folder, destination_folder)
