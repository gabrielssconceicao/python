import os


def list_files_and_dirs_tail_recursive(path, level=1, content=None,arquivos=None):
    if content is None:
        content = os.listdir(path)
    if len(content) == 0:
        return arquivos
    if arquivos is None:
        arquivos = []
    
    # Pegar o primeiro item do array content
    item = content.pop(0)
    path_item = os.path.join(path, item)
   
    
    #Verifica se é diretorio
    if os.path.isdir(path_item):
        new_files = os.listdir(path_item)
        arquivos.append({"file": item+"/", "level": level})
        result = list_files_and_dirs_tail_recursive(path_item,level+1,new_files)
        arquivos.extend(result)
    else:
        arquivos.append({"file": item, "level": level})
    return list_files_and_dirs_tail_recursive(path,level,content,arquivos)
    
    

directory_path = ""
files = list_files_and_dirs_tail_recursive(directory_path)
print(f"Arquivos de {directory_path}")
for file in files:
    print("\t" * file["level"] + file["file"])