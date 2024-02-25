from abc import ABC, abstractmethod


class Document(ABC):
    @abstractmethod
    def create_header(self):
        pass

    @abstractmethod
    def create_body(self):
        pass

# kl pake abscrat decor, wajib di implement
    @abstractmethod
    def create_footer(self):
        pass


class PDFDocument(Document):
    def create_header(self):
        return "PDF Header"

    def create_body(self):
        return "PDF Body"

    def create_footer(self):
        return "PDF Footer"


class HTMLDocument(Document):
    def create_header(self):
        return "HTML Header"

    def create_body(self):
        return "HTML Body"

    def create_footer(self):
        return "HTML Footer-00"


class DocumentFactory:
    def createPDF(self):
        return PDFDocument()

    def createHTML(self):
        return HTMLDocument()


document = DocumentFactory()

pdf = document.createPDF()
html = document.createHTML()

print(pdf, html)
