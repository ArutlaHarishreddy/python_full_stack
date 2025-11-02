#Write a function that writes a list of numbers to a file (one per line).
def write_numbers_to_file(numbers, filename):
    try:
        with open(filename,"w",encoding="utf-8") as file:
            for num in numbers:
                file.write(str(num) +"\n")
        print(f"Numbers written successfully to {filename}")
        with open(filename,'r',encoding="utf-8") as file:
            print(file.read())
        
    except Exception as e:
        print("Error:",e)
numbers=[10,20,30,40,50]
write_numbers_to_file(numbers,"numbers.txt")