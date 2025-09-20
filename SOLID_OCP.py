# class Report():
#     def __init__(self, title, content):
#        self.title = title
#        self.content = content

#        def docPrinter(self):
#        print(f'сформирован отчёт - {self.title} - {self.content}')


from abc import ABC, abstractmethod

class Formatted(ABC):
    @abstractmethod
    def format(self, report):
        pass

class TextFormatted(Formatted):
    def format(self, report):
        print(report.title)
        print(report.content)

class HTMLFormatted(Formatted):
    def format(self, report):
        print(f'<h1>{report.title}</h1>')
        print(f'<p>{report.content}</p>')

class Report():
    def __init__(self, title, content, formatted):
        self.title = title
        self.content = content
        self.formatted = formatted

    def docPrinter(self):
        self.formatted.format(self)


report = Report('Заголовок отчёта', 'Тут много контента, это текст отчёта', HTMLFormatted())

report.docPrinter()





