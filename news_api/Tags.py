from .Tag import Tag, np
import openai

class Tags:
    def __init__(self):
        self._tags:list[Tag]