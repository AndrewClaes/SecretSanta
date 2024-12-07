import random
import os

def get_input(prompt):
    """Helper function for user input."""
    return input(prompt).strip()

def secret_santa():
    # Step 1: Input Names
    print("Welcome to the Secret Santa Generator!")
    print("Input participant names, separated by commas:")
    names = [name.strip() for name in get_input("Names: ").split(",")]
    
    # Validate input
    if len(names) < 2:
        print("You need at least 2 participants!")
        return

    # Step 2: Gather restrictions
    restrictions = {}
    for name in names:
        print(f"Who should {name} NOT draw? Separate names by commas or leave empty for no restrictions:")
        not_allowed = [na.strip() for na in get_input(f"{name}: ").split(",") if na.strip()]
        restrictions[name] = set(not_allowed)

    # Step 3: Assign Secret Santas with restrictions
    available_recipients = set(names)
    assignments = {}
    for giver in names:
        available = list(available_recipients - {giver} - restrictions[giver])
        if not available:
            print(f"Could not find a valid recipient for {giver}. Restarting...")
            return secret_santa()  # Restart if no valid assignments are possible

        recipient = random.choice(available)
        assignments[giver] = recipient
        available_recipients.remove(recipient)

    # Step 4: Output results
    print("Ready! Generating text files...")
    if not os.path.exists("SecretSanta"):
        os.makedirs("SecretSanta")

    for giver, recipient in assignments.items():
        with open(f"SecretSanta/{giver}_SecretSanta.txt", "w") as f:
            f.write(f"Hi {giver},\n\nYou are the Secret Santa for: {recipient}!\n\nHave fun!\n")
    
    print("All Secret Santa assignments have been saved in the 'SecretSanta' folder!")

# Run the program
if __name__ == "__main__":
    secret_santa()
