import json
class save_note:
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