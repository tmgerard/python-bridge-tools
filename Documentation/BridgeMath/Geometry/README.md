# Geometry

# Contents
- Two-Dimensional Geometry
  - [Point2D](#point2d)
  - [Vector2D](#vector2d)
  - [Rectangle2D](#rectangle2d)
  - [Segment2D](#segment2d)
- Three-Dimensional Geometry
  - [Point3D](#point3d)
  - [Vector3D]()
- Factory Methods
  - [make_rectangle2d_containing]()
  - [make_rectangle2D_containing_with_padding]()
  - [make_rectangle_centered]()

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

The Vector2D class represents a two-dimensional vector with u and v components representing displacement in the x and y directions. 

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

Tests for equality between two Vector2D objects. True if u and v values are equal. False otherwise.

```python
from BridgeMath import Vector2D

vector1 = Vector2D(3.0, 4.0)
vector2 = Vector2D(1.0, 0.0)

print(vector1 == vector2)  # Prints False to console
```

# Polygon2D

The Polygon2D class represents a normal polygon shape define with three or more coordinate points. Polygons should not have any crossing sides. There are currently no checks to validate if the polygon meets these criteria.

## Initializer

The polygon initializer requires a list of Point2D objects to construct the Polygon2D object

### Polygon2D(vertices: List\[Point2D\])

```python
from BridgeMath import Polygon2D, Point2D

polygon = Polygon2D(
  [
    Point2D(0.0, 0.0), 
    Point2D(10.0, 0.0), 
    Point2D(12.0, 5.0),  
    Point2D(3.0, 2.0)
  ]
)
```

## Methods

### contains_point(point: Point2D)

Checks if a given point lies within the polygon. True if point is within polygon. False otherwise.

```python
from BridgeMath import Polygon2D, Point2D

polygon = Polygon2D(
  [
    Point2D(0.0, 0.0), 
    Point2D(10.0, 0.0), 
    Point2D(12.0, 5.0),  
    Point2D(3.0, 2.0)
  ]
)

point = Point2D(4.0, 2.0)

print(polygon.contains_point(point))  # True
```

## Properties

### area

Returns the area of the polygon

```python
from BridgeMath import Polygon2D, Point2D

polygon = Polygon2D(
  [
    Point2D(0.0, 0.0), 
    Point2D(10.0, 0.0), 
    Point2D(12.0, 5.0),  
    Point2D(3.0, 2.0)
  ]
)

area = polygon.area  # 29.5
```

### centroid

Returns a Point2D object representing the centroid of the polygon area

```python
from BridgeMath import Polygon2D, Point2D

polygon = Polygon2D(
  [
    Point2D(0.0, 0.0), 
    Point2D(10.0, 0.0), 
    Point2D(12.0, 5.0),  
    Point2D(3.0, 2.0)
  ]
)

centroid = polygon.centroid  # Point2D x=6.25 and y=1.75
```

## Overrides

### \_\_eq\_\_(other)

Checks if a given polygon is equivalent to the current polygon object. True if the vertex list is equivalent for both polygons.

```python
from BridgeMath import Polygon2D, Point2D

polygon1 = Polygon2D(
  [
    Point2D(0.0, 0.0), 
    Point2D(10.0, 0.0), 
    Point2D(12.0, 5.0),  
    Point2D(3.0, 2.0)
  ]
)

polygon2 = Polygon2D(
  [
    Point2D(0.0, 0.0),
    Point2D(5.0, 5.0),
    Point2D(3.0, 10.0)
  ]
)

print(polygon1 == polygon2)  # Prints False to console
```

# Rectangle2D

Represents a rectangle with a given width, height, and origin point. The origin point is a Point2D that identifies the lower left corner of the rectangle.

## Initializer

The Rectangle2D initializer requires a width, height, and Point2D to initialize the object. The origin is an optional parameter and will default to a point with x and y both equal to zero.

### Rectangle2D(width: float, height: float, origin=Point2D(0, 0))

```python
from BridgeMath import Rectangle2D, Point2D

rectangle1 = Rectangle2D(6.0, 2.0, Point2D(1.0, 1.0))  # Defining origin point
rectangle2 = Rectangle2D(6.0, 2.0)  # Default origin x=0.0 and y=0.0
```

## Methods

### contains_point(point: Point2D)

Checks if a given point lies within the rectangle. True if point is within rectangle. False otherwise.

```python
from BridgeMath import Rectangle2D, Point2D

rectangle = Rectangle2D(6.0, 2.0, Point2D(1.0, 1.0))

print(rectangle.contains_point(Point2D(2.0, 2.0)))  # Prints True to console
```

### to_polygon

Returns Polygon2D representing the rectangle

```python
from BridgeMath import Rectangle2D, Point2D

rectangle = Rectangle2D(6.0, 2.0, Point2D(1.0, 1.0))

rect_polygon = rectangle.to_polygon()  # Polygon2D with four vertices
```

## Properties

### area

Returns the area of the rectangle

```python
from BridgeMath import Rectangle2D, Point2D

rectangle = Rectangle2D(6.0, 2.0, Point2D(1.0, 1.0))

area = rectangle.area  # 12.0
```

### bottom

Returns y-coordinate of the rectangles bottom edge

```python
from BridgeMath import Rectangle2D, Point2D

rectangle = Rectangle2D(6.0, 2.0, Point2D(1.0, 1.0))

bottom = rectangle.bottom  # 1.0
```

### diagonal_length

Returns the distance from one bottom corner to the opposing top corner of the rectangle.

```python
from BridgeMath import Rectangle2D, Point2D

rectangle = Rectangle2D(6.0, 2.0, Point2D(1.0, 1.0))

diagonal_length = rectangle.diagonal_length  # 6.32455...
```

### left

Returns x-coordinate of the rectangle's left edge

```python
from BridgeMath import Rectangle2D, Point2D

rectangle = Rectangle2D(6.0, 2.0, Point2D(1.0, 1.0))

left = rectangle.left  # 1.0
```

### perimeter

Returns the perimeter distance of the rectangle

```python
from BridgeMath import Rectangle2D, Point2D

rectangle = Rectangle2D(6.0, 2.0, Point2D(1.0, 1.0))

perimeter = rectangle.perimeter  # 16.0
```

### right

Returns the x-coordinate of the rectangle's right edge

```python
from BridgeMath import Rectangle2D, Point2D

rectangle = Rectangle2D(6.0, 2.0, Point2D(1.0, 1.0))

right = rectangle.right  # 7.0
```

### top

Returns the y-coordinate of the rectangle's top edge

```python
from BridgeMath import Rectangle2D, Point2D

rectangle = Rectangle2D(6.0, 2.0, Point2D(1.0, 1.0))

top = rectangle.top  # 3.0
```

## Overrides

### \_\_eq\_\_(other)

Checks for equality between two Rectangle2D objects. True if origin, width, and height are equal. False otherwise.

```python
from BridgeMath import Rectangle2D, Point2D

rectangle1 = Rectangle2D(6.0, 2.0, Point2D(1.0, 1.0))
rectangle2 = Rectangle2D(6.0, 2.0)

print(rectangle1 == rectangle2)  # False (different origins)
```

# Segment2D

The Segment2D class defines a two-dimensional line segment with defined start and end coordinate points.

## Initializer

The Segment2D initializer takes two Point2D objects that define the start and end of the line segment.

### Segment2D(start: Point2D, end: Point2D)

```python
from BridgeMath import Segment2D, Point2D

segment = Segment2D(Point2D(0.0, 0.0), Point2D(3.0, 4.0))
```

## Methods

### closest_point_to(point: Point2D)

Returns a Point2D on the line segment that corresponds to the closest point in relation to a given Point2D object.

```python
from BridgeMath import Segment2D, Point2D

segment = Segment2D(Point2D(0.0, 0.0), Point2D(3.0, 4.0))

point = segment.closest_point_to(Point2D(1.0, 1.0))  # Point2D x=0.84 and y=1.12
```

### distance_to(point: Point2D)

Returns the distance between a point in space and the closest point on the line segment.

```python
from BridgeMath import Segment2D, Point2D

segment = Segment2D(Point2D(0.0, 0.0), Point2D(3.0, 4.0))

distance = segment.distance_to(Point2D(1.0, 1.0))  # 1.9999...
```

### intersection_with(other: Segment2D)

Returns a Point2D representing the intersection point between a given line segment and the current line segment. Returns ***None*** if no intersection exists.

```python
from BridgeMath import Segment2D, Point2D

segment1 = Segment2D(Point2D(0.0, 0.0), Point2D(3.0, 4.0))
segment2 = Segment2D(Point2D(0.0, 4.0), Point2D(3.0, 0.0))
segment3 = Segment2D(Point2D(0.0, 1.0), Point2D(3.0, 5.0))

point = segment1.intersection_with(segment2)   # Point2D x=1.5 and y=2.0
point2 = segment1.intersection_with(segment3)  # Returns None
```

### point_at(ratio: float)

Returns a Point2D at a location along the line segment. The given location is a ration from 0.0 to 1.0, where 0.0 corresponds to the start of the line segment and 1.0 corresponds to the end of the line segment.

```python
from BridgeMath import Segment2D, Point2D

segment = Segment2D(Point2D(0.0, 0.0), Point2D(3.0, 4.0))

point = segment.point_at(0.5)  # Point2D x=1.5 and y=2.0
```

## Properties

### direction_vector

Returns a vector between the start and end points of the line segment.

```python
from BridgeMath import Segment2D, Point2D

segment = Segment2D(Point2D(0.0, 0.0), Point2D(3.0, 4.0))

vector = segment.direction_vector  # Vector2D u=3.0 and v=4.0
```

### length

Returns the length of the line segment

```python
from BridgeMath import Segment2D, Point2D

segment = Segment2D(Point2D(0.0, 0.0), Point2D(3.0, 4.0))

length = segment.length  # 5.0
```

### normal_unit_vector

Returns a unit length vector that is perpendicular to the line segment.

```python
from BridgeMath import Segment2D, Point2D

segment = Segment2D(Point2D(0.0, 0.0), Point2D(3.0, 4.0))

vector = segment.normal_unit_vector  # Vector2D u=-0.8 and v=0.6
```

### point_at_middle

Returns a Point2D that corresponds to the mid-point of the line segment.

```python
from BridgeMath import Segment2D, Point2D

segment = Segment2D(Point2D(0.0, 0.0), Point2D(3.0, 4.0))

point = segment.point_at_middle  # Point2D x=1.5 and y=2.0
```

### unit_direction_vector

Returns a unit length vector that is directed from the start of the line segment to the end of the line segment.

```python
from BridgeMath import Segment2D, Point2D

segment = Segment2D(Point2D(0.0, 0.0), Point2D(3.0, 4.0))

vector = segment.unit_direction_vector  # Vector2D u=-0.6 and v=0.8
```

## Overrides

### \_\_eq\_\_(other)

Checks if a given Segment2D is equivalent to the current Segment2D. Returns True if the start and end points are equal. False otherwise.

```python
from BridgeMath import Segment2D, Point2D

segment1 = Segment2D(Point2D(0.0, 0.0), Point2D(3.0, 4.0))
segment2 = Segment2D(Point2D(0.0, 4.0), Point2D(3.0, 0.0))

print(segment1 == segment2)  # Prints False to console
```

# Point3D

The Point3D class defines a three-dimensional cartesian (xyz) coordinate point.

## Initializer

The Point3D initializer requires an x, y, and z value to construct the object

### Point2D(x, y, z)
```python
from BridgeMath import Point3D

point = Point3D(2.0, 1.0, 4.0)
```
## Methods

### displaced(vector: Vector3D, times)

Returns a Point3D that is the current point displaced by a given Vector3D a specified number of times.

```python
from BridgeMath import Point3D, Vector3D

point = Point3D(2.0, 1.0, 4.0)
displaced = point.displaced(Vector3D(2.0, 2.0, 2.0), 1.0) # Point2D with x=4.0, y=3.0, and z=6.0
```

### distance_to(other: Point3D)

Returns the distance to a given Point3D

```python
from BridgeMath import Point3D

point1 = Point3D(2.0, 1.0, 4.0)
point2 = Point3D(6.0, 10.0, 0.0)

distance = point1.distance_to(point2)  # 10.6301...
```

## Overloads

### \_\_sub\_\_(other: Point3D)

Subtracts two Point3D objects and returns a Vector3D

```python
from BridgeMath import Point3D

point1 = Point3D(2.0, 1.0, 4.0)
point2 = Point3D(6.0, 10.0, 0.0)

vec = point2 - point1  # Vector3D with u=4.0, v=9.0, and w=-4.0
```

### \_\_eq\_\_(other: Point3D)

Tests for equality between two Point3D objects. True if x, y, and z values are equal. False otherwise.

```python
from BridgeMath import Point3D

point1 = Point3D(2.0, 1.0, 4.0)
point2 = Point3D(6.0, 10.0, 0.0)

print(point1 == point2)  # Prints False to console 
```