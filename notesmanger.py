import json
class NotesManager:
    def __init__(self):
        self.data = []

    def load_notes(self):
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

    def edit_note_by_title(self, title, new_note):
        for note_dict in self.data:
            if title in note_dict:
                note_dict[title] = new_note

                with open("notes.json", "w", encoding="utf-8") as file:
                    json.dump(self.data, file, indent=4)

                return True
        return False
    def delete_note_by_title(self):
        title_to_delete = input("what is note title you want to delete: ")
        for note_dict in self.data:
            if title_to_delete in note_dict:
                self.data.remove(note_dict)
                with open("notes.json", "w", encoding="utf-8") as file:
                    json.dump(self.data, file, indent=4)
                    print(f"deleted {title_to_delete} from notes")
                return True
        return False