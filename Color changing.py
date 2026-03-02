
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import math


win_width = 512
win_height = 512
x0, y0 = win_width // 2, win_height // 2
radius = 10
out_rad = radius + 80
pulsate = True
var = 1


# Drawing

def dpoint(x, y):

    glBegin(GL_POINTS)

    glVertex2i(x, y)

    glEnd()





def dlines(x0, y0, x1, y1):

    dx = abs(x1 - x0)

    dy = abs(y1 - y0)

    mn = dx - dy
    d = True
    dl = 5
    count = 0


    if  x0 < x1:

        xs = 1

    else:

        -1

    if y0 < y1:

        ys = 1

    else:

        -1


    while True:

        if count == dl:
            d = not d
            count = 0

        # else:
        #     return 

        if x0 == x1 and y0 == y1:
            break

        z2 = 2 * mn

        if z2 < dx:

            mn += dx

            y0 += ys

        if z2 > -dy:

            mn -= dy

            x0 += xs

        if d:

            dpoint(x0, y0)

        count += 1




def display():

    global out_rad

    global var

    glClear(GL_COLOR_BUFFER_BIT)


    # pulsation
    if pulsate is True: 

        out_rad += var

        if out_rad < radius + 10 or out_rad > radius + 80:

            var = - var
    # else:
    #     return 0



    # outer 
    mcl(x0, y0, out_rad)

    #  inner 
    glColor3f(1.0, 1.0, 1.0)

    mcl(x0, y0, radius, inner = True)


    
    glColor3f(1.0, 1.0, 1.0)

    dlines(win_width // 2, 0, win_width // 2, win_height) #vert

    dlines(0, win_height // 2, win_width, win_height // 2) #hori

    glutSwapBuffers()
    glutPostRedisplay()  



def color_quad(x, y):

    if x > win_width // 2 and y > win_height // 2:
        glColor3f(1.0, 1.0, 0.0)  # Yellow

    elif x < win_width // 2 and y > win_height // 2:
        glColor3f(0.0, 1.0, 0.0)  # Green

    elif x < win_width // 2 and y < win_height // 2:
        glColor3f(1.0, 0.0, 0.0)  # Red

    elif x > win_width // 2 and y < win_height // 2:
        glColor3f(0.0, 0.0, 1.0)  # Blue



# Algorithms

def mcl(x0, y0, r, inner=False):

    x = 0
    y = r
    dat = 1 - r

    def wrapped_point(px, py):
       

        wrapped_positions = [(px % win_width, py % win_height),(px % win_width, (py + win_height) % win_height),((px + win_width) % win_width, py % win_height),((px + win_width) % win_width, (py + win_height) % win_height)]

        # for wx, wy in wrapped_positions:
        #     glColor3f(1.0, 1.0, 1.0)  
        #     glBegin(GL_POINTS)
        #     glVertex2i(wx, wy)
        #     glEnd()


        for (wx, wy) in wrapped_positions:
            color_quad(wx, wy)
            dpoint(wx, wy)




    while x <= y:
        p = [ (x + x0, y + y0), (-x + x0, y + y0),(-x + x0, -y + y0),(x + x0, -y + y0),(y + x0, x + y0),(-y + x0, x + y0),(-y + x0, -x + y0),(y + x0, -x + y0)]

        for (px, py) in p:

            if inner:
                dpoint(px % win_width, py % win_height)
               
            else:
                wrapped_point(px, py)
               
        facX = 2 * x
        facY = 2 * y

        func1 = facX + 3
        func2 = facX - facY + 5

        # func1 = ((x) + 13)

        # func2 = ((x) - (2 * y) + 15)

        if dat > 0:
            dat += func2

            x += 1

            y -= 1

            # dat += func1

            # x += 1

        else:
            dat += func1

            x += 1





def mpl(x0, y0, x1, y1):

    dxx = abs(x1 - x0)

    dyy = abs(y1 - y0)

    if x0 < x1:

        xss = 1 

    else:

        -1

    if y0 < y1:

        yss = 1 

    else:

        -1

    sad = dxx - dyy

    # djs = 2 * dy - 2 * dx
    # km = 2 * dy

    while True:

        dpoint(x0, y0)

        if x0 == x1 and y0 == y1:

            break
        # else:
        #     continue 
        f2 = 2 * sad

        if f2 < dxx:
            
            sad += dxx

            y0 += yss

        if f2 > -dyy:

            sad -= dyy

            x0 += xss

        # else:
        #     return 0







# Functionalities

def keyboard(key, x, y):

    global pulsate

    if key == b' ':

        pulsate = not pulsate

    glutPostRedisplay()



def sp_keys(key, x, y):

    global x0
    global y0

    if key == GLUT_KEY_UP:

        y0 += 20

    if key == GLUT_KEY_DOWN:

        y0 -= 20

    if key == GLUT_KEY_LEFT:

        x0 -= 20

    if key == GLUT_KEY_RIGHT:

        x0 += 20



    glutPostRedisplay()



def mouse(b, state, x, y):

    global x0

    global y0

    if b == GLUT_LEFT_BUTTON and state == GLUT_DOWN:

        y0 = win_height - y

        x0 = x

        glutPostRedisplay()


def reshap(w, h):

    glViewport(0, 0, w, h)

    glMatrixMode(GL_PROJECTION)

    glLoadIdentity()

    gluOrtho2D(0, w, 0, h)

    glMatrixMode(GL_MODELVIEW)

def main():

    glutInit(sys.argv)

    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)

    glutInitWindowSize(win_width, win_height)

    glutCreateWindow("Midpoint Circle")

    glClearColor(0.0, 0.0, 0.0, 0.0)

    glPointSize(3.0)

    glutDisplayFunc(display)

    glutReshapeFunc(reshap)

    glutKeyboardFunc(keyboard)

    glutSpecialFunc(sp_keys)

    glutMouseFunc(mouse)

    glutMainLoop()

if __name__ == "__main__":
    main()
