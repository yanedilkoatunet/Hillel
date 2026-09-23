class Rhombus:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, name, value):
        if name == "side_a" and value <= 0:
            raise ValueError("Side must be greater than 0")

        if name == "angle_a":
            if not 0 < value < 180:
                raise ValueError("Angle must be between 0 and 180")

            object.__setattr__(self, "angle_a", value)
            object.__setattr__(self, "angle_b", 180 - value)
        else:
            object.__setattr__(self, name, value)

rhombus = Rhombus(5, 60)

print(rhombus.side_a)
print(rhombus.angle_a)
print(rhombus.angle_b)