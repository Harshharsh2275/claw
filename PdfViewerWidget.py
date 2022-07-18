from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtWebEngineWidgets import *
from PySide2.QtWebEngineCore import *
from os import getcwd, path
import sys

# Config settings for pdfjs and its dependencies
PDFJS = f"file:///{path.abspath('./libs/pdfjs/web/viewer.html')}".replace('\\', '/')
print(PDFJS)


class PdfViewer(QWebEngineView):

    def __init__(self, PdfPath) -> None:
        super(PdfViewer, self).__init__()

        # Configuration settings for the web engine
        self.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        self.settings().setAttribute(QWebEngineSettings.PdfViewerEnabled, True)
        self.settings().setAttribute(QWebEngineSettings.LocalContentCanAccessFileUrls, True)
        self.settings().setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)
        self.requestInterceptor = NWUrlRequestInterceptor(
            {'Access-Control-Allow-Origin': '*'})
        self.page().profile().setUrlRequestInterceptor(self.requestInterceptor)
        # *******************************************
        # self.load(QUrl.fromUserInput(
        #     f"{PDFJS}?file=https://www.opportunitiesforyouth.org/wp-content/uploads/2021/04/Atomic_Habits_by_James_Clear-1.pdf"))
        self.load(QUrl.fromLocalFile(
            f"{path.abspath(getcwd() + './ui/richdad.pdf')}"))
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self)
        self.setLayout(self.layout)
        pass


class NWUrlRequestInterceptor(QWebEngineUrlRequestInterceptor):
    def __init__(self, headers):
        super(NWUrlRequestInterceptor, self).__init__()
        self.headers = headers

    def set_headers(self, headers):
        self.headers = headers

    def interceptRequest(self, info):
        # print(info, self.headers)
        for header in self.headers:
            info.setHttpHeader(b'Access-Control-Allow-Origin', b'*')


# Uncomment to run on its own or else will be included in the main file
# as component
PDF = path.abspath(getcwd()+"/ui/richdad.pdf")
app = QApplication(sys.argv)
viewer = PdfViewer(PdfPath=PDF)
viewer.show()
app.exec_()
