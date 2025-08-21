name = input("Enter nam: ")
password = input("Enter pasword: ")
nam = name.lower()          
nam = nam.replace(" ", "_")  
password_length = len(password)
print
print(f"Username: {nam}")
print(f"Password Length: {password_length}")
print("========")
print("Password length >= 8:", password_length >= 8)
print("Username is 'admin':", nam == "admin")
print("Password is '1234':", password == "1234")
print("This is the default account!" if nam == "admin" and password == "1234" else "Not the default account.")
print(f"= Welcome {name} =")



