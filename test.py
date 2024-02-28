import sys
from qtpy.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton

class CenteredWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Creamos un layout vertical para el widget
        layout = QVBoxLayout(self)
        
        # Creamos algunos widgets
        label = QLabel("¡Widget centrado en la pantalla!", self)
        button = QPushButton("Botón", self)

        # Agregamos los widgets al layout
        layout.addWidget(label)
        layout.addWidget(button)

        # Configuramos la alineación del layout para que los widgets estén centrados
        layout.setAlignment(label, 0x0082)  # AlignHCenter | AlignVCenter
        layout.setAlignment(button, 0x0082) # AlignHCenter | AlignVCenter

        # Establecemos el layout para el widget principal
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CenteredWidget()
    window.setWindowTitle('Widget centrado')
    window.setGeometry(100, 100, 400, 300) # Establecemos el tamaño del widget
    window.show()
    sys.exit(app.exec_())
    