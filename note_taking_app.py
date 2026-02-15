import json
import os

NOTES_FILE = "notes.json"

def load_notes():
    if os.path.exists(NOTES_FILE):
        try:
            with open(NOTES_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []
    return []


def save_notes(notes):
    try:
        with open(NOTES_FILE, "w", encoding="utf-8") as f:
            json.dump(notes, f, ensure_ascii=False, indent=2)
    except Exception:
        pass


def add_note(notes, text):
    notes.append(text)
    return notes


def delete_note(notes, index):
    if 0 <= index < len(notes):
        return notes.pop(index)
    raise IndexError("Invalid index")


def edit_note(notes, index, new_text):
    if 0 <= index < len(notes):
        notes[index] = new_text
        return notes
    raise IndexError("Invalid index")


def list_notes(notes):
    if not notes:
        print("No notes.")
        return
    for i, note in enumerate(notes, start=1):
        print(f"{i}. {note}")


def note_taking_app():
    notes = load_notes()

    while True:
        print("\n--- Note Taking Application ---")
        print("1: Add a new note")
        print("2: Delete a note")
        print("3: Edit a note")
        print("4: List notes")
        print("5: Exit program")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            new_note = input("Enter your new note: ").strip()
            if new_note:
                add_note(notes, new_note)
                save_notes(notes)
                print("Note added successfully!")
            else:
                print("Empty note not added.")

        elif choice == "2":
            if notes:
                list_notes(notes)
                try:
                    idx = int(input("Enter the note number to delete: "))
                    removed = delete_note(notes, idx - 1)
                    save_notes(notes)
                    print(f"Note '{removed}' deleted.")
                except ValueError:
                    print("Please enter a valid number.")
                except IndexError:
                    print("Invalid note number.")
            else:
                print("No notes to delete.")

        elif choice == "3":
            if notes:
                list_notes(notes)
                try:
                    idx = int(input("Enter the note number to edit: "))
                    new_text = input("Enter the new text: ").strip()
                    if new_text:
                        edit_note(notes, idx - 1, new_text)
                        save_notes(notes)
                        print("Note updated successfully!")
                    else:
                        print("Empty text. Note not changed.")
                except ValueError:
                    print("Please enter a valid number.")
                except IndexError:
                    print("Invalid note number.")
            else:
                print("No notes to edit.")

        elif choice == "4":
            list_notes(notes)

        elif choice == "5":
            save_notes(notes)
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    note_taking_app()
