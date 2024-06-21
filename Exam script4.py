from abc import ABC, abstractmethod


class Document(ABC):
    @abstractmethod
    def print(self):
        pass

    def prepare_for_printing(self):
        print("Preparing document for printing...")
        self.print()


class PDFDocument(Document):
    def print(self):
        print("Printing PDF document")


class WordDocument(Document):
    def print(self):
        print("Printing Word document")


class ExcelDocument(Document):
    def print(self):
        print("Printing Excel document")


class DocumentFactory:
    @staticmethod
    def create_document(doc_type):
        if doc_type == "pdf":
            return PDFDocument()
        elif doc_type == "word":
            return WordDocument()
        elif doc_type == "excel":
            return ExcelDocument()
        else:
            raise ValueError(f"Unknown document type: {doc_type}")


if __name__ == "__main__":
    
    factory = DocumentFactory()

    pdf_doc = factory.create_document("pdf")
    word_doc = factory.create_document("word")
    excel_doc = factory.create_document("excel")

    pdf_doc.prepare_for_printing()
    word_doc.prepare_for_printing()
    excel_doc.prepare_for_printing()
