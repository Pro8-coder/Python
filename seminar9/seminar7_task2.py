class Road:
    _length = 0
    _width = 0

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self):
        return f'{self._width * self._length * 25 * 5 / 1000} т'
