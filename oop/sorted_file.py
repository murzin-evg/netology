import os


def sorted_files_line_length():
    current = os.getcwd()
    folder1 = 'oop'
    folder2 = 'sorted'
    files = os.listdir(os.path.join(current, folder1, folder2))

    result = {}
    for file_name in files:
        full_path = os.path.join(current, folder1, folder2, file_name)
        with open(full_path, 'rt') as file:
            result[file_name] = len(file.readlines())

    sorted_tuples = sorted(result.items(), key=lambda item: item[1])
    sorted_result = {key: value for key, value in sorted_tuples}
    return sorted_result


def write_file(sorted_dict):
    full_path = os.path.join(os.getcwd(), 'oop', 'result.txt')
    with open(full_path, 'w', encoding='utf-8') as file:
        for key, value in sorted_dict.items():
            file.write(f'{key}\n')
            file.write(f'{value}\n')

            for i in range(1, value+1):
                file.write(f'Строка номер {i} файла номер {key.strip(".txt")}\n')
            

sorted_dict = sorted_files_line_length()
write_file(sorted_dict)