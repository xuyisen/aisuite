from typing import Literal

from aisuite.framework.message import Message


class Choice:
    def __init__(self):
        self.finish_reason: Literal["stop", "tool_calls"] | None = None
        self.message = Message(
            content=None,
            tool_calls=None,
            role="assistant",
            refusal=None,
            reasoning_content=None,
        )
        self.intermediate_messages: list[Message] = []
