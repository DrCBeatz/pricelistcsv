import glob

read_files = glob.glob("draw/*.txt")

with open("result.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())
            outfile.write(bytes('\n\n', encoding='utf8'))