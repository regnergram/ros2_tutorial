"""
Folgender Code basiert auf die Dokumentation von ROS2 Galactic:
https://docs.ros.org/en/galactic/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Publisher-And-Subscriber.html

"""

import rclpy                        # Fuer ROS2 Knoten immer einzubinden
from rclpy.node import Node

from std_msgs.msg import String     # Hier kann auf weitere (vorgefertigte wie eigene) ROS2-Packages
                                    # zurueckgegriffen werden. Die vorgefertigten Packages befinden sich
                                    # im Pfad /opt/ros/$ROS_DISTRO/lib/python3.8/site-packages/
                                    # Eigene Packages sollten sich im Workspace/src/ Pfad befinden.


class MinimalPublisher(Node):       # Durch die Vererbung von Node wird aus der Klasse ein Knoten

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(String, 'topic', 10)        # Ein neuer Publisher wird erstellt mit dem Message-Typ String, dem Topic-Namen 'topic' und dem Quality of Service 10.
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)   # Durch Setzen des Timers wird die self.timer_callback - Methode periodisch aufgerufen.
        self.i = 0

    def timer_callback(self):                                               # Methode, die zyklisch aufgerufen werden soll.
        msg = String()                                                      
        msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(msg)                                        # Hier wird die vorgefertigte Message gepublished. Es koennen nur Messages mit dem festgelegten Typ veroeffentlicht werden.
        self.get_logger().info('Publishing: "%s"' % msg.data)               # Ein Logger, der nuetzlich zum Debuggen ist und den String auf die Konsole schreibt.
        self.i += 1


def main(args=None):                                                        # Diese Funktion wird entsprechend der setup.py-Parametrierung aufgerufen.
    rclpy.init(args=args)                                                   # Eroefffnet die ROS2-Kommunikation

    minimal_publisher = MinimalPublisher()                                  # erstellt einen neuen Knoten.

    rclpy.spin(minimal_publisher)                                           # erst mit dieser Funktion wird der Knoten auch wirklich gestartet.

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()                                        # fuehrt zu einem sauberen Beenden des Knotens
    rclpy.shutdown()                                                        # Beendet die ROS2-Kommunikation


if __name__ == '__main__':
    main()


## Folgende Zeilen werden automatisch in die Node geschrieben, wenn der Kommandozeilenbefehl
## ros2 pkg create --build-type ament_python --dependencies std_msgs --node-name talker py_pubsub
## ausgefuehrt wird:
# def main():
#     print('Hi from py_pubsub.')


# if __name__ == '__main__':
#     main()
