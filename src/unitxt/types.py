from typing import Any, Dict, List, Literal, NewType, Optional, Type, TypedDict, Union

from .type_utils import register_type

Text = NewType("Text", str)
Number = NewType("Number", Union[float, int])


class Turn(TypedDict):
    role: Literal["system", "user", "agent"]
    content: Text


class RagResponse(TypedDict):
    answer: str
    contexts: List[str]
    context_ids: Union[List[int], List[str]]
    is_answerable: bool


Dialog = NewType("Dialog", List[Turn])


class Image(TypedDict):
    image: Any
    format: str


class Document(TypedDict):
    title: str
    body: str


MultiDocument = NewType("MultiDocument", List[Document])

Video = NewType("Video", List[Image])


class Audio(TypedDict):
    audio: Any


class Table(TypedDict):
    header: List[str]
    rows: List[List[Any]]


class SQLDatabase(TypedDict):
    db_id: Optional[str]
    db_type: Literal["local", "in_memory", "remote"]
    dbms: Optional[str]
    data: Optional[Dict[str, Dict]]

class Parameter(TypedDict):
    name: str
    type: Optional[Type]  # Using actual Python type objects

class Tool(TypedDict):
    name: str
    description: str
    parameters: List[Parameter]

class ToolCall(TypedDict):
    name: str
    arguments: Dict[str, Any]

register_type(Text)
register_type(Number)
register_type(Turn)
register_type(Dialog)
register_type(Table)
register_type(Audio)
register_type(Image)
register_type(Video)
register_type(Document)
register_type(MultiDocument)
register_type(RagResponse)
register_type(SQLDatabase)
register_type(Parameter)
register_type(Tool)
register_type(ToolCall)

