from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QTablewidget, Qlistwidget, QlistWidgetItem, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup, QRadioButton, QPushButton, Qlable, QSpinBox)
txt_Question = QLineEdit('')
txt_Answer = QLineEdit('')
txt_wrong1 = QLineEdit("")
txt_wrong2 = QLineEdit("")
txt_wrong3 = QLineEdit("")

layout_form = QFormLayout()

layout_form.addRow('Question:', txt_Question)
layout_form.addRow('Correct answer:',txt_Answer)
layout_form.addRow('Incorrect option #1', txt_wrong1)
layout_form.addRow('Incorrect option #2', txt_wrong2)
layout_form.addRow('Incorrect option #3', txt_wrong3)













































