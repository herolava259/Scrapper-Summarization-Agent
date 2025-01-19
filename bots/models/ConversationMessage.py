from typing import List


class ConversationMessage:
    def __init__(self, role: str, content: str):
        self.Role = role
        self.Content = content
    Role: str
    Content: str

    def to_json_object(self) -> dict:

        return {'role': self.Role, 'content': self.Content}


