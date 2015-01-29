import sys
from NivelTanque import *

class MiFormulario(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        grview = self.ui.graphicsView
        scene = QtGui.QGraphicsScene()
        pic = QtGui.QPixmap("img_tanque/tanque.jpg")
        scene.addItem(QtGui.QGraphicsPixmapItem(pic.scaled(150, 180)))
        #scene.addRect(0,50,80,100)
        grview.setScene(scene)
        grview.show()

        QtCore.QObject.connect(self.ui.horizontalSlider, QtCore.SIGNAL('valueChanged(int)'), self.mostrarImg)
        #self.mostrarImg()
        #QtCore.QObject.connect(self.ui.lblNumPorc, QtCore.SIGNAL('valueChanged(int)'), self.ui.lblNumPorc.setNum)

    def comprobar(self, x):
        resto = x%3
        if (resto!=0):
            x = x - resto
            return x
        else:
            return x

    def num(self, x):
        return (int(x/3))

    def mostrarImg(self):
        y = self.ui.horizontalSlider.value()
        self.ui.lblNumPorc.setNum(y)
        grview = self.ui.graphicsView
        scene = QtGui.QGraphicsScene()
        result = self.comprobar(y)
        if str(result) == '0':
            result = ''
            pic = QtGui.QPixmap("img_tanque/tanque"+result+".jpg")
        elif result == 3:
            pic = QtGui.QPixmap("img_tanque/tanque1.jpg")
        else:
            result = (result * 27) / 99
            pic = QtGui.QPixmap("img_tanque/tanque"+str(int(result))+".jpg")

        scene.addItem(QtGui.QGraphicsPixmapItem(pic.scaled(150, 180)))
        grview.setScene(scene)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MiFormulario()
    myapp.show()
    sys.exit(app.exec_())