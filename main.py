import json
from notesmanger import NotesManager
from saving import save_note
print("Welcome to My Notes\n")


save = save_note
manager = NotesManager()
manager.load_notes()

while True:
    print("\nMenu:")
    print("1. Add a note")
    print("2. View all note titles")
    print("3. View a note by title")
    print("4. Edit a note")
    print("5. delete a note")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        title, note = save.get_note_input()
        note_dict = {title: note}
        save.save_note(note_dict)
        manager.load_notes()
        print(f"Note '{title}' saved!")

    elif choice == "2":
        manager.print_all_titles()

    elif choice == "3":
        search_title = input("Enter the title: ")
        title, note = manager.get_note_by_title(search_title)
        if title:
            print(f"\nTitle: {title}\nNote: {note}")
        else:
            print("Note not found!")

    elif choice == "4":
        edit_title = input("Enter the title to edit: ")
        _, current_note = manager.get_note_by_title(edit_title)

        if current_note is None:
            print("Note not found!")
        else:
            print(f"Current note: {current_note}")
            new_note = input("Enter the new note: ")

            if manager.edit_note_by_title(edit_title, new_note):
                manager.load_notes()
                print("Note updated!")
            else:
                print("Error updating note.")

    elif choice == "6":
        print("Exiting...")
        break
    elif choice == "5":
        manager.delete_note_by_title()


    else:
        print("Invalid choice. Try again!")