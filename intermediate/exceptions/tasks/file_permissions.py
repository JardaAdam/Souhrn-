
# Napis funkciu append_text(filename, text), ktora doplni text `text` do suboru s nazvom `filename`.
# Ak je subor readonly, osetri tento pripad tak, ze vypises na vystup "Cannot write to file <filename>"
# Pre windows userov, ako nastavit, aby bol subor readonly:
# https://adamtheautomator.com/how-to-make-a-file-read-only/

# with open("text_file.txt", "a") as file:
#     file.write("\nthis line write by append")
#
#
# with open("readonly_file.txt", "a") as new_file:
#     new_file.writelines("\nI want to write here")

def append_text(filename: str, text: str) -> None:
    try:
        with open(filename, 'a') as file:
            """ 'a' = append """
            print(text, file=file)
            """in print we writen to our file"""
    except PermissionError:
        print(f"Cannot write to this file {filename}")


if __name__ == "__main__":
    append_text('text_file.txt', '\nadd some words to this file')
    append_text('readonly_file.txt', 'I learn how do exceptions')
