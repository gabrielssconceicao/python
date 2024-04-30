import os


def list_files_and_dirs_tail_recursive(path, level=1, content=None):
    if content is None:
        content = os.listdir(path)
    if len(content) == 0:
        return
    
    # Pega o
    print(path)
    print(content)


# Exemplo de uso:
directory_path = 'C:\\Users\gabri\Documents\Python'
directory_path2 = 'C:\Development\Tools\Java'
list_files_and_dirs_tail_recursive(directory_path2)
