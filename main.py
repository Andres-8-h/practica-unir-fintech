"""
License: Apache
Organization: UNIR
"""

import os
import sys

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False
DEFAULT_UPPERCASE = False
DEFAULT_MIN_LENGTH = 0 

def sort_list(items, ascending=True):
    if not isinstance(items, list):
        raise RuntimeError(f"No puede ordenar {type(items)}")

    return sorted(items, reverse=(not ascending))


def remove_duplicates_from_list(items):
    return list(set(items))


def convert_to_uppercase(items):
    """Convierte todas las palabras de la lista a mayúsculas"""
    return [word.upper() for word in items]


def filter_by_min_length(items, min_length):
    """Filtra las palabras que tienen una longitud mayor o igual a min_length"""
    return [word for word in items if len(word) >= min_length]

def count_word_frequencies(items):
    """Cuenta la frecuencia de cada palabra en la lista"""
    frequencies = {}
    for word in items:
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies


if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES
    convert_uppercase = DEFAULT_UPPERCASE
     min_length = DEFAULT_MIN_LENGTH
    
    if len(sys.argv) >= 3:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
        
        if len(sys.argv) >= 4:
            convert_uppercase = sys.argv[3].lower() == "yes"
    else:
        print("Se debe indicar el fichero como primer argumento")
        print("El segundo argumento indica si se quieren eliminar duplicados")
        print("El tercer argumento (opcional) indica si convertir a mayúsculas")
        sys.exit(1)

    print(f"Se leerán las palabras del fichero {filename}")
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        print(f"El fichero {filename} no existe")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    if remove_duplicates:
        word_list = remove_duplicates_from_list(word_list)
        
    if convert_uppercase:
        word_list = convert_to_uppercase(word_list)
    if min_length > 0:
        word_list = filter_by_min_length(word_list, min_length)   
    
    print("\nFrecuencia de palabras:")
    frequencies = count_word_frequencies(word_list)
    for word, count in frequencies.items():
        print(f"{word}: {count}")


    print(sort_list(word_list))