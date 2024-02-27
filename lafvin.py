import time
from serial.serialposix import Serial


class ArduinoConnection:
    """Стандартный порт /dev/ttyUSB0"""

    def __init__(self, port: str = "/dev/ttyUSB0") -> None:
        self._serial = Serial(port, baudrate=9600, timeout=.1)
        time.sleep(2.1)


class Lafvin(ArduinoConnection):
    def read_distance(self) -> int:
        """
        Считать дистанцию с датчика\n
        Возвращает int дистанции в см
        """
        self._serial.write(b'd')
        time.sleep(.5)
        result = self._serial.readline().decode().rstrip()
        if result
            to_int = int(float(result))
            return result
        else:
            raise Exception('Seriar.readline() is None')

    def move_servo(self, angle: int = 90) -> None:
        """
        Повернуть сервопривод на ? градусов\n
        Принимает значения от 0 до 180
        """
        self._serial.write("c{}".format(angle).encode())
        return

    def go_forward(self, speed: int = 100) -> None:
        """
        Установить скорость моторов на ?\n
        Принимает значения от 0 до 255
        """
        self._serial.write("f{}".format(speed).encode())
        return

    def rotate_left(self, speed: int = 150) -> None:
        """
        Установить скорость правого мотора на ? \n
        Принимает значения от 0 до 255
        """
        self._serial.write("r{}".format(speed).encode())
        return

    def rotate_right(self, speed: int = 150) -> None:
        """
        Установить скорость левого мотора на ? \n
        Принимает значения от 0 до 255
        """
        self._serial.write("l{}".format(speed).encode())
        return

    def go_backward(self, speed: int = 100) -> None:
        """
        Установить скорость моторов на ? в реверс\n
        Принимает значения от 0 до 255
        """
        self._serial.write("b{}".format(speed).encode())
        return

    def stop(self) -> None:
        """Остановить моторы\n"""
        self._serial.write(b's')
        return
