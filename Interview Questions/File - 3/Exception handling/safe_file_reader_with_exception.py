#35. Implement a safe file reader that handles `FileNotFoundError`.
def safe_file_reader(filename):
    try:
        with open(filename,'r',encoding="UTF-8") as file:
            content=file.read()
            print("File content:\n",content)
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found")
    except Exception as e:
        print("An unecepted occured",e)
filename="example.txt"
safe_file_reader(filename)
        