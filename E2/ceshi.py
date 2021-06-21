class Vector:
    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z
    

    def __add__(self, rhs):
        rx = self.__x + rhs.__x
        ry = self.__y + rhs.__y
        rz = self.__z + rhs.__z
        result = Vector(rx, ry, rz)
        return result


    def __sub__(self, rhs):
        rx = self.__x - rhs.__x
        ry = self.__y - rhs.__y
        rz = self.__z - rhs.__z
        result = Vector(rx, ry, rz)
        return result


    def __mul__(self, rhs):
        rx = self.__x * rhs.__x
        ry = self.__y * rhs.__y
        rz = self.__z * rhs.__z
        result = Vector(rx, ry, rz)
        return result


    def __truediv__(self, rhs):
        rx = self.__x / rhs.__x
        ry = self.__y / rhs.__y
        rz = self.__z / rhs.__z
        result = Vector(rx, ry, rz)
        return result


    def show(self):
        print((self.__x, self.__y, self.__z))

if __name__ == '__main__':
    v1 = Vector(1, 1, 1)
    v1.show()
    v2 = Vector(2, 2, 2)
    v2.show()
    v3 = v1 + v2
    v3.show()
    v4 = v1 - v2
    v4.show()
    v5 = v1 * v2
    v5.show()
    v6 = v1 / v2
    v6.show()
    