from __future__ import annotations
import math
from typing import Union


class Vector:
    def __init__(self, x: Union[int, float], y: Union[int, float]) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x=self.x + other.x,
            y=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x=self.x - other.x,
            y=self.y - other.y
        )

    def __mul__(self,
                other: Union[int, float, Vector]
                ) -> Union[int, float, Vector]:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

        return Vector(
            x=round(self.x * other, 2),
            y=round(self.y * other, 2)
        )

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple
                                    ) -> Vector:
        return cls(
            x=end_point[0] - start_point[0],
            y=end_point[1] - start_point[1]
        )

    def get_length(self) -> Union[int, float]:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        vector_len = self.get_length()
        return Vector(
            x=self.x / vector_len,
            y=self.y / vector_len
        )

    def angle_between(self, other: Vector) -> float:
        cos_a = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> float:
        axis_y = Vector(0, 1)
        cos_a = (self * axis_y) / (self.get_length() * axis_y.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees: int) -> Vector:
        cos_rad_angle = math.cos(math.radians(degrees))
        sin_rad_angle = math.sin(math.radians(degrees))
        return Vector(
            x=self.x * cos_rad_angle - self.y * sin_rad_angle,
            y=self.x * sin_rad_angle + self.y * cos_rad_angle
        )
