
def write_file(file_name, file_content):
    # Ensure the file has a .txt extension
    file_name = f"{file_name}.txt"
    
    # Open the file in write mode and write the content
    with open(file_name, 'w') as file:
        file.write(file_content)

def append_file(file_name, file_content):
    # Ensure the file has a .txt extension
    file_name = f"{file_name}.txt"
    
    # Open the file in append mode and add the content
    with open(file_name, 'a') as file:
        file.write(file_content)

def read_file(file_name):
    # Ensure the file has a .txt extension
    file_name = f"{file_name}.txt"
    
    # Open the file in read mode and return the content
    with open(file_name, 'r') as file:
        content = file.read()
    
    return content
