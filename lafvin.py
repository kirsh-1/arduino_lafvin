from serial.serialposix import Serial

import time
import asyncio


class ArduinoConnection:

    def __init__(self, device: str = "/dev/ttyUSB0") -> None:
        self._serial = Serial(device, baudrate=9600, timeout=.1)
        time.sleep(2)


class Lafvin(ArduinoConnection):
    def _send_command(self, command) -> str:
        self._serial.write(command.encode())
        response = self.__read_response()
        return response

    def __read_response(self) -> str:
        while True:
            line = self._serial.readline().decode().rstrip()
            if line:
                return line
            time.sleep(0.1)

    def read_distance(self) -> str:
        """Возвращает строку дистанции до объекта в см"""
        return self._send_command("d")

    def move_servo(self, angle: int = 90) -> str:
        """Поворот сервопривода\nЗначения от 0 до 180"""
        return self._send_command("c{}".format(angle))

    def go_forward(self, speed: int = 100) -> str:
        """Устанавливает скорость моторов\nЗначения от 0 до 255"""
        return self._send_command("f{}".format(speed))

    def rotate_right(self, speed: int = 150) -> str:
        """Устанавливает скорость левого мотора\nЗначения от 0 до 255"""
        return self._send_command("r{}".format(speed))

    def rotate_left(self, speed: int = 150) -> str:
        """Устанавливает скорость правого мотора\nЗначения от 0 до 255"""
        return self._send_command("l{}".format(speed))

    def go_backward(self, speed: int = 150) -> str:
        """Устанавливает скорость моторов в реверс\nЗначения от 0 до 255"""
        return self._send_command("b{}".format(speed))

    def stop(self):
        """Останавливает моторы"""
        return self._send_command("s")


class AsyncLafvin(ArduinoConnection):

    async def _send_command(self, command) -> str:
        self._serial.write(command.encode())
        response = await self.__read_response()
        return response

    async def __read_response(self) -> str:
        while True:
            line = self._serial.readline().decode('utf-8').rstrip()
            if line:
                return line
            await asyncio.sleep(0.1)

    async def move_servo(self, angle: int = 90) -> str:
        """Поворот сервопривода\nЗначения от 0 до 180"""
        return await self._send_command("c{}".format(angle))

    async def read_distance(self) -> str:
        """Возвращает строку дистанции до объекта в см"""
        return await self._send_command("d")

    async def go_forward(self, speed: int = 100) -> str:
        """Устанавливает скорость моторов\nЗначения от 0 до 255"""
        return await self._send_command("f{}".format(speed))

    async def go_backward(self, speed: int = 150) -> str:
        """Устанавливает скорость моторов в реверсе\nЗначения от 0 до 255"""
        return await self._send_command("b".format(speed))

    async def rotate_left(self, speed: int = 150) -> str:
        """Устанавливает скорость правого мотора\nЗначения от 0 до 255"""
        return await self._send_command("l{}".format(speed))

    async def rotate_right(self, speed: int = 150) -> str:
        """Устанавливает скорость левого мотора\nЗначения от 0 до 255"""
        return await self._send_command("r{}".format(speed))

    async def stop(self) -> str:
        """Останавливает моторы"""
        return await self._send_command("s")
