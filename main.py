import json

print("Welcome to My Notes\n")

def get_note_input():
    title = input("What is the title: ")
    note = input("What is the note: ")
    return title, note

def save_note(note_dict):
    try:
        with open("notes.json", "r", encoding="utf-8") as file:
            try:
                notes = json.load(file)
            except json.JSONDecodeError:
                notes = []
    except FileNotFoundError:
        notes = []

    notes.append(note_dict)

    with open("notes.json", "w", encoding="utf-8") as file:
        json.dump(notes, file, indent=4)

class NotesManager:
    def __init__(self):
        self.data = []

    def load_notes(self):
        """Load notes safely, even if file is empty or invalid"""
        try:
            with open("notes.json", "r", encoding="utf-8") as f:
                try:
                    self.data = json.load(f)
                except json.JSONDecodeError:
                    self.data = []
        except FileNotFoundError:
            self.data = []

    def get_note_by_title(self, title):
        for note_dict in self.data:
            if title in note_dict:
                return title, note_dict[title]
        return None, None

    def print_all_titles(self):
        if not self.data:
            print("No notes found!")
            return

        print("\nAll note titles:")
        for idx, note_dict in enumerate(self.data, start=1):
            for key in note_dict.keys():
                print(f"{idx}. {key}")

manager = NotesManager()
manager.load_notes()

while True:
    print("\nMenu:")
    print("1. Add a note")
    print("2. View all note titles")
    print("3. View a note by title")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        title, note = get_note_input()
        note_dict = {title: note}
        save_note(note_dict)
        manager.load_notes()
        print(f"Note '{title}' saved!")

    elif choice == "2":
        manager.print_all_titles()

    elif choice == "3":
        search_title = input("Enter the title to view: ")
        title, note = manager.get_note_by_title(search_title)
        if title:
            print(f"\nTitle: {title}\nNote: {note}")
        else:
            print("Note not found!")

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Try again!")