import os
import shutil
from concurrent.futures import ThreadPoolExecutor

def move_file(source_path, destination_path):
    try:
        shutil.move(source_path, destination_path)
        print(f"Moved {source_path} to {destination_path}")
    except Exception as e:
        print(f"Error moving {source_path}: {e}")

def process_folder(folder_path, destination_folder):
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
    source_folder = "/path/to/Хлам"  # Замініть це шляхом до вашої папки
    destination_folder = "/path/to/Sorted"  # Замініть це шляхом до папки для сортування

    # Creating destination folders for each extension
    for ext in set(file.split('.')[-1].lower() for _, _, files in os.walk(source_folder) for file in files):
        os.makedirs(os.path.join(destination_folder, ext), exist_ok=True)

    # Using ThreadPoolExecutor to parallelize folder processing
    with ThreadPoolExecutor() as executor:
        executor.submit(process_folder, source_folder, destination_folder)
