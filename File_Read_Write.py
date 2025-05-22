# File Read & Write with Error Handling in Python

def read_and_modify_file(input_filename):
    """
    Reads a file line by line, adds line numbers,
    and returns the modified content as a list.
    """
    modified_lines = []
    try:
        with open(input_filename, 'r') as file:
            for index, line in enumerate(file, start=1):
                # Add line number to the beginning of each line
                modified_lines.append(f"{index}: {line}")
        return modified_lines
    except FileNotFoundError:
        print(f"❌ Error: The file '{input_filename}' was not found.")
        return None
    except IOError:
        print(f"❌ Error: Could not read the file '{input_filename}'.")
        return None

def write_to_new_file(output_filename, lines):
    """
    Writes the modified lines to a new file.
    """
    try:
        with open(output_filename, 'w') as file:
            file.writelines(lines)
        print(f"✅ Successfully wrote to '{output_filename}'.")
    except IOError:
        print(f"❌ Error: Could not write to the file '{output_filename}'.")

def main():
    """
    Main program flow: Get filename from user, read and modify it,
    then write to a new file.
    """
    input_filename = input("📥 Enter the name of the file to read: ")
    modified_content = read_and_modify_file(input_filename)

    if modified_content:
        output_filename = "modified_" + input_filename
        write_to_new_file(output_filename, modified_content)

if __name__ == "__main__":
    main()
