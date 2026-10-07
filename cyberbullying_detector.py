import joblib


# Load trained ML model and TF-IDF vectorizer
model = joblib.load("cyberbullying_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")


def detect_cyberbullying(message):
    # Convert message into TF-IDF features
    message_tfidf = vectorizer.transform([message])

    # Predict using trained model
    prediction = model.predict(message_tfidf)[0]

    if prediction == 1:
        return "Potentially Harmful"
    else:
        return "Safe"


def remediate_content():
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
                message = remediate_content()
                print("Remediated Message:", message)

        elif choice == "2":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()