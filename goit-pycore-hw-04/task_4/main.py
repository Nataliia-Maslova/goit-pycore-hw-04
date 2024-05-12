

#def parse_input(): #рядок на команду та її аргументи
# введення команди "exit" або "close"
# add_contact(), change_contact(), show_phone() тощо.
# dict Ім'я буде ключем, а номер телефону – значенням
#  ідентифікувати та повідомляти про неправильно введені команди

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact changed."
    else:
        add_contact(args, contacts)

def show_phone(args, contacts):
    name, = args
    if name in contacts:
        return contacts[name]
    else:
        print("Contact doesn't exist.")

def all(contacts):
    print(contacts)



def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
