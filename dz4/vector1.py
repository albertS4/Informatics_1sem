class Vector():
    def __init__(self, *args):
        assert len(args) <= 3
        if len(args) == 1:
            if type(args[0]) == float or type(args[0]) == int:
                self.x = args[0]; self.y = 0; self.z = 0
            elif type(args[0]) == str:
                if args[0][0] != "{" or args[0][-1] != "}":
                    raise ValueError("Cannon use a string as a vector")
                else:
                    values = args[0][1:-1].split(",")
                    assert len(values) <= 3
                    values_numeric = []
                    for value in values:
                        value = value.strip()
                        if (value.count(".") == 0 or value.count(".") == 1 and value[0] != "." and value[-1] != ".") and (value.count("-") == 0 or value.count("-") == 1 and value[0] == "-") and value.replace(".", "").replace("-", "").isdecimal():
                            values_numeric.append(float(value))
                        else:
                            raise ValueError("Wrong coordinates")
                    values_numeric = values_numeric + [0]*(3 - len(values_numeric))
                    self.x, self.y, self.z = values_numeric
        elif len(args) > 1:
            for a in args:
                assert type(a) == int or type(a) == float
            self.x, self.y, self.z = list(args) + [0]*(3 - len(args))
    def __abs__(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x+other.x,self.y+other.y,self.z+other.z)
        else:
            raise ValueError("Cannot add to a vector")
    def __radd__(self, other):
            return self + other
    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x*other.x + self.y*other.y + self.z*other.z
        elif isinstance(other, int) or isinstance(other, float):
            return Vector(self.x*other, self.y*other, self.z*other)
        else:
            raise ValueError("Cannot multiply by a vector")
    def __rmul__(self, other):
            return self*other
    def __str__(self):
        return f'x = {self.x} y = {self.y} z = {self.z}'