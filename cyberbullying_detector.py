# Cyberbullying Detection and Remediation
# A simple rule-based Python prototype for detecting
# potentially harmful messages and applying remediation.

def detect_cyberbullying(message):
    harmful_words = [
    "stupid",
    "idiot",
    "hate",
    "loser",
    "ugly",
    "shut up",
    "dumb"
]

    for word in harmful_words:
        if word in message.lower():
            return "Potentially Harmful"

    return "Safe"
    


def remediate_content(message):
    print("Action: Harmful content detected.")
    print("Action: Content removed.")
    return "[Content removed due to harmful language]"


def main():
    while True:
        print("\nCyberbullying Detection System")
        print("1. Check Message")
        print("2. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            message = input("Enter a message: ").strip()

            if not message:
                print("Message cannot be empty.")
                continue

            result = detect_cyberbullying(message)

            print("Result:", result)

            if result == "Potentially Harmful":
                message = remediate_content(message)
                print("Remediated Message:", message)

        elif choice == "2":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()