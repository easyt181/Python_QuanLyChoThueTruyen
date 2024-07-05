from PySide6.QtWidgets import QApplication
from frontPage import MySidebar
import sys

app = QApplication(sys.argv)

window = MySidebar()

window.show()
app.exec()