# Pialago, Nathaniel Christian M.  BSCS601

name = str(input("Name? "))
age = str(input("Age? "))
byear = str(input("Birthyear? "))

print("Your name is " + name + " at the age of " + age + ". You were born in " + byear + ".")

password = ""

while password != "default123":
    password = str(input("Please enter a password: "))
    
    if password == "default123":
        break
    else:
        print("Wrong password.")
print("Granted.")
