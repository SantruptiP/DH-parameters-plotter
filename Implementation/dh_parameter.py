from math import radians, sin, cos
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np


class Matrix(object):

    def __init__(self):
        self.matrix = np.identity(4)

    def __getitem__(self, key):
        return self.matrix[key]

    def get(self):
        return self.matrix

    def x_axis(self, rot_about_X):
        # Rotation about x axis
        rot_x = np.identity(4)
        rot_x[1, 1] = cos(radians(rot_about_X))
        rot_x[1, 2] = -(sin(radians(rot_about_X)))
        rot_x[2, 1] = sin(radians(rot_about_X))
        rot_x[2, 2] = cos(radians(rot_about_X))

        self.matrix = np.dot(self.matrix, rot_x)

    def z_axis(self, rot_about_Z):
        # Rotation about z axis

        rot_z = np.identity(4)
        rot_z[0, 0] = cos(radians(rot_about_Z))
        rot_z[0, 1] = -(sin(radians(rot_about_Z)))
        rot_z[1, 0] = sin(radians(rot_about_Z))
        rot_z[1, 1] = cos(radians(rot_about_Z))

        self.matrix = np.dot(self.matrix, rot_z)

    def set_a(self, A):
        # sets the a parameter
        dist_x = np.identity(4)
        dist_x[0, 3] = A
        self.matrix = np.dot(self.matrix, dist_x)
        #self.matrix[0, 3] = a

    def set_alpha(self, alpha):

        # sets the alpha parameter
        self.x_axis(alpha)

    def set_d(self, D):
        # sets the d parameter

        self.matrix[2, 3] = D

    def set_theta(self, theta):
        # sets the theta parameter

        self.z_axis(theta)

    def set_row(self, next_row):
        self.matrix = np.dot(next_row, self.matrix)

L = []
CH = int(input("Choose:\n  1. Read from file\n  2. Enter data Manually"))
if CH == 1:
    F = open("DH_Table.txt", 'r')
    C = int(F.readline())
    for i in range(0, C+1):
        L.insert(i, Matrix())
    for i in range(1, C+1):
        print "Row {0}".format(i)
        q1 = float(F.readline())
        L[i].set_theta(q1)
        D = float(F.readline())
        L[i].set_d(D)
        A = float(F.readline())
        L[i].set_a(A)
        q2 = float(F.readline())
        L[i].set_alpha(q2)
        L[i].set_row(L[i-1].get())
    F.close()

else:
    C = int(input("Enter DOF:"))
    for i in range(0, C+1):
        L.insert(i, Matrix())
    for i in range(1, C+1):
        print "Row {0}".format(i)
        q1 = float(input("\tEnter theta(in degrees): "))
        L[i].set_theta(q1)
        D = float(input("\tEnter d: "))
        L[i].set_d(D)
        A = float(input("\tEnter a: "))
        L[i].set_a(A)
        q2 = float(input("\tEnter alpha(in degrees): "))
        L[i].set_alpha(q2)
        L[i].set_row(L[i-1].get())

# coordinates X Y Z for plotting
X = []
Y = []
Z = []
for i in range(0, C+1):
    A = L[i]
    X.insert(i, A[0, 3])
    Y.insert(i, A[1, 3])
    Z.insert(i, A[2, 3])
print "End effector coordinates are:"
print "x-coordinate: {0}".format(X[C])
print "y-coordinate: {0}".format(Y[C])
print "z-coordinate: {0}".format(Z[C])
# Plot
FIG = plt.figure()
AX = FIG.add_subplot(111, projection='3d')
AX.plot_wireframe(X, Y, Z)
AX.set_xlabel('x')
AX.set_ylabel('y')
AX.set_zlabel('z')
plt.show()

