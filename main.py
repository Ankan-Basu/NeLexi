from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from PyQt5 import uic
import sys

class MyGUI(QMainWindow):
  def __init__(self):
    super(MyGUI, self).__init__()
    uic.loadUi('untitled.ui', self)
    self.setWindowTitle('NeLexi')
    self.show()

    self.actionNew.triggered.connect(self.new_file)
    self.actionOpen.triggered.connect(self.open_file)
    self.actionSave.triggered.connect(self.save_file)
    self.actionSaveAs.triggered.connect(self.save_file)


    self.fontPicker.activated.connect(self.pressed_font_family)
    self.fontColorPicker.activated.connect(self.pressed_font_color)
    self.fontSizePicker.valueChanged.connect(self.pressed_font_size)

    self.boldToggle.stateChanged.connect(
      lambda: self.show_status('Bold: ' + str(self.boldToggle.isChecked()))
      )
    self.italicToggle.stateChanged.connect(
      lambda: self.show_status('Italic: ' + str(self.italicToggle.isChecked()))
      )


  def new_file(self):
    # To Do. 
    print('New file')
    self.show_status('New File opened')


  def open_file(self):
    options = QFileDialog.Options()
    filename, _ = QFileDialog.getOpenFileName(self, "Open File", "", "nli Files (*.nli)", options=options)

    if filename != '':
      print(filename)
      self.show_status('File opened: ' + filename)


  def save_file(self):
    options = QFileDialog.Options()
    filename, _ = QFileDialog.getSaveFileName(self, "Save File", "", "nli Files (*.nli)", options=options)
    
    if filename != '':
      filename_short = filename.split('/')[-1]

      print(filename_short)
      if len(filename_short) > 4:
        # print(filename_short[-4::])
        if filename_short[-4::] != '.nli':
          filename += '.nli'
      else:
        filename += '.nli'
      
      print(filename)
      self.show_status('File saved: ' + filename)

      with open(filename, 'w') as f:
        pass


  def closeEvent(self, event):
    dialog = QMessageBox()
    dialog.setText('Do you want to save?')
    dialog.addButton(QPushButton('Yes'), QMessageBox.YesRole)
    dialog.addButton(QPushButton('No'), QMessageBox.NoRole)
    dialog.addButton(QPushButton('Cancel'), QMessageBox.RejectRole)

    resp = dialog.exec_()

    if resp == 0:
      self.save_file()
    elif resp == 2:
      event.ignore()


  def pressed_font_family(self):
    print(self.fontPicker.currentText())
    self.show_status(self.fontPicker.currentText())

  def pressed_font_size(self):
    print(self.fontSizePicker.value())
    self.show_status(str(self.fontSizePicker.value()))

  def pressed_font_color(self):
    print(self.fontColorPicker.currentText())
    self.show_status(self.fontColorPicker.currentText())


  def show_status(self, msg):
    self.statusLabel.setText(msg)

    self.modify_status()
    self.statusLabel.adjustSize()


  def modify_status(self):
    font = self.fontPicker.currentText()
    size = self.fontSizePicker.value()
    self.statusLabel.setFont(QFont(font, size))
    color = self.fontColorPicker.currentText()
    isBold = 'bold' if self.boldToggle.isChecked() else 'normal'
    isItalic = 'italic' if self.italicToggle.isChecked() else 'normal'
    self.statusLabel.setStyleSheet(f'color: {color}; font-weight: {isBold}; font-style: {isItalic};')


  def paintEvent(self, event):
    qp = QPainter()
    qp.setBackgroundMode(QBrush(opaqueMode))
    qp.begin(self)
    qp.setPen(QColor(Qt.red))
    qp.setFont(QFont('Arial', 20))
    qp.drawText(10,50, "hello Python")
    qp.setPen(QColor(Qt.blue))
    qp.drawLine(10,100,100,100)
    qp.drawRect(10,150,150,100)
    qp.setPen(QColor(Qt.yellow))
    qp.drawEllipse(100,50,100,50)
    qp.drawPixmap(220,10,QPixmap("pythonlogo.png"))
    qp.fillRect(20,175,130,70,QBrush(Qt.SolidPattern))
    qp.end()



def main():
  print('main')
  app = QApplication(sys.argv)
  window = MyGUI()
  app.exec_()

if __name__ == '__main__':
  main()