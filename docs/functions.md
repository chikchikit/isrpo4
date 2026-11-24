# Описание функций

## rectangle.py

### `area(a, b)`
Площадь прямоугольника по двум сторонам.

- `a`, `b` - длины сторон
- возвращает `a * b`

```python
import rectangle
rectangle.area(3, 5)    # 15
rectangle.area(10, 0)   # 0
```

### `perimeter(a, b)`
Периметр прямоугольника по двум сторонам.

- `a`, `b` - длины сторон
- возвращает `2 * (a + b)`

```python
rectangle.perimeter(3, 5)    # 16
rectangle.perimeter(10, 10)  # 40
```

## triangle.py

### `area(a, h)`
Площадь треугольника по стороне и высоте, проведённой к ней.

- `a` - длина стороны
- `h` - высота, проведённая к стороне `a`
- возвращает `a * h / 2`

```python
import triangle
triangle.area(6, 4)   # 12.0
triangle.area(3, 5)   # 7.5
```

### `perimeter(a, b, c)`
Периметр треугольника по трём сторонам.

- `a`, `b`, `c` - длины сторон
- возвращает `a + b + c`

```python
triangle.perimeter(3, 4, 5)   # 12
triangle.perimeter(5, 5, 5)   # 15
```