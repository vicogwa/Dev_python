# this code reads existing file
with open ("file_reader.py", "r") as file:
   for line in file:
      print(f"hello", line.rstrip())


