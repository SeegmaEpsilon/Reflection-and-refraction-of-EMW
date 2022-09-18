import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QSlider, QMainWindow, QVBoxLayout, QApplication
from PyQt5.QtGui import QFont
from OtherWindow import Ui_OtherWindow
from math import radians, pi, asin, sin, cos, degrees, tan, atan
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from Otrajenie_Lucha import refraction_reflection_graph
from coeff_otr_prohojd import plot_graphics_coef
from Amplitudes_graphics import graphs_amplitude, ellipse_lucha
import design

app1 = QApplication(sys.argv)
screen = app1.screens()[0]
dpi = screen.physicalDotsPerInch()
app1.quit()

class MyMplCanavas(FigureCanvasQTAgg):
    def __init__(self, fig, parent=None):
        super(MyMplCanavas, self).__init__(fig)

class EMW_REF_APP(QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        # self.ui = uic.loadUi('main.ui', self)
        self.setupUi(self)
        self.init_UI()
        self.connectUi()
        self.lineEdit_6.setInputMask('99')

    def init_UI(self):
        self.canvas = None
        self.canvas1 = None
        self.canvas2 = None
        self.canvas3 = None
        self.canvas4 = None
        self.canvas5 = None
        self.companovka_for_mpl = QVBoxLayout(self.MplWidget)
        self.companovka_for_mpl_2 = QVBoxLayout(self.MplWidget_2)
        self.companovka_for_mpl_3 = QVBoxLayout(self.MplWidget_3)
        self.companovka_for_mpl_4 = QVBoxLayout(self.MplWidget_4)
        self.companovka_for_mpl_5 = QVBoxLayout(self.MplWidget_5)
        self.companovka_for_mpl_6 = QVBoxLayout(self.MplWidget_6)

        self.horizontalSlider.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider.setTickInterval(10)
        self.prepare_canavas_and_toolbar()
        self.reflection_coefficient()

        fontDPI = QFont()
        if dpi<100:
            font_size = 12
        elif dpi>200:
            font_size = int(dpi / 15)
        else:
            font_size = int(dpi/10)
        fontDPI.setFamily("Microsoft YaHei")
        fontDPI.setPointSize(font_size)
        fontDPI.setWeight(50)
        fontDPI.setKerning(True)
        self.label.setFont(fontDPI)
        self.label_2.setFont(fontDPI)
        self.label_3.setFont(fontDPI)
        self.label_4.setFont(fontDPI)
        self.label_5.setFont(fontDPI)
        self.label_6.setFont(fontDPI)
        self.label_7.setFont(fontDPI)
        self.label_8.setFont(fontDPI)
        self.label_9.setFont(fontDPI)
        self.label_10.setFont(fontDPI)
        self.label_11.setFont(fontDPI)
        self.label_14.setFont(fontDPI)

    def connectUi(self):
        self.pushButton.clicked.connect(self.prepare_canavas_and_toolbar)
        self.pushButton.clicked.connect(self.reflection_coefficient)
        self.horizontalSlider.valueChanged.connect(self.changedValue)
        self.pushButton_2.clicked.connect(self.openWindow)
        self.pushButton_3.clicked.connect(self.reset_nom)

    def reset_nom(self):
        self.lineEdit.setText("1.0")
        self.lineEdit_2.setText("1.5")
        self.lineEdit_3.setText("10")
        self.lineEdit_4.setText("20")
        self.lineEdit_6.setText("45")
        self.horizontalSlider.setProperty("value", 45)


    def changedValue(self):
        size = str(self.horizontalSlider.value())
        self.lineEdit_6.setText(size)

    def openWindow(self):
        global OtherWindow
        OtherWindow = QtWidgets.QMainWindow()
        ui = Ui_OtherWindow()
        ui.setupUi(OtherWindow)
        OtherWindow.show()

    def prepare_canavas_and_toolbar(self):
        n_1 = float(self.lineEdit.text())
        n_2 = float(self.lineEdit_2.text())
        phi = float(self.lineEdit_6.text())
        E_pad_perp = float(self.lineEdit_3.text())
        E_pad_paral = float(self.lineEdit_4.text())
        fig = refraction_reflection_graph(n_1, n_2, phi)
        fig1 = plot_graphics_coef(n_1, n_2)
        fig2, fig3, fig4 = graphs_amplitude(n_1, n_2, E_pad_perp, E_pad_paral)
        fig5 = ellipse_lucha(phi, n_1, n_2, E_pad_perp, E_pad_paral)

        if self.canvas:
            self.companovka_for_mpl.removeWidget(self.toolbar)
            self.companovka_for_mpl.removeWidget(self.canvas)
            self.toolbar.deleteLater()
            self.canvas.deleteLater()
            self.canvas.hide()
            self.toolbar.hide()

        if self.canvas1:
            self.companovka_for_mpl_2.removeWidget(self.toolbar1)
            self.companovka_for_mpl_2.removeWidget(self.canvas1)
            self.toolbar1.deleteLater()
            self.canvas1.deleteLater()
            self.canvas1.hide()
            self.toolbar1.hide()

        if self.canvas2:
            self.companovka_for_mpl_3.removeWidget(self.toolbar2)
            self.companovka_for_mpl_3.removeWidget(self.canvas2)
            self.toolbar2.deleteLater()
            self.canvas2.deleteLater()
            self.canvas2.hide()
            self.toolbar2.hide()

        if self.canvas3:
            self.companovka_for_mpl_4.removeWidget(self.toolbar3)
            self.companovka_for_mpl_4.removeWidget(self.canvas3)
            self.toolbar3.deleteLater()
            self.canvas3.deleteLater()
            self.canvas3.hide()
            self.toolbar3.hide()

        if self.canvas4:
            self.companovka_for_mpl_5.removeWidget(self.toolbar4)
            self.companovka_for_mpl_5.removeWidget(self.canvas4)
            self.toolbar4.deleteLater()
            self.canvas4.deleteLater()
            self.canvas4.hide()
            self.toolbar4.hide()

        if self.canvas5:
            self.companovka_for_mpl_6.removeWidget(self.toolbar5)
            self.companovka_for_mpl_6.removeWidget(self.canvas5)
            self.toolbar5.deleteLater()
            self.canvas5.deleteLater()
            self.canvas5.hide()
            self.toolbar5.hide()

        self.canvas = MyMplCanavas(fig)
        self.companovka_for_mpl.addWidget(self.canvas)
        self.toolbar = NavigationToolbar2QT(self.canvas, self)
        self.companovka_for_mpl.addWidget(self.toolbar)

        self.canvas1 = MyMplCanavas(fig1)
        self.companovka_for_mpl_2.addWidget(self.canvas1)
        self.toolbar1 = NavigationToolbar2QT(self.canvas1, self)
        self.companovka_for_mpl_2.addWidget(self.toolbar1)

        self.canvas2 = MyMplCanavas(fig2)
        self.companovka_for_mpl_3.addWidget(self.canvas2)
        self.toolbar2 = NavigationToolbar2QT(self.canvas2, self)
        self.companovka_for_mpl_3.addWidget(self.toolbar2)

        self.canvas3 = MyMplCanavas(fig3)
        self.companovka_for_mpl_4.addWidget(self.canvas3)
        self.toolbar3 = NavigationToolbar2QT(self.canvas3, self)
        self.companovka_for_mpl_4.addWidget(self.toolbar3)

        self.canvas4 = MyMplCanavas(fig4)
        self.companovka_for_mpl_5.addWidget(self.canvas4)
        self.toolbar4 = NavigationToolbar2QT(self.canvas4, self)
        self.companovka_for_mpl_5.addWidget(self.toolbar4)

        self.canvas5 = MyMplCanavas(fig5)
        self.companovka_for_mpl_6.addWidget(self.canvas5)
        self.toolbar5 = NavigationToolbar2QT(self.canvas5, self)
        self.companovka_for_mpl_6.addWidget(self.toolbar5)

    def reflection_coefficient(self):
        E_pad_perp = float(self.lineEdit_3.text())
        E_pad_paral = float(self.lineEdit_4.text())
        phi_rad = radians(float(self.lineEdit_6.text()))
        n_1 = float(self.lineEdit.text())
        n_2 = float(self.lineEdit_2.text())
        brw_angle = degrees(atan(n_2 / n_1))
        angle_of_full_refraction = 0
        try:
            theta = asin(sin(phi_rad) * n_1 / n_2)
        except ValueError:
            theta = pi/2
        if (phi_rad == 0):
            R_perpendicular = R_parallel = 0.0
            T_perpendicular = T_parallel = 1.0

            E_otr_perp = (n_1 * cos(phi_rad) - n_2 * cos(theta)) / (n_1 * cos(phi_rad) + n_2 * cos(theta)) * E_pad_perp
            E_otr_paral = (n_2 * cos(phi_rad) - n_1 * cos(theta)) / (n_2 * cos(phi_rad) + n_1 * cos(theta)) * E_pad_paral
            E_prelom_perp = 2 * n_1 * cos(phi_rad) / (n_1 * cos(phi_rad) + n_2 * cos(theta)) * E_pad_perp
            E_prelom_paral = 2 * n_1 * cos(phi_rad) / (n_2 * cos(phi_rad) + n_1 * cos(theta)) * E_pad_paral
        elif (theta == pi / 2):
            R_perpendicular = R_parallel = 1.0
            T_perpendicular = T_parallel = 0.0
            E_otr_perp = E_pad_perp
            E_otr_paral = E_pad_paral
            E_prelom_perp = E_prelom_paral = 0
        elif ((n_1 != n_2) and (phi_rad != 0)):
            R_perpendicular = pow((sin(phi_rad - theta) / sin(phi_rad + theta)), 2)
            R_parallel = pow((tan(phi_rad - theta) / tan(phi_rad + theta)), 2)
            T_perpendicular = 1 - pow((sin(phi_rad - theta) / sin(phi_rad + theta)), 2)
            T_parallel = sin(2 * phi_rad) * sin(2 * theta) / pow((sin(phi_rad + theta) * cos(phi_rad - theta)), 2)

            E_otr_perp = (n_1 * cos(phi_rad) - n_2 * cos(theta)) / (n_1 * cos(phi_rad) + n_2 * cos(theta)) * E_pad_perp
            E_otr_paral = (n_2 * cos(phi_rad) - n_1 * cos(theta)) / (n_2 * cos(phi_rad) + n_1 * cos(theta)) * E_pad_paral
            E_prelom_perp = 2*n_1*cos(phi_rad)/(n_1*cos(phi_rad)+n_2*cos(theta))*E_pad_perp
            E_prelom_paral = 2 * n_1 * cos(phi_rad) / (n_2 * cos(phi_rad) + n_1 * cos(theta)) * E_pad_paral
        elif (n_1 == n_2):
            R_perpendicular = R_parallel = 0.0
            T_perpendicular = T_parallel = 1.0
            E_otr_perp = 0
            E_otr_paral = 0
            E_prelom_perp = E_pad_perp
            E_prelom_paral = E_pad_paral
        if (n_1 > n_2):
            angle_of_full_refraction = degrees(asin(n_2/n_1))
        # print('E_pad_perp=', E_pad_perp)
        # print('E_pad_paral=', E_pad_paral)
        # print('----------')
        # print('E_otr_perp=', E_otr_perp)
        # print('E_otr_paral=', E_otr_paral)
        # print('E_prelom_perp=', E_prelom_perp)
        # print('E_prelom_paral=', E_prelom_paral)
        self.lcdNumber.display(round(degrees(theta)))
        self.lcdNumber_3.display(round(E_prelom_paral, 3))
        self.lcdNumber_4.display(round(E_prelom_perp, 3))
        self.lcdNumber_5.display(round(E_otr_perp, 3))
        self.lcdNumber_6.display(round(E_otr_paral, 3))
        self.lcdNumber_7.display(round(R_perpendicular, 3))
        self.lcdNumber_8.display(round(R_parallel,3 ))
        self.lcdNumber_9.display(round(T_perpendicular, 3))
        self.lcdNumber_10.display(round(T_parallel, 3))
        self.lcdNumber_2.display(round(brw_angle))
        self.lcdNumber_11.display(round(angle_of_full_refraction))

app = QtWidgets.QApplication(sys.argv)



mainWindow = EMW_REF_APP()
mainWindow.show()
sys.exit(app.exec_())
