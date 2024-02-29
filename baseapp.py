import sys
import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Pose
from std_msgs.msg import Empty
from std_msgs.msg import Bool
from PySide2.QtWidgets import QApplication, QMainWindow
from ui_Interfaz_Drone_final import Ui_MainWindow  # Importa la clase generada desde tu archivo Python

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Configura la interfaz de usuario según lo generado por Qt Designer
        rospy.init_node('robot_position_listener')
        rospy.Subscriber("/drone/gt_pose", Pose, self.telemetria)
        

        #botones funcionalidades
        self.botton_start_drone.clicked.connect(self.despegar)
        self.botton_stop_drone.clicked.connect(self.aterrizar)
        self.botton_control_drone.clicked.connect(self.mover_drone)
        #self.botton_alarma_nvr.clicked.connect(self.nvr)
        #self.botton_alarma_nvr.clicked.connect(self.alarma)
        
        #botones control manual
        self.arriba.clicked.connect(self.boton_arriba)
        self.abajo.clicked.connect(self.boton_abajo)
        self.izquierda.clicked.connect(self.boton_izquierda)
        self.derecha.clicked.connect(self.boton_derecha)
        self.up.clicked.connect(self.boton_up)
        self.down.clicked.connect(self.boton_down)
        self.diag_upleft.clicked.connect(self.boton_diag_upleft)
        self.diag_upright.clicked.connect(self.boton_diag_upright)
        self.diag_downright.clicked.connect(self.boton_diag_downright)
        self.diag_downleft.clicked.connect(self.boton_diag_downleft)
        self.stop.clicked.connect(self.boton_stop)
        


    def telemetria(self, data): #lectura telemetria
        x = data.position.x
        y = data.position.y
        z = data.position.z
        w = data.orientation.w
        self.lcd_longitud_drone.display(x)
        self.lcd_latitud_drone.display(y)
        self.lcd_altura_drone.display(z)
        self.lcd_rotacion_drone.display(w)
    
    def mover_drone(self): #mover el drone por boton de coordenadas
        rate = rospy.Rate(0.5)
        pub_mover = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        pub_mode_pos = rospy.Publisher("/drone/posctrl", Bool, queue_size=10)
        pub_mode_vel = rospy.Publisher("/drone/vel_mode", Bool, queue_size=10)
        stop = Twist()
        stop.linear.x = 0
        stop.linear.y = 0
        stop.linear.z = 0
        stop.angular.x = 0
        stop.angular.y = 0
        stop.angular.z = 0        
        pub_mover.publish(stop)
        pos_mode = Bool()
        pos_mode.data = True
        pub_mode_pos.publish(pos_mode)
        coor = self.obtener_coord()
        x = int(coor[0])
        y = int(coor[1])
        z = int(coor[2])
        w = int(coor[3])
        mover = Twist()
        mover.linear.x = x
        mover.linear.y = y
        mover.linear.z = z
        pub_mover.publish(mover)
        rate.sleep()
        pub_mode_vel.publish(pos_mode)
        pub_mode_vel.publish(pos_mode)

    def obtener_coord(self):#obtener datos de ventana de texto
        latitud = self.ingreso_latitud.text()
        longitud = self.Ingreso_longitud.text()
        altura = self.ingreso_altura.text()
        angulo = self.ingres_angulo.text()
        return [latitud, longitud, altura, angulo]

    def despegar(self): #despegar Drone
        pub_retorno = rospy.Publisher('/drone/takeoff', Empty, queue_size=10)
        desp = Empty()
        pub_retorno.publish(desp)
        

    def aterrizar(self): #aterrizar Drone
        rate = rospy.Rate(0.5)
        pub_mover = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        pub_mode_pos = rospy.Publisher("/drone/posctrl", Bool, queue_size=10)
        pub_retorno = rospy.Publisher('/drone/land', Empty, queue_size=10)
        stop = Twist()
        stop.linear.x = 0
        stop.linear.y = 0
        stop.linear.z = 0
        stop.angular.x = 0
        stop.angular.y = 0
        stop.angular.z = 0        
        pub_mover.publish(stop)
        pos_mode = Bool()
        pos_mode.data = True
        pub_mode_pos.publish(pos_mode)
        stop.linear.x = 0
        stop.linear.y = 0
        stop.linear.z = 0.1
        pub_mover.publish(stop)
        rate.sleep()
        ret = Empty()
        pub_retorno.publish(ret)

    #funciones control manual
    def boton_arriba(self):
        pub_mover = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        stop = Twist()
        stop.linear.x = 1
        stop.linear.y = 0
        stop.linear.z = 0
        stop.angular.x = 0
        stop.angular.y = 0
        stop.angular.z = 0        
        pub_mover.publish(stop)


    def boton_abajo(self):
        pub_mover = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        stop = Twist()
        stop.linear.x = -1
        stop.linear.y = 0
        stop.linear.z = 0
        stop.angular.x = 0
        stop.angular.y = 0
        stop.angular.z = 0        
        pub_mover.publish(stop)

    def boton_derecha(self):
        pub_mover = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        stop = Twist()
        stop.linear.x = 0
        stop.linear.y = 0
        stop.linear.z = 0
        stop.angular.x = 0
        stop.angular.y = 0
        stop.angular.z = 1        
        pub_mover.publish(stop)

    def boton_izquierda(self):
        pub_mover = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        stop = Twist()
        stop.linear.x = 0
        stop.linear.y = 0
        stop.linear.z = 0
        stop.angular.x = 0
        stop.angular.y = 0
        stop.angular.z = -1        
        pub_mover.publish(stop)

    def boton_diag_upleft(self):
        pub_mover = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        stop = Twist()
        stop.linear.x = 1
        stop.linear.y = 0
        stop.linear.z = 0
        stop.angular.x = 0
        stop.angular.y = 0
        stop.angular.z = -1        
        pub_mover.publish(stop)
    
    def boton_diag_upright(self):
        pub_mover = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        stop = Twist()
        stop.linear.x = 1
        stop.linear.y = 0
        stop.linear.z = 0
        stop.angular.x = 0
        stop.angular.y = 0
        stop.angular.z = 1        
        pub_mover.publish(stop)

    def boton_diag_downleft(self):
        pub_mover = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        stop = Twist()
        stop.linear.x = -1
        stop.linear.y = 0
        stop.linear.z = 0
        stop.angular.x = 0
        stop.angular.y = 0
        stop.angular.z = -1        
        pub_mover.publish(stop)
    
    def boton_diag_downright(self):
        pub_mover = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        stop = Twist()
        stop.linear.x = -1
        stop.linear.y = 0
        stop.linear.z = 0
        stop.angular.x = 0
        stop.angular.y = 0
        stop.angular.z = 1        
        pub_mover.publish(stop)
    
    def boton_stop(self):
        pub_mover = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        stop = Twist()
        stop.linear.x = 0
        stop.linear.y = 0
        stop.linear.z = 0
        stop.angular.x = 0
        stop.angular.y = 0
        stop.angular.z = 0        
        pub_mover.publish(stop) 

    def boton_up(self):
        pub_mover = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        stop = Twist()
        stop.linear.x = 0
        stop.linear.y = 0
        stop.linear.z = 0.1
        stop.angular.x = 0
        stop.angular.y = 0
        stop.angular.z = 0        
        pub_mover.publish(stop) 
    
    def boton_down(self):
        pub_mover = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        stop = Twist()
        stop.linear.x = 0
        stop.linear.y = 0
        stop.linear.z = -0.1
        stop.angular.x = 0
        stop.angular.y = 0
        stop.angular.z = 0        
        pub_mover.publish(stop) 


    #def video(self): #mostrar registros video
        
    #def alarma(self): #mostrar registro alarmas alarmas

    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
