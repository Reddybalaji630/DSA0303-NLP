def generate_plural(noun):
    # Finite State Machine for plural formation

    if noun.endswith(("s", "x", "z", "ch", "sh")):
        # Add "es"
        return noun + "es"

    elif noun.endswith("y") and len(noun) > 1 and noun[-2].lower() not in "aeiou":
        # Replace "y" with "ies"
        return noun[:-1] + "ies"

    else:
        # Default: Add "s"
        return noun + "s"


# Main Program
word = input("Enter a singular noun: ")

plural = generate_plural(word)

print("Singular Noun :", word)
print("Plural Noun   :", plural)