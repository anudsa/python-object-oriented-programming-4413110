# Creating immutable data classes
from dataclasses import dataclass

@dataclass(frozen=True)  # TODO: "The "frozen" parameter makes the class immutable
class ImmutableClass:
    value1: str = "Value 1"
    value2: int = 0


obj = ImmutableClass("xyz",22)
print(obj.value1)
print(obj.value2)
# TODO: attempting to change the value of an immutable class throws an exception
# obj.value1="xyz"
# print(obj.value1)
# TODO: even functions within the class can't change anything
