# Classes

<!-- Note: this is pretty much the tutorial from Java 1501. I think it would be fun to split the class into three groups, have them each do a section, and then switch and trace each others' code. -->

## Introduction
In this tutorial we will design, develop, and use custom classes. In small groups, working on paper or the whiteboard, work through the following exercises. You can check your answers using the Python interpreter, but try to solve them by hand first.

## The Circle class
1. Define a new class named `Circle`.
2. Define a **parameterized constructor** (`__init__` method) to initialize a `Circle` with a specified **radius** (a `float`). Your radius should be assigned to an **instance variable**
3. Define and implement a method named `area` that returns the **area** of the circle as a `float`

## The Rectangle class
1. Define a new class named `Rectangle`.
2. Define a **parameterized constructor** (`__init__` method) to initialize a `Rectangle` with a specified **length** and **width** (both `float`). Your parameters should be assigned to **instance variables**
3. Define and implement a method named `area` that returns the **area** of the rectangle as a `float`

## Using classes
Classes are developed so that you can use them to solve a variety of problems.  The major advantage of classes and objects is that they are reusable, that is, once they are developed, they can be used in a number of applications. For this tutorial, assume that the classes `Circle` and `Rectangle` are already defined and have the following methods:

- Constructor: `Circle` takes one `float` parameter, the **radius**, while `Rectangle` takes **length** and **width** (both `float`)
- `area`: Returns the area of the shape as a `float`

1. In a given park, a circular running track is being built. Write a program that will allow the user to enter the **outer** radius of the track and the **inner** radius, then display the total track **area**.

2. You want to create a poster that is rectangular in shape. Write a program that will allow the user to enter the **dimensions of the poster** and the **cost per square foot** for materials and print out the **cost of producing the poster**.

