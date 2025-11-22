import json
notes = []
def add_note():
    text = input("Enter your note: ")
    note = {
        "id": len(notes) + 1,
        "text": text
    }
    notes.append(note)
    print("Note added successfully ")

def view_notes():
    if not notes:
        print("No notes available")
        return

    print("\nYour notes: ")
    for note in notes:
        print(f"{note['id']}.{note['text']}")

def search_notes():
    keyword = input("Enter a keyword to search: ").lower()

    results = []

    for note in notes:
        if keyword in note["text"].lower():
            results.append(note)
    if not results:
        print("No matching notes found.")
        return
    print("\nSearch results: ")
    for note in results:
        print(f"{note["id"]}.{note["text"]}")

def delete_notes():
    if not notes:
        print("No notes to delete")
        return

    print("\n Your notes: ")
    for note in notes:
        print(f"{note["id"]}. {note["text"]}")

    try:
        note_id = int(input("Enter the id of the note to delete: "))
    except ValueError:
        print("Invalid ID, please enter a number")
        return

    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            print("Note deleted successfully")
            break

    else:
        print("No note found with that ID")

    for index, note in enumerate(notes, start=1):
        note["id"] = index

def save_notes():
    with open("notes.json", "w") as file:
        json.dump(notes, file, indent=4)
    print("Notes saved successfully")

def load_note():
    global notes
    try:
        with open("notes.json", "r") as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []

def edit_note():
    if not notes:
        print("No notes to edit")
        return
    print("\nYour Notes:")
    for note in notes:
        print(f"{note["id"]}.{note["text"]}")

    try:
        note_id = int(input("Enter the ID of the note to edit: "))
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return

    for note in notes:
        if note["id"] == note_id:
            print(f"Current text: {note['text']}")
            new_text = input("Enter New Text: ")
            note["text"] = new_text
            print("Note updated successfully")
            return

    print("No note found with that ID")


def main():

    load_note()
    while True:
        print("\n--- My NoteBook ---")
        print("1. Add a note")
        print("2.  View notes")
        print("3. Search notes ")
        print("4. Delete Notes")
        print("5. Save notes")
        print("6. Edit notes")
        print("7. Quit")

        choice = input("Choose an option: ")


        if choice ==  "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            search_notes()
        elif choice == "4":
            delete_notes()
        elif choice == "5":
            save_notes()
        elif choice == "6":
            edit_note()
        elif choice == "7":
            save_notes()
            print("Goodbye")
            break
        else:
            print("Invalid Choice, try again!")

if __name__ == "__main__":
    main()






