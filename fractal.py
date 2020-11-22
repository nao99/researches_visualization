import graphics

CANVAS_WIDTH = 900
CANVAS_HEIGHT = 900

canvas = graphics.GraphWin('Sierpinski Carpet', CANVAS_WIDTH, CANVAS_HEIGHT)


def drawCarpet(rectangleCoordinateX, rectangleCoordinateY, rectangleWidth, rectangleHeight, step):
    if 0 >= step:
        return

    nextRectangleCoordinateX = rectangleCoordinateX * 2 / 3 + rectangleWidth / 3
    nextRectangleWidth = rectangleCoordinateX / 3 + rectangleWidth * 2 / 3
    nextRectangleCoordinateY = rectangleCoordinateY * 2 / 3 + rectangleHeight / 3
    nextRectangleHeight = rectangleCoordinateY / 3 + rectangleHeight * 2 / 3

    nextStep = step - 1

    rectangleStartPoint = graphics.Point(nextRectangleCoordinateX, nextRectangleCoordinateY)
    rectangleEndPoint = graphics.Point(nextRectangleWidth, nextRectangleHeight)

    rectangle = createRectangle('white', rectangleStartPoint, rectangleEndPoint)
    rectangle.draw(canvas)

    drawCarpet(rectangleCoordinateX, rectangleCoordinateY, nextRectangleCoordinateX, nextRectangleCoordinateY, nextStep)
    drawCarpet(nextRectangleCoordinateX, rectangleCoordinateY, nextRectangleWidth, nextRectangleCoordinateY, nextStep)
    drawCarpet(nextRectangleWidth, rectangleCoordinateY, rectangleWidth, nextRectangleCoordinateY, nextStep)

    drawCarpet(rectangleCoordinateX, nextRectangleCoordinateY, nextRectangleCoordinateX, nextRectangleHeight, nextStep)
    drawCarpet(nextRectangleWidth, nextRectangleCoordinateY, rectangleWidth, nextRectangleHeight, nextStep)

    drawCarpet(rectangleCoordinateX, nextRectangleHeight, nextRectangleCoordinateX, rectangleHeight, nextStep)
    drawCarpet(nextRectangleCoordinateX, nextRectangleHeight, nextRectangleWidth, rectangleHeight, nextStep)
    drawCarpet(nextRectangleWidth, nextRectangleHeight, rectangleWidth, rectangleHeight, nextStep)


def createRectangle(color, startPoint, endPoint):
    rectangle = graphics.Rectangle(startPoint, endPoint)
    rectangle.setFill(color)

    return rectangle


canvasStartingPoint = graphics.Point(0, 0)
canvasEndPoint = graphics.Point(CANVAS_WIDTH, CANVAS_HEIGHT)

# 1. Fill the initial background of the canvas with white
canvasBackground = graphics.Rectangle(canvasStartingPoint, canvasEndPoint)

canvasBackground.setFill('black')
canvasBackground.draw(canvas)

# 2. Define maximum iterations count
iterationsCount = 6

# 3. Draw carpet
drawCarpet(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, iterationsCount)

while True:
    graphics.time.sleep(0.25)

    if canvas.checkMouse():
        break

canvas.close()
