from dataclasses import dataclass

from prompts.system import get_system_prompt


@dataclass
class MessageItem:
    role: str
    content: str
    token_count: int | None = None


class ContextManager:
    def __int__(self) -> None:
        self._system_prompt = get_system_prompt()
        self._messages: list[MessageItem] = []
