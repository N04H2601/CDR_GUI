import webbrowser

from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Window(QMainWindow):

    # Definition of the "openFile" method which opens an image file to replace the table picture
    def openFile(self):
        try:
            fileName, _ = QFileDialog.getOpenFileName(
                self, 'Open File', '/home', 'Image files (*.jpg *.gif *.png)', QDir.currentPath())
            if fileName:
                self.table_picture.hide()
                self._add_table_picture(fileName)

        except Exception as e:
            print(e)

    # Definition of the "redirectReglement" method which opens the CDR rules in a new tab
    def redirectReglement(self):
        webbrowser.open(
            'https://wobbly-kryptops-c2e.notion.site/CDR-2023-a5c81e4559d4449bab987941d388ea8d', new=2)

    # Definition of the "default2022_2023" method which sets the default theme of the table
    def default2022_2023(self):
        self.table_picture.hide()
        self._add_table_picture('images/table.png')

    # Definition of the "_create_menu_bar" method which creates the menu bar
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

    # Definition of the "_connect_actions" method which connects the actions to the methods
    def _connect_actions(self):
        self.openAction.triggered.connect(self.openFile)
        self.reglementAction.triggered.connect(self.redirectReglement)
        self.defaultAction.triggered.connect(self.default2022_2023)

    # Definition of the "_add_table_picture" method which adds the table picture to the window
    def _add_table_picture(self, filename='images/table.png'):
        self.table_picture = QLabel(self)
        pixmap = QPixmap(filename)

        self.table_picture.setPixmap(pixmap.scaled(
            pixmap.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        self.table_picture.setScaledContents(True)
        self.table_picture.setFixedWidth(1365)
        self.table_picture.setFixedHeight(910)
        self.table_picture.setStyleSheet('border: 2px solid white;')
        self.table_picture.mouseMoveEvent = self._display_coordinates
        self.table_picture.mousePressEvent = self._display_distance
        self.table_picture.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom | QtCore.Qt.AlignCenter)

        self.layout = QHBoxLayout()
        self.layout.addStretch(1)
        self.layout.addWidget(self.table_picture)
        self.layout.setContentsMargins(0, 0, 1, 0)
        self.layout.setAlignment(Qt.AlignCenter | Qt.AlignRight)

        self.main_layout.addLayout(self.layout)
        self.main_layout.addWidget(self.table_picture, 1)

    # Definition of the "_create_main_layout" method which creates the main layout
    def _create_main_layout(self):
        self.main_layout = QHBoxLayout()
        self.main_layout.setSpacing(0)
        self.main_layout.setAlignment(Qt.AlignCenter)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.central_widget)

    # Definition of the "_create_actions_panel" method which creates the actions panel
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

        self.battery_icon = QLabel(self)
        self.battery_icon.setPixmap(QPixmap('images/battery_icon.png'))
        self.battery_icon.setScaledContents(True)
        self.battery_icon.setMaximumWidth(80)
        self.battery_icon.setMaximumHeight(60)
        self.battery_icon.setAlignment(Qt.AlignCenter)
        self.battery_icon.setStyleSheet(
            'border: 2px solid white; border-radius: 5px;')

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

        self.timer_label = QLabel('Timer', self)
        self.timer_label.setStyleSheet(
            'color: white; font-size: 25px; border: 2px solid white; border-radius: 5px; padding: 5px;')
        self.timer_label.setAlignment(Qt.AlignCenter)

        self.timer_container = QLabel('0', self)
        self.timer_container.setStyleSheet(
            'color: #22427C; font-size: 25px; border-radius: 5px; padding: 5px; background-color: white;')
        self.timer_container.setAlignment(Qt.AlignCenter)

        self.timer_layout = QHBoxLayout()
        self.timer_layout.setAlignment(Qt.AlignCenter)
        self.timer_layout.addWidget(self.timer_label)
        self.timer_layout.addSpacerItem(QSpacerItem(20, 0))
        self.timer_layout.addWidget(self.timer_container)

        self.coordinate_label = QLabel('Coordinates', self)
        self.coordinate_label.setStyleSheet(
            'color: white; font-size: 25px; border: 2px solid white; border-radius: 5px; padding: 5px;')
        self.coordinate_label.setAlignment(Qt.AlignCenter)

        self.coordinate_x_label = QLabel('X', self)
        self.coordinate_x_label.setStyleSheet(
            'color: white; font-size: 25px; border: 2px solid red; border-radius: 5px; padding: 5px;')
        self.coordinate_x_label.setAlignment(Qt.AlignCenter)

        self.coordinate_x_container = QLabel('0', self)
        self.coordinate_x_container.setStyleSheet(
            'color: #22427C; font-size: 25px; border-radius: 5px; padding: 5px; background-color: white;')
        self.coordinate_x_container.setAlignment(Qt.AlignCenter)

        self.coordinate_y_label = QLabel('Y', self)
        self.coordinate_y_label.setStyleSheet(
            'color: white; font-size: 25px; border: 2px solid red; border-radius: 5px; padding: 5px;')
        self.coordinate_y_label.setAlignment(Qt.AlignCenter)

        self.coordinate_y_container = QLabel('0', self)
        self.coordinate_y_container.setStyleSheet(
            'color: #22427C; font-size: 25px; border-radius: 5px; padding: 5px; background-color: white;')
        self.coordinate_y_container.setAlignment(Qt.AlignCenter)

        self.coordinates_separator = QLabel('-', self)
        self.coordinates_separator.setStyleSheet(
            'color: white; font-size: 25px; padding: 5px;')
        self.coordinates_separator.setAlignment(Qt.AlignCenter)

        self.coordinates_layout = QHBoxLayout()
        self.coordinates_layout.setAlignment(Qt.AlignCenter)
        self.coordinates_layout.addWidget(self.coordinate_label)
        self.coordinates_layout.addSpacerItem(QSpacerItem(15, 0))
        self.coordinates_layout.addWidget(self.coordinate_x_label)
        self.coordinates_layout.addSpacerItem(QSpacerItem(15, 0))
        self.coordinates_layout.addWidget(self.coordinate_x_container)
        self.coordinates_layout.addSpacerItem(QSpacerItem(15, 0))
        self.coordinates_layout.addWidget(self.coordinates_separator)
        self.coordinates_layout.addSpacerItem(QSpacerItem(15, 0))
        self.coordinates_layout.addWidget(self.coordinate_y_label)
        self.coordinates_layout.addSpacerItem(QSpacerItem(15, 0))
        self.coordinates_layout.addWidget(self.coordinate_y_container)

        self.distance_label = QLabel('Distance covered', self)
        self.distance_label.setStyleSheet(
            'color: white; font-size: 25px; border: 2px solid white; border-radius: 5px; padding: 5px;')
        self.distance_label.setAlignment(Qt.AlignCenter)

        self.distance_container = QLabel('0', self)
        self.distance_container.setStyleSheet(
            'color: #22427C; font-size: 25px; border-radius: 5px; padding: 5px; background-color: white;')
        self.distance_container.setAlignment(Qt.AlignCenter)

        self.distance_layout = QHBoxLayout()
        self.distance_layout.setAlignment(Qt.AlignCenter)
        self.distance_layout.addWidget(self.distance_label)
        self.distance_layout.addSpacerItem(QSpacerItem(20, 0))
        self.distance_layout.addWidget(self.distance_container)

        self.bot_dvb = QLabel(self)
        self.bot_dvb.setPixmap(QPixmap('images/bot_dvb.svg'))
        self.bot_dvb.setScaledContents(False)
        self.bot_dvb.setAlignment(Qt.AlignCenter)

        self.enemy_bot = QLabel(self)
        self.enemy_bot.setPixmap(QPixmap('images/enemy.svg'))
        self.enemy_bot.setScaledContents(False)
        self.enemy_bot.setAlignment(Qt.AlignCenter)

        self.actions_layout = QVBoxLayout()
        self.actions_layout.setAlignment(Qt.AlignCenter | Qt.AlignTop)

        self.actions_layout.addWidget(self.actions_label)
        self.actions_layout.addSpacerItem(QSpacerItem(0, 20))

        self.actions_layout.addWidget(self.battery_icon)
        self.actions_layout.addSpacerItem(QSpacerItem(0, 30))

        self.actions_layout.addLayout(self.points_layout)
        self.actions_layout.addSpacerItem(QSpacerItem(0, 40))

        self.actions_layout.addLayout(self.timer_layout)
        self.actions_layout.addSpacerItem(QSpacerItem(0, 40))

        self.actions_layout.addLayout(self.coordinates_layout)
        self.actions_layout.addSpacerItem(QSpacerItem(0, 40))

        self.actions_layout.addLayout(self.distance_layout)
        self.actions_layout.addSpacerItem(QSpacerItem(0, 40))

        self.actions_layout.addWidget(self.bot_dvb)
        self.actions_layout.addSpacerItem(QSpacerItem(0, 30))

        self.actions_layout.addWidget(self.enemy_bot)
        self.actions_layout.addSpacerItem(QSpacerItem(0, 40))

        self.actions_layout.addStretch(1)
        self.actions_layout.addSpacerItem(QSpacerItem(410, 0))

        self.line = QFrame()
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setStyleSheet('color: white; border: 2px solid white;')

        self.main_layout.addLayout(self.actions_layout)
        self.main_layout.addSpacerItem(QSpacerItem(50, 0))
        self.main_layout.addWidget(self.line, 1)

    def _display_coordinates(self, event):
        distance_cm_x = round((event.x()/1365)*300)
        distance_cm_y = round((event.y()/910)*200)

        if distance_cm_x < 0 or distance_cm_x > 300 or distance_cm_y < 0 or distance_cm_y > 200:
            self.coordinate_x_container.setText(str(-1))
            self.coordinate_y_container.setText(str(-1))
            return
        self.coordinate_x_container.setText(str(distance_cm_x))
        self.coordinate_y_container.setText(str(distance_cm_y))

    # add a function that displays distance covered in cm in the distance container label when the mouse is pressed on the table picture label and move the mouse on it
    def _display_distance(self, event):
        distance_cm_x = round((event.x()/1365)*300)
        distance_cm_y = round((event.y()/910)*200)

        if distance_cm_x < 0 or distance_cm_x > 300 or distance_cm_y < 0 or distance_cm_y > 200:
            self.distance_container.setText(str(-1))
            return
        self.distance_container.setText(str(distance_cm_x + distance_cm_y))

    def __init__(self):
        super().__init__()
        self.setWindowTitle('CDR')
        self.setWindowIcon(QIcon('images/logo_cdr.png'))
        self.setStyleSheet('background-color: #22427C;')
        self.setMinimumSize(1900, 990)

        self._create_menu_bar()
        self._create_main_layout()
        self._create_actions_panel()
        self._add_table_picture()
        self._connect_actions()

        self.showMaximized()
