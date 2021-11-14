from dataclasses import dataclass


@dataclass(frozen=True)
class ImmutableClass:
    value1: str = "Value 1"
    value2: int = 0

    def somefunc(self, newval):
        self.value2 = newval

obj = ImmutableClass()
print(obj.value1)


# obj.value1 = "Another value"
# print(obj.value1)


obj.somefunc(20)
