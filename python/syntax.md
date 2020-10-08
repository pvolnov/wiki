
Спецсимволы
----

1. `s.union(t)` == `s | t` - уникальные символы
2.  `s.update(t)` == `s |= t`

A
===

1. Abstract metod
```python
from abc import ABC, abstractmethod
 
class ChessPiece(ABC):
    # общий метод, который будут использовать все наследники этого класса
    def draw(self):
        print("Drew a chess piece")
 
    # абстрактный метод, который будет необходимо переопределять для каждого подкласса
    @abstractmethod
    def move(self):
        pass

    @abstractproperty
    def val(self):
        pass
```

2. `ascii` - вывести код буквы