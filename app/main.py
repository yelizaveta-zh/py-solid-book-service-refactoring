import json
import xml.etree.ElementTree as ET
from abc import abstractmethod, ABC


class DisplayStrategy(ABC):
    @abstractmethod
    def display(self, content: str) -> None:
        pass


class ConsoleDisplay(DisplayStrategy):
    def display(self, content: str) -> None:
        print(content)


class ReverseDisplay(DisplayStrategy):
    def display(self, content: str) -> None:
        print(content[::-1])


class PrintStrategy(ABC):
    @abstractmethod
    def print_book(self, title: str, content: str) -> None:
        pass


class ConsolePrint(PrintStrategy):
    def print_book(self, title: str, content: str) -> None:
        print(f"Printing the book: {title}...")
        print(content)


class ReversePrint(PrintStrategy):
    def print_book(self, title: str, content: str) -> None:
        print(f"Printing the book in reverse: {title}...")
        print(content[::-1])


class SerializationStrategy(ABC):
    @abstractmethod
    def serialize(self, title: str, content: str) -> str:
        pass


class JSONSerialization(SerializationStrategy):
    def serialize(self, title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})


class XMLSerialization(SerializationStrategy):
    def serialize(self, title: str, content: str) -> str:
        root = ET.Element("book")
        title_element = ET.SubElement(root, "title")
        title_element.text = title
        content_element = ET.SubElement(root, "content")
        content_element.text = content
        return ET.tostring(root, encoding="unicode")


class Book:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    def display(self, strategy: DisplayStrategy) -> None:
        strategy.display(self.content)

    def print_book(self, strategy: PrintStrategy) -> None:
        strategy.print_book(self.title, self.content)

    def serialize(self, strategy: SerializationStrategy) -> str:
        return strategy.serialize(self.title, self.content)


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            book.display(method_type)
        elif cmd == "print":
            book.print_book(method_type)
        elif cmd == "serialize":
            return book.serialize(method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
