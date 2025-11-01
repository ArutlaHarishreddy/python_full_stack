#39. Create a context manager that opens a file and automatically closes it.
class FileManager:
    def __init__(self,filename, mode):
        self.filename=filename
        self.mode=mode
        self.file=None
    def __enter__(self):
        print(f"Opening file: {self.filename}")
        self.file=open(self.filename,self.mode,encoding="utf-8")
        return self.file
    def __exit__(self,exe_type,exe_value,traceback):
        if self.file:
            self.file.close()
            print(f"Closing file: {self.filename}")
        if exe_type:
            print(f"An error occured: {exe_value}")
        return False
    
with FileManager("example.txt","w") as f:
    f.write("Hello, Harish Reddy! This file was managed by custom context manager.")

with FileManager("example.txt", "r") as f:
    print(f.read())