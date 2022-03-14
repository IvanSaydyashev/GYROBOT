from PyQt5 import uic, QtWidgets
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice

app = QtWidgets.QApplication([])
ui = uic.loadUi("design.ui")
ui.setWindowTitle("SerialGUI")

serial = QSerialPort()
serial.setBaudRate(9600)
portList = []
ports = QSerialPortInfo().availablePorts()
for ports in ports:
    portList.append(ports.portName())
ui.comL.addItems(portList)


def onRead():
    rx = serial.readLine()
    rxs = str(rx, 'utf-8').strip()
    data = rxs.split(',')
    print(data)


def serialSend(data):
    txs = ""
    for val in data:
        txs += str(val)
        txs += ','
    txs = txs[::-1]
    txs += ';'
    serial.write(txs.encode())


def comOpen():
    serial.setPortName(ui.comL.currentText())
    serial.open(QIODevice.ReadWrite)


def comClose():
    serial.close()


def vkp(val):
    serialSend([0, val])


def vki(val):
    serialSend([1, val])


def vkd(val):
    serialSend([2, val])

def bkp(val):
    serialSend([3, val])


def bki(val):
    serialSend([4, val])


def bkd(val):
    serialSend([5, val])


def lkp(val):
    serialSend([6, val])


def lki(val):
    serialSend([7, val])


def lkd(val):
    serialSend([8, val])


def bpoint(val):
    serialSend([9, val])


def velocity(val):
    serialSend([10, val])

try:
    serial.readyRead().connect(onRead)
except:
    pass
ui.openB.clicked.connect(comOpen)
ui.closeB.clicked.connect(comClose)
ui.vkp.valueChanged.connect(vkp)
ui.vki.valueChanged.connect(vki)
ui.vkd.valueChanged.connect(vkd)
ui.bkp.valueChanged.connect(bkp)
ui.bki.valueChanged.connect(bki)
ui.bkd.valueChanged.connect(bkd)
ui.lkp.valueChanged.connect(lkp)
ui.lki.valueChanged.connect(lki)
ui.lkd.valueChanged.connect(lkd)
ui.balance_point.valueChanged.connect(bpoint)
ui.velocity.valueChanged.connect(velocity)
ui.show()
app.exec()
