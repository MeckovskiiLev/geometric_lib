# Math formulas
###
# [Circle:](../circle.py)
## Formula: **S = πR²**

Function ***area*** takes as an argument number **r** and makes multiplication betweer **r**, **r** and number **π**.

>***Example***
> 
> *Input*: **2**
> 
> *Output*: **6.283**

## Formula: **P = 2 * R * π**

Function ***perimetr*** takes as an argument number **r** and makes multiplication between **2, r** and number **π**

>***Example***
> 
> *Input*: **2**
> 
> *Output*: **12.566**

# [Rectangle:](../rectangle.py) 
## Formula: **S = ab**
Function ***area*** takes two numbers as arguments **a**, **b** : (**rectangle's width and length**) and makes ***multiplication*** between them.

>***Example***
> 
> *Input*: **5 6**
> 
> *Output*: **30**
 
## Formula: **S = a * 2 + b * 2**
Function ***perimetr*** takes two numbers as arguments **a**, **b** : (**rectangle's width and length**), makes ***addition*** between doucle **a** and double **b**.

>***Example***
> 
> *Input*: **5 6**
> 
> *Output*: **22**
 
# [Square:](../square.py) 
## Formula: **S = a * a**
Function ***area*** takes number **a** as an argument and returns ***squared number a***.

>***Example***
> 
> *Input*: **5**
> 
> *Output*: **25**


## Formula: **P = 4 * a**
Function ***perimetr*** takes number **a** an an argument and returns ***a multiplied by 4***.

>***Example***
> 
> *Input*: **5**
> 
> *Output*: **20**

# [Triangle:](../triangle.py)
## Formula: **S = (a * h) / 2**

Function ***area*** takes number **a** and **h** as arguments(***size of triangle's side and its height***) and returns ***multiplied a and h devided by 2***.

>***Example***
> 
> *Input*: **4 5**
> 
> *Output*: **10**

## Formula: **P = a + b + c**

Function ***perimetr*** takes numbers **a, b, b** as arguments(***size of a triangle's sizes***) and returns and ***adds*** all the sides.

>***Example***
> 
> *Input*: **4 5 6**
> 
> *Output*: **15**

# [Unittest](../unit_test.py)

## CircleTestCase - test_area

### self.assertAlmostEqual(circle_area(2), math.pi * 2 * 2, places=5)
> Verifies area calculation for a circle with radius 2; expects result close to π*4.

### self.assertAlmostEqual(circle_area(0), 0, places=5)
> Confirms area for circle with radius 0 is 0.

### self.assertAlmostEqual(circle_area(2147483647), math.pi * 2147483647 * 2147483647, places=5)
> Checks area calculation for a circle with a very large radius, `2147483647`.

### self.assertAlmostEqual(circle_area(-8), "Negative number was detected: Circle::area", places=5)
> Verifies handling of negative radius in area calculation. Output is **error**.

---

## CircleTestCase - test_perimeter

### self.assertAlmostEqual(circle_perimeter(2), 2 * math.pi * 2, places=5)
> Tests perimeter for circle with radius 2; expects result close to 4π.

### self.assertAlmostEqual(circle_perimeter(0), 0, places=5)
> Confirms perimeter for circle with radius 0 is 0.

### self.assertAlmostEqual(circle_perimeter(2147483647), 2 * math.pi * 2147483647, places=5)
> Checks perimeter calculation for a circle with a very large radius.

### self.assertAlmostEqual(circle_perimeter(-6), "Negative number was detected: Circle::perimetr", places=5)
> Verifies handling of negative radius in perimeter calculation. Output is **error**.

---

## RectangleTestCase - test_area

### self.assertEqual(rec_area(-5, -6), "Negative number was detected: Rectangle::area")
> Tests rectangle area with negative dimensions. Output is **error**.

### self.assertEqual(rec_area(0, 5), 0)
> Verifies area of rectangle with one side as 0 is 0.

### self.assertEqual(rec_area(7, 2), 14)
> Confirms rectangle area calculation for dimensions 7x2; expects 14.

### self.assertEqual(rec_area(2147483647, 2147483647), 2147483647 * 2147483647)
> Checks area calculation for very large rectangle dimensions. 

---

## RectangleTestCase - test_perimeter

### self.assertEqual(rec_perimeter(-5, -6), "Negative number was detected: Rectangle::perimetr")
> Tests rectangle perimeter with negative dimensions. Output is **error**.

### self.assertEqual(rec_perimeter(0, 5), 10)
> Verifies perimeter calculation with one side as 0; expects 10.

### self.assertEqual(rec_perimeter(7, 2), 18)
> Confirms perimeter calculation for rectangle with dimensions 7x2.

### self.assertEqual(rec_perimeter(2147483647, 2147483647), 2147483647*2 + 2147483647*2)
> Checks perimeter calculation for very large rectangle dimensions.

---

## SquareTestCase - test_area

### self.assertEqual(sq_area(-5), "Negative number was detected: Square::area")
> Tests square area with negative side length. Output is **error**.

### self.assertEqual(sq_area(0), 0)
> Verifies area calculation for square with side length 0.

### self.assertEqual(sq_area(2147483647), 2147483647 * 2147483647)
> Checks area calculation for square with very large side length.

### self.assertEqual(sq_area(10), 100)
> Confirms area calculation for square with side length 10.

---

## SquareTestCase - test_perimeter

### self.assertEqual(sq_perimeter(-5), "Negative number was detected: Square::perimetr")
> Tests square perimeter with negative side length. Output is **error**.

### self.assertEqual(sq_perimeter(0), 0)
> Verifies perimeter calculation for square with side length 0.

### self.assertEqual(sq_perimeter(2147483647), 2147483647 * 4)
> Checks perimeter calculation for square with very large side length.

### self.assertEqual(sq_perimeter(10), 40)
> Confirms perimeter calculation for square with side length 10.

---

## TriangleTestCase - test_area

### self.assertEqual(tri_area(-4, -5), "Negative number was detected: Triangle::area")
> Tests triangle area with negative base and height. Output is **error**.

### self.assertEqual(tri_area(3, 6), 9)
> Verifies area calculation for triangle with base 3 and height 6.

### self.assertEqual(tri_area(2147483647, 2), 2147483647 * 2 / 2)
> Checks area calculation for triangle with very large base.

### self.assertEqual(tri_area(7, 8), 28)
> Confirms area calculation for triangle with base 7 and height 8.

---

## TriangleTestCase - test_perimeter

### self.assertEqual(tri_perimeter(-4, -5, -6), "Negative number was detected: Triangle::perimetr")
> Tests triangle perimeter with negative side lengths. Output is **error**.

### self.assertEqual(tri_perimeter(3, 4, 5), 12)
> Verifies perimeter calculation for triangle with sides 3, 4, 5.

### self.assertEqual(tri_perimeter(6, 8, 10), 24)
> Confirms perimeter calculation for triangle with sides 6, 8, 10.

### self.assertEqual(tri_perimeter(2147483647, 2147483647, 2147483647), 2147483647 + 2147483647 + 2147483647)
> Checks perimeter calculation for triangle with very large side lengths.

# Project history

>[**814279b**](https://github.com/MeckovskiiLev/geometric_lib/commit/814279bce509b35efb766b1689c099c764d4871c) (HEAD -> new_features_405095) Added changed RREADME file
>
>[**bf0f43e**](https://github.com/MeckovskiiLev/geometric_lib/commit/bf0f43e4a708aaa0421d4f05e98ba615fe000a6a) (origin/new_features_405095) Changed formula in rectangle.py
>
>[**4268c8b**](https://github.com/MeckovskiiLev/geometric_lib/commit/4268c8b6718093569694ab4406805f2a5f6cde9f) Added triangle.py    
>
>[**f831743**](https://github.com/MeckovskiiLev/geometric_lib/commit/f8317430564534c93183cf2f25242ed5c93e662d) Added rectangle.py

> [**e92aeb3**]() Added everything about unittest



