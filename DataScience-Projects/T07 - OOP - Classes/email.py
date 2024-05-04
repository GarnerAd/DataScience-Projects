class Email:
    # Class variable
    has_been_read = False

    def __init__(self, email_address, subject_line, email_content):
        # Instance variables
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

    @classmethod
    def mark_as_read(cls):
        cls.has_been_read = True

# Initialise an empty list to store email objects
inbox = []

# Function to populate inbox with sample email objects
def populate_inbox():
    global inbox
    # Sample emails
    email1 = Email("student@HyperionDev.com", "Welcome to HyperionDev!", "Great work on the bootcamp!")
    email2 = Email("adams@HyperionDev.com", "Your excellent marks!", "Keep up the good work!")
    email3 = Email("teachers@HyperionDev.com", "Important announcement", "Don't forget about the upcoming meeting.")
    
    # Add sample emails to inbox
    inbox.extend([email1, email2, email3])

# Function to list emails in the inbox
def list_emails():
    print("Inbox:")
    for i, email in enumerate(inbox, start=1):
        print(f"{i}. {email.subject_line}")
    print()

# Function to read an email
def read_email():
    list_emails()  # Display the list of emails
    try:
        index = int(input("Enter the number of the email you want to read: ")) - 1
        if 0 <= index < len(inbox):
            email = inbox[index]
            if not email.has_been_read:
                print(f"\nSubject: {email.subject_line}")
                print(f"From: {email.email_address}")
                print(f"\n{email.email_content}\n")
                Email.mark_as_read()  # Mark the email as read
            else:
                print("\nThis email has already been read.\n")
        else:
            print("\nInvalid email number.\n")
    except ValueError:
        print("\nInvalid input. Please enter a number.\n")

# Populating inbox with sample emails
populate_inbox()

# Main function
def main():
    print("Welcome to the Email Simulator!\n")
    while True:
        print("Menu:")
        print("1. Read an email")
        print("2. View unread emails")
        print("3. Quit application")
        choice = input("Enter your choice: ")
        if choice == '1':
            read_email()
        elif choice == '2':
            unread_emails = [email.subject_line for email in inbox if not email.has_been_read]
            if unread_emails:
                print("\nUnread emails:")
                for email in unread_emails:
                    print(email)
                print()
            else:
                print("\nNo unread emails.\n")
        elif choice == '3':
            print("\nThank you for using the Email Simulator. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a valid option.\n")

if __name__ == "__main__":
    main()
