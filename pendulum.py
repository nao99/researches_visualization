import graphics
import math


def getNextPendulumPoint(previousPendulumCoordinates, previousPendulumTopAndBodyAngle):
    nextPendulumCoordinateX = canvasCenterPoint.x + leverLength * math.sin(previousPendulumTopAndBodyAngle)
    nextPendulumCoordinateY = canvasCenterPoint.y + leverLength * math.cos(previousPendulumTopAndBodyAngle)

    nextPendulumPoint = graphics.Point(nextPendulumCoordinateX, nextPendulumCoordinateY)

    distanceBetweenPreviousAndNextPendulumPointsX = nextPendulumPoint.x - previousPendulumCoordinates.x
    distanceBetweenPreviousAndNextPendulumPointsY = nextPendulumPoint.y - previousPendulumCoordinates.y

    return graphics.Point(distanceBetweenPreviousAndNextPendulumPointsX, distanceBetweenPreviousAndNextPendulumPointsY)


def getNextPendulumTopAndBodyAngle(previousPendulumTopAndBodyAngle, bodyAcceleration, gravityForce):
    nextPendulumTopAndBodyAngle = previousPendulumTopAndBodyAngle + bodyAcceleration

    bodyAcceleration += -gravityForce * math.sin(previousPendulumTopAndBodyAngle)
    bodyAcceleration *= 0.99

    return nextPendulumTopAndBodyAngle, bodyAcceleration


CANVAS_WIDTH = 800
CANVAS_HEIGHT = 800

canvas = graphics.GraphWin('Mathematical Pendulum', CANVAS_WIDTH, CANVAS_HEIGHT)

leverLength = 300
gravityForce = 0.01
bodyMass = 10
startPendulumTopAndBodyAngle = 3
startBodyAcceleration = 0

startAcceleration = -gravityForce * math.sin(startPendulumTopAndBodyAngle)

canvasStartingPoint = graphics.Point(0, 0)
canvasCenterPoint = graphics.Point(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2)
canvasEndPoint = graphics.Point(CANVAS_WIDTH, CANVAS_HEIGHT)

canvasCenterPointRadius = 20
pendulumBodyCircleRadius = bodyMass * 5

startPendulumCoordinateX = canvasCenterPoint.x + leverLength * math.sin(startPendulumTopAndBodyAngle)
startPendulumCoordinateY = canvasCenterPoint.y + leverLength * math.cos(startPendulumTopAndBodyAngle)

startPendulumCoordinates = graphics.Point(startPendulumCoordinateX, startPendulumCoordinateY)
startPendulumPoint = graphics.Point(startPendulumCoordinates.x, startPendulumCoordinates.y)

# 1. Fill the initial background of the canvas with white
canvasBackground = graphics.Rectangle(canvasStartingPoint, canvasEndPoint)

canvasBackground.setFill('white')
canvasBackground.draw(canvas)

# 2. Draw a central pendulum circle (pendulum top)
centralPendulumCircle = graphics.Circle(canvasCenterPoint, canvasCenterPointRadius)

centralPendulumCircle.setFill('black')
centralPendulumCircle.draw(canvas)

# 3. Draw a body of pendulum
pendulumBodyCircle = graphics.Circle(startPendulumPoint, pendulumBodyCircleRadius)

pendulumBodyCircle.setFill('grey')
pendulumBodyCircle.draw(canvas)

previousPendulumTopAndBodyAngle = startPendulumTopAndBodyAngle
previousBodyAcceleration = startBodyAcceleration

# 4. The main logic: changing an angel and redrawing it
while True:
    previousPendulumTopAndBodyAngle, previousBodyAcceleration = getNextPendulumTopAndBodyAngle(
        previousPendulumTopAndBodyAngle,
        previousBodyAcceleration,
        gravityForce
    )

    nextPendulumPoint = getNextPendulumPoint(pendulumBodyCircle.getCenter(), previousPendulumTopAndBodyAngle)
    pendulumBodyCircle.move(nextPendulumPoint.x, nextPendulumPoint.y)

    line = graphics.Line(canvasCenterPoint, pendulumBodyCircle.getCenter())
    line.draw(canvas)

    graphics.time.sleep(0.03)
    line.undraw()

    if canvas.checkMouse():
        break

canvas.close()
