def read_file(file_path):
    """Read content from a text file and return list of lines."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def filter_and_write(input_path, output_path, keyword):
    """Filter lines containing keyword and write to a new file."""
    lines = read_file(input_path)
    filtered_lines = [line for line in lines if keyword in line]
    with open(output_path, 'w', encoding='utf-8') as file:
        file.writelines(filtered_lines)