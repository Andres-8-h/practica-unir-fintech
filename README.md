# Repo para EIEC - DevOps - UNIR
Este repositorio nos servirá para demostrar el uso de Git en la asignatura de EIEC y muchas cosas mas.
---
Los comandos del Makefile funcionarán en Linux y MacOS. En caso de usar Windows, necesitarás adaptarlos o ejecutarlos en una máquina virtual Linux.

## Ejecución
python3 main.py <filename> <dup> [<upper>]
  filename: **ruta** al fichero que contiene la lista de palabras, una por línea
  dup: **yes|no**, yes para eliminar palabras duplicadas, no para mantener la lista
  upper: **yes|no**, yes para convertir las palabras a mayúsculas, no para mantenerlas como están (opcional)

## Ejemplo de uso
```bash
# Ordenar palabras del archivo words.txt, eliminar duplicados y convertir a mayúsculas
python3 main.py words.txt yes yes

# Ordenar palabras del archivo my_words.txt y mantener duplicados
python3 main.py my_words.txt no

# Leer words.txt, eliminar duplicados, convertir a mayúsculas y filtrar palabras de al menos 6 caracteres
python3 main.py words.txt yes yes 6

# Frecuencia de palabras. 
python3 main.py words.txt yes yes
