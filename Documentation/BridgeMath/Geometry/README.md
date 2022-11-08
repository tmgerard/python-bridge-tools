# Geometry

# Contents
- Two-Dimensional Geometry
  - [Point2D](#point2d)
  - [Vector2D](#vector2d)

# Point2D

The Point2D class defines a two-dimensional cartesian (xy) coordinate point.

## Initializer

The Point2D initializer requires an x and y value to construct the object

### Point2D(x, y)
```python
from BridgeMath import Point2D

point = Point2D(2.0, 1.0)
```
## Methods

### displaced(vector: Vector2D, times)

Returns a Point2D that is the current point displaced by a given Vector2D a specified number of times.

```python
from BridgeMath import Point2D, Vector2D

point = Point2D(2.0, 1.0)
displaced = point.displaced(Vector2D(2.0, 2.0), 1.0) # Point2D with x=4.0 and y=2.0
```

### distance_to(other: Point2D)

Returns the distance to a given Point2D

```python
from BridgeMath import Point2D

point1 = Point2D(2.0, 1.0)
point2 = Point2D(6.0, 10.0)

distance = point1.distance_to(point2)  # 9.84885...
```

## Overloads

### \_\_sub\_\_(other: Point2D)

Subtracts two Point2D objects and returns a Vector2D

```python
from BridgeMath import Point2D

point1 = Point2D(2.0, 1.0)
point2 = Point2D(6.0, 10.0)

vec = point1 - point2  # Vector2D with u=-4.0 and v=-9.0
```

### \_\_eq\_\_(other: Point2D)

Tests for equality between two Point2D objects. True if x and y values are equal. False otherwise.

```python
from BridgeMath import Point2D

point1 = Point2D(2.0, 1.0)
point2 = Point2D(6.0, 10.0)

print(point1 == point2)  # Prints False to console 
```

# Vector2D

## Initializer

The Vector initializer requires u and v component values, representing vector displacement in the x and y directions, to construct the object

### Vector2D(u, v)

```python
from BridgeMath import Vector2D

vector = Vector2D(3.0, 4.0)
```

## Methods

### angle_value_to(other: Vector2D)

Returns the magnitude of the angle between two Vector2D objects (radians)

```python
from BridgeMath import Vector2D

vector1 = Vector2D(3.0, 4.0)
vector2 = Vector2D(10.0, 0.0)

angle_value = vector1.angle_value_to(vector2)  # 0.927295...
```

### angle_to(other: Vector2D)

Returns the angle between two Vector2D objects (radians). A positive value indicated counter-clockwise rotation.

```python
from BridgeMath import Vector2D

vector1 = Vector2D(3.0, 4.0)
vector2 = Vector2D(10.0, 0.0)

angle_value = vector1.angle_to(vector2)  # -0.927295...
```

### cross(other: Vector2D)

Returns the cross product assuming a w (z-axis) component of zero. Useful for determining the angle between two vectors.

```python
from BridgeMath import Vector2D

vector1 = Vector2D(3.0, 4.0)
vector2 = Vector2D(10.0, 0.0)

cross = vector1.cross(vector2)  # -40.0
```

### dot(other: Vector2D)

Returns the dot product of two vectors

```python
from BridgeMath import Vector2D

vector1 = Vector2D(3.0, 4.0)
vector2 = Vector2D(10.0, 0.0)

cross = vector1.dot(vector2)  # 30.0
```

### is_parallel_to(other: Vector2D)

Checks if a given vector is parallel to the current vector

```python
from BridgeMath import Vector2D

vector1 = Vector2D(3.0, 4.0)
vector2 = Vector2D(10.0, 0.0)
vector3 = Vector2D(1.0, 0)

print(vector1.is_parallel_to(vector2))  # Prints False to console
print(vector2.is_parallel_to(vector3))  # Prints True to console
```

### is_perpendicular_to(other: Vector2D)

Checks if a given vector is perpendicular to the current vector

```python
from BridgeMath import Vector2D

vector1 = Vector2D(3.0, 4.0)
vector2 = Vector2D(10.0, 0.0)
vector3 = Vector2D(0.0, 1.0)

print(vector1.is_perpendicular_to(vector2))  # Prints False to console
print(vector2.is_perpendicular_to(vector3))  # Prints True to console
```

### projection_over(direction: Vector2D)

Returns the magnitude of the projection of the vector in the given direction.

```python
from BridgeMath import Vector2D

vector1 = Vector2D(3.0, 4.0)
vector2 = Vector2D(10.0, 0.0)

projection = vector1.projection_over(vector2)  # 3.0
```

### normalized()

Returns a vector of unit length in the direction of the original vector

```python
from BridgeMath import Vector2D

vector1 = Vector2D(3.0, 4.0)
vector2 = Vector2D(10.0, 0.0)

normal_vector1 = vector1.normalized()  # Vector with u=0.6 and v=0.8
normal_vector2 = vector2.normalized()  # Vector with u=1.0 and v=0.0
```

### opposite()

Returns a vector that is in the opposite direction of the original vector

```python
from BridgeMath import Vector2D

vector = Vector2D(3.0, 4.0)

opposite = vector.opposite()  # Vector with u=-3.0 and v=-4.0
```

### with_length()

Returns a vector with the specified length in the direction of the original vector

```python
from BridgeMath import Vector2D

vector = Vector2D(3.0, 4.0)

new_vector = vector.with_length(1.0)  # Vector with u=0.6 and v=0.8
```

### perpendicular

Returns a vector that is perpendicular to the original vector

```python
from BridgeMath import Vector2D

vector = Vector2D(3.0, 4.0)

perpendicular = vector.perpendicular()  # Vector with u=-4.0 and v=3.0
```

## Properties

### cosine

Returns the direction cosine of the vector

```python
from BridgeMath import Vector2D

vector = Vector2D(3.0, 4.0)

cos = vector.cosine  # 0.6
```

### norm

Returns the length of the vector

```python
from BridgeMath import Vector2D

vector = Vector2D(3.0, 4.0)

norm = vector.norm  # 5.0
```

### is_normal

Checks if vector has a unit length. True if norm = 1.0. False otherwise.

```python
from BridgeMath import Vector2D

vector1 = Vector2D(3.0, 4.0)
vector2 = Vector2D(1.0, 0.0)

print(vector1.is_normal)  # Prints False to console
print(vector2.is_normal)  # Prints True to console
```

## Overloads

### \_\_add\_\_(other: Vector2D)

Returns a new vector that is the result of the addition of two vectors

```python
from BridgeMath import Vector2D

vector1 = Vector2D(3.0, 4.0)
vector2 = Vector2D(1.0, 0.0)

new_vector = vector1 + vector2  # Vector with u=13.0 and v=4.0
```

### \_\_sub\_\_(other: Vector2D)

Returns a new vector that is the result of the subtraction of two vectors

```python
from BridgeMath import Vector2D

vector1 = Vector2D(3.0, 4.0)
vector2 = Vector2D(1.0, 0.0)

new_vector = vector1 - vector2  # Vector with u=-7.0 and v=4.0
```

### \_\_eq\_\_(other: Vector2D)

Tests for equality between two Vector2 objects. True if u and v values are equal. False otherwise.

```python
from BridgeMath import Vector2D

vector1 = Vector2D(3.0, 4.0)
vector2 = Vector2D(1.0, 0.0)

print(vector1 == vector2)  # Prints False to console
```