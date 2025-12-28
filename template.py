import os

# Use current directory as project root
BASE_DIR = os.getcwd()

STRUCTURE = {
    "": [
        "app.py",
        ".env",
        "requirements.txt",
    ],
    "peya": [
        "assistant.py",
        "gemini_engine.py",
        "prompt_controller.py",
        "memory.py",
    ],
    "config": [
        "settings.py",
    ],
}

def create_project_structure():
    print(f"Using current folder as project root:")
    print(f"{BASE_DIR}\n")

    for folder, files in STRUCTURE.items():
        folder_path = os.path.join(BASE_DIR, folder)

        # Create folder only if it doesn't exist
        if folder and not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Created folder: {folder}")

        for file in files:
            file_path = os.path.join(folder_path, file)

            if not os.path.exists(file_path):
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write("")
                print(f"Created file: {file_path}")
            else:
                print(f"Already exists: {file_path}")

    print("\nProject structure ready in current folder!")

if __name__ == "__main__":
    create_project_structure()
