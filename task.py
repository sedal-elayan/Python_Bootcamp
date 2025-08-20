
name = input("Enter nam: ")

notes = input("Write your notes: ")


with open("notes.txt", "w") as f:
    f.write(f"Name: {name}\n")
    f.write(f"Notes: {notes}\n")
print("========")
with open("notes.txt", "r") as f:
    content = f.read()
print(content)
