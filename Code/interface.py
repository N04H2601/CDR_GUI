import sys
import webbrowser

from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Window(QMainWindow):

    def openFile(self):
        try:
            fileName, _ = QFileDialog.getOpenFileName(
                self, 'Open File', '/home', 'Image files (*.jpg *.gif *.png)', QDir.currentPath())
            if fileName:
                self.table_picture.hide()
                self._add_table_picture(fileName)

        except Exception as e:
            print(e)

    def redirectReglement(self):
        webbrowser.open(
            'https://wobbly-kryptops-c2e.notion.site/CDR-2023-a5c81e4559d4449bab987941d388ea8d', new=2)

    def default2022_2023(self):
        self.table_picture.hide()
        self._add_table_picture('table.png')

    def _create_menu_bar(self):
        self.menu_bar = self.menuBar()
        self.menu_bar.setStyleSheet('background-color: #B3C2FF;')
        self.file_menu = self.menu_bar.addMenu('File')
        self.edit_menu = self.menu_bar.addMenu('Edit')
        self.view_menu = self.menu_bar.addMenu('View')
        self.help_menu = self.menu_bar.addMenu('CDR Rules')

        self.openAction = QAction('Open', self)
        self.file_menu.addAction(self.openAction)

        self.defaultAction = QAction('Set 2022-2023 theme', self)
        self.file_menu.addAction(self.defaultAction)

        self.reglementAction = QAction('CDR 2022-2023', self)
        self.help_menu.addAction(self.reglementAction)

    def _connect_actions(self):
        self.openAction.triggered.connect(self.openFile)
        self.reglementAction.triggered.connect(self.redirectReglement)
        self.defaultAction.triggered.connect(self.default2022_2023)

    def _add_table_picture(self, filename='table.png'):
        self.table_picture = QLabel(self)
        pixmap = QPixmap(filename)
        pixmap = pixmap.scaled(
            self.size()/1.04, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        self.table_picture.setPixmap(pixmap)
        self.table_picture.setScaledContents(True)
        self.table_picture.setMaximumWidth(1430)
        self.table_picture.setStyleSheet('border: 2px solid white;')
        self.table_picture.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom | QtCore.Qt.AlignCenter)

        self.layout = QHBoxLayout()
        self.layout.addStretch(1)
        self.layout.addWidget(self.table_picture)
        self.layout.setContentsMargins(0, 0, 1, 0)
        self.layout.setAlignment(Qt.AlignCenter | Qt.AlignRight)

        self.main_layout.addLayout(self.layout)

    def _create_main_layout(self):
        self.main_layout = QHBoxLayout()
        self.main_layout.setSpacing(0)
        self.main_layout.setAlignment(Qt.AlignCenter)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.central_widget)

    def _create_actions_panel(self):
        self.actions_label = QLabel('Actions', self)
        self.actions_label.setStyleSheet(
            'color: white; font-size: 30px; border: 2px solid white; border-radius: 5px; padding: 5px;')
        self.actions_label.setAlignment(Qt.AlignCenter)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setOffset(0)
        shadow.setColor(QColor(0, 0, 0))
        self.actions_label.setGraphicsEffect(shadow)

        self.points_label = QLabel('Points', self)
        self.points_label.setStyleSheet(
            'color: white; font-size: 25px; border: 2px solid white; border-radius: 5px; padding: 5px;')
        self.points_label.setAlignment(Qt.AlignCenter)

        self.points_container = QLabel('0', self)
        self.points_container.setStyleSheet(
            'color: #22427C; font-size: 25px; border-radius: 5px; padding: 5px; background-color: white;')
        self.points_container.setAlignment(Qt.AlignCenter)

        self.points_layout = QHBoxLayout()
        self.points_layout.setAlignment(Qt.AlignCenter)
        self.points_layout.addWidget(self.points_label)
        self.points_layout.addSpacerItem(QSpacerItem(20, 0))
        self.points_layout.addWidget(self.points_container)

        self.actions_layout = QVBoxLayout()
        self.actions_layout.setAlignment(Qt.AlignCenter | Qt.AlignTop)
        self.actions_layout.addWidget(self.actions_label)
        self.actions_layout.addSpacerItem(QSpacerItem(0, 20))
        self.actions_layout.addLayout(self.points_layout)
        self.actions_layout.addStretch(1)
        self.actions_layout.addSpacerItem(QSpacerItem(410, 0))

        self.line = QFrame()
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setStyleSheet('color: white; border: 2px solid white;')

        self.main_layout.addLayout(self.actions_layout)
        self.main_layout.addSpacerItem(QSpacerItem(25, 0))
        self.main_layout.addWidget(self.line, 1)

    def __init__(self):
        super().__init__()
        self.setWindowTitle('CDR')
        self.setWindowIcon(QIcon('logo_cdr.png'))
        self.setStyleSheet('background-color: #22427C;')
        self.setMinimumSize(1900, 990)

        self._create_menu_bar()
        self._create_main_layout()
        self._create_actions_panel()
        self._add_table_picture()
        self._connect_actions()

        self.showMaximized()


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
