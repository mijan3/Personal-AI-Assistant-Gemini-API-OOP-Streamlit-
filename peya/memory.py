import json
import os
from typing import List, Dict


class Memory:
    """
    Memory class handles conversation persistence using a JSON file.
    """

    def __init__(self, file_path: str = "memory.json"):
        self.file_path = file_path
        self._ensure_memory_file()

    def _ensure_memory_file(self):
        """
        Create memory file if it does not exist.
        """
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w", encoding="utf-8") as f:
                json.dump([], f)

    def _load(self) -> List[Dict[str, str]]:
        """
        Load conversation history from JSON file.
        """
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def _save(self, data: List[Dict[str, str]]):
        """
        Save conversation history to JSON file.
        """
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def add(self, role: str, message: str):
        """
        Add a new message to memory.

        Args:
            role (str): 'user' or 'assistant'
            message (str): message content
        """
        history = self._load()
        history.append({
            "role": role,
            "message": message
        })
        self._save(history)

    def get_history(self) -> str:
        """
        Return formatted conversation history as text.
        """
        history = self._load()

        if not history:
            return "No previous conversation."

        formatted_history = []
        for item in history:
            role = item.get("role", "unknown").capitalize()
            message = item.get("message", "")
            formatted_history.append(f"{role}: {message}")

        return "\n".join(formatted_history)

    def clear(self):
        """
        Clear all conversation memory.
        """
        self._save([])
