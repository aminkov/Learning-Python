def convert1251(string, filename):
    with open(filename, mode='wb') as fh:
        fh.write(encoded_str)

convert1251("здравейте", "textfile.txt")

def upper_1251(filename):
    with open(filename, mode="rb") as fh:
        bytes = fh.read()
        #0417
        print(bytes)

