name = input("Please type you name: ").lower()  # .lower() converts the input into all lowercase letters
print(f"Welcome to the code {name.title()}")  # .title converts the first letter of output into capital letter


ID = "SABY1998"
input_id = input("Type your id: ").upper()  # .upper() converts the input into all uppercase letters

if input_id == ID:
    print("Welcome onboard Saby!")
else:
    print(f"Code does not recognise you.{input_id}")
    # Here type something rather than saby1998, this statement will
    # show what is .upper() doing
