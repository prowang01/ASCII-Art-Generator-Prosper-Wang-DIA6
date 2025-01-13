import pyfiglet

def generate_ascii_art(text: str) -> str:
    """
    Generate ASCII art from a given text using pyfiglet.
    """
    try:
        ascii_art = pyfiglet.figlet_format(text)
        return ascii_art
    except Exception as e:
        return f"Error generating ASCII art: {e}"

if __name__ == "__main__":
    # Generate and display an ASCII art welcome message
    welcome_art = generate_ascii_art("ASCII Art Generator")
    print(welcome_art)
    print("Type your text below to generate ASCII art. (Type 'exit' to quit)\n")

    while True:
        user_input = input("Enter text (or type 'exit' to quit): ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        art = generate_ascii_art(user_input)
        print(art)
