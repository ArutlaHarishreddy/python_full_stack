# Write a generator that reads a large file line by line.
def read_large_file(filename):
    with open(filename,"r",encoding="utf-8") as file:
        for line in file:
            yield line.strip()

for line in read_large_file("example.txt"):
    print(line)