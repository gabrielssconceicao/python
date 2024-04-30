import os

def list_files_and_dirs_tail_recursive(path, level=1, content=None):
    if content is None:
        content = os.listdir(path)
    if len(content) == 0:
        return
    item = content.pop(0)
    item_path = os.path.join(path, item)
    if os.path.isdir(item_path):
        print(
            "\t" * level + f"{item}/")
        new_content = os.listdir(item_path)
        content = new_content + content
        list_files_and_dirs_tail_recursive(item_path, level + 1, content)
    else:
        print("\t" * level + item)
    return list_files_and_dirs_tail_recursive(path, level,content)


# Exemplo de uso:
directory_path = 'C:\\Users\gabri\Documents\Python'
directory_path2 = 'C:\Development\Tools\Java'
list_files_and_dirs_tail_recursive(directory_path2)
