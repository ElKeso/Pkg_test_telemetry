import sys
import rospy
from geometry_msgs.msg import Pose
from PySide2.QtWidgets import QApplication, QMainWindow
from ui_Interfaz_Drone4 import Ui_MainWindow  # Importa la clase generada desde tu archivo Python

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Configura la interfaz de usuario según lo generado por Qt Designer
        #rospy.init_node('robot_position_listener')
        #rospy.Subscriber("Drone/pose", Pose, self.telemetria)

    
    def telemetria(self, data):
        x = data.orientation.x
        y = data.orientation.y
        z = data.orientation.z
        w = data.orientation.w
        self.lcd_longitud_drone.display(x)
        self.lcd_latitud_drone.display(y)
        self.lcd_altura_drone.display(z)
        self.lcd_rotacion_drone.display(w)
    
    #def mover_drone(self): #mover el drone por boton de coordenadas
        #
    #def inicio(self): #iniciar vuelo
        
    #def retornar(self): #aterrizar Drone
    
    #def video(self): #mostrar registros video
        
    #def alarma(self): #mostrar registro alarmas alarmas

    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())