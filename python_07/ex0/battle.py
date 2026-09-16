from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def render(self) -> str:
        ...


class TextReport(Document):
    def render(self) -> str:
       return "Informe en texto"


class TextReceipt(Document):
    def render(self) -> str:
        return "Recibo en texto"


class HtmlReport(Document):
    def render(self) -> str:
        return "<h1>Informe</h1>"


class HtmlReceipt(Document):
    def render(self) -> str:
        return "<p>Recibo</p>"


class DocumentFactory(ABC):
    @abstractmethod
    def create_report(self) -> Document:
        ...

    @abstractmethod
    def create_receipt(self) -> Document:
        ...


class TextFactory(DocumentFactory):
    def create_report(self) -> Document:
        return TextReport()

    def create_receipt(self) -> Document:
        return TextReceipt()


class HtmlFactory(DocumentFactory):
    def create_report(self) -> Document:
        return HtmlReport()

    def create_receipt(self) -> Document:
        return HtmlReceipt()

def preview_documents(factory: DocumentFactory) -> None:
        report = factory.create_report()
        receipt = factory.create_receipt()
        print(report.render())
        print(receipt.render())

preview_documents(TextFactory())
preview_documents(HtmlFactory())


