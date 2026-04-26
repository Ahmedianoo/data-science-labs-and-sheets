# IMPORTANT NOTES
# 1- you are using JS Name Casing (CamelCasing)
# 2- make this code as clean as possible
# 3- apply all the concepts you learned during this lab (Naming, comments,  functions)


class Point:
    def __init__(self, coordX, coordY):
        self.coordX = coordX
        self.coordY = coordY


class Rectangle:
    def __init__(self, topLeft, width, height):
        self.validateDimensions(width, height)
        
        self.topLeft = topLeft
        self.width = width 
        self.height = height  

    def validateDimensions(self, width, height):
        if not height or height <= 0 or not width or width <= 0:
            raise RuntimeError(
                "invalid Width and Height"
            )  

    def calculateArea(self):
        return self.width * self.height

    def calculatePerimeter(self):
        return 2 * self.width + 2 * self.height

    def updateHeight(self, height):
        if height and height > 0:
            self.height = height
        # TODO: handle case of updating the height of square

    def update(self, rectangleSpecs):
        topLeft = rectangleSpecs["topLeft"]
        width = rectangleSpecs["width"]
        height = rectangleSpecs["height"]

        self.validateDimensions(width, height)

        self.topLeft = topLeft
        self.width = width
        self.height = height

    def getHeight(self):
        return self.height
    
    def getWidth(self):
        return self.width

    def printCoordinates(self):
        topRight = self.topLeft.coordX + self.width
        bottomLeft = self.topLeft.coordY + self.height
        print("End Point X-Axis (Top Right): " + str(topRight))
        print("End Point Y-Axis (Bottom Left): " + str(bottomLeft))



def buildRectangle(rectangleSpecs):
    topLeft = Point(rectangleSpecs["coord_x"], rectangleSpecs["coord_y"])
    rect = Rectangle(topLeft, rectangleSpecs["width"], rectangleSpecs["height"])
    rect.printCoordinates()
    return rect


def buildSquare(squareSpecs):
    square = None

    if not squareSpecs["height"] or squareSpecs["height"] <= 0:
        raise RuntimeError(
            "invalid Height"
        )
    
    square = buildRectangle({
            "coord_x": squareSpecs["coord_x"],
            "coord_y": squareSpecs["coord_y"],
            "width": squareSpecs["height"],
            "height": squareSpecs["height"]
        })
    
    squareArea = square.calculateArea()
    squarePerimeter = square.calculatePerimeter()
    print("square Area ", squareArea)
    print("square Perimeter ", squarePerimeter)
    return square

rectDimensions = {
    "width": 2,
    "coord_x": 3,
    "height": 5,
    "coord_y": 4 
}

squareDimensions = {
    "coord_x": 3,
    "height": 5,
    "coord_y": 4 
}

rectangle = buildRectangle(rectDimensions)
square = buildSquare(squareDimensions)

print(square.calculatePerimeter())
square.printCoordinates()

rectangle.updateHeight(3)
