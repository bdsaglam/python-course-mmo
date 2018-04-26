# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this example, we create a bit
more complicated window layout using
the QGridLayout manager.

author: Jan Bodnar
website: zetcode.com
last edited: January 2015
"""

import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
                             QTextEdit, QGridLayout, QApplication, QPushButton)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        browseTitleButton = QPushButton("...", self)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 0, 0)
        grid.addWidget(titleEdit, 0, 1)
        grid.addWidget(browseTitleButton, 0, 2)

        grid.addWidget(author, 1, 0,)
        grid.addWidget(authorEdit, 1, 1, 1, 2)

        grid.addWidget(review, 2, 0)
        grid.addWidget(reviewEdit, 2, 1, 5, 2)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
