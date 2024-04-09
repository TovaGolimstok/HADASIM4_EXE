def option_1_rectangle(rectangle):
    if rectangle.height == rectangle.width or abs(rectangle.height - rectangle.width) > 5:
        print(f"The area of the rectangle is: {rectangle.area()}")
    else:
        print(f"The perimeter of the rectangle is: {rectangle.perimeter()}")