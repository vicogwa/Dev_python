# the code below is use to re-write new items to file
name = input("what is your name? ")
file = open ("file_reader.py", "w")
file.write(name)
file.close()

