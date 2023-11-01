
contacts = {}

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Invalid command format"
    return wrapper

@input_error
def add_contact(input_str):
    parts = input_str.split()
    name, phone = parts[1], parts[2]
    contacts[name] = phone
    return f"Contact {name} added with phone {phone}"

@input_error
def change_contact(input_str):
    parts = input_str.split()
    name, phone = parts[1], parts[2]
    if name in contacts:
        contacts[name] = phone
        return f"Phone number for {name} changed to {phone}"
    else:
        return f"Contact {name} not found"

@input_error
def phone_contact(input_str):
    name = input_str.split()[1]
    if name in contacts:
        return f"Phone number for {name} is {contacts[name]}"
    else:
        return f"Contact {name} not found"

@input_error
def show_all_contacts(input_str):
    if not contacts:
        return "No contacts found"
    result = "All contacts:\n"
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result

def main():
    print("How can I help you?")
    
    while True:
        user_input = input().strip().lower()

        if user_input == "hello":
            print("How can I help you?")
        elif user_input.startswith("add "):
            response = add_contact(user_input)
            print(response)
        elif user_input.startswith("change "):
            response = change_contact(user_input)
            print(response)
        elif user_input.startswith("phone "):
            response = phone_contact(user_input)
            print(response)
        elif user_input == "show all":
            response = show_all_contacts(user_input)
            print(response)
        elif user_input in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
