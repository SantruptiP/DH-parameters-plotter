from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from math import radians, sin, cos

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

        self.matrix = np.dot(self.matrix,rot_z)

    def set_a(self, a):
        # sets the a parameter
        dist_x=np.identity(4)
        dist_x[0,3] = a
        self.matrix = np.dot(self.matrix, dist_x)
        #self.matrix[0, 3] = a

    def set_alpha(self, alpha):

        # sets the alpha parameter
        self.x_axis(alpha)

    def set_d(self, d):
        # sets the d parameter

        self.matrix[2, 3] = d

    def set_theta(self, theta):
        # sets the theta parameter

        self.z_axis(theta)

    def set_row(self, next_row):
        self.matrix = np.dot(next_row, self.matrix)



l=[]
c=int(input("Enter DOF:"))
for i in range(0,c+1):
    l.insert(i,Matrix())
for i in range(1,c+1):
    print("Row {0}".format(i))
    q1=float(input("\tEnter theta(in degrees): "))
    l[i].set_theta(q1)
    d=float(input("\tEnter d: "))
    l[i].set_d(d)
    a=float(input("\tEnter a: "))
    l[i].set_a(a)
    q2=float(input("\tEnter alpha(in degrees): "))
    l[i].set_alpha(q2)
    l[i].set_row(l[i-1].get())

# oordinates X Y Z for plotting
X=[]
Y=[]
Z=[]
for i in range(0,c+1):
    a=l[i]
    X.insert(i,a[0,3])
    Y.insert(i,a[1,3])
    Z.insert(i,a[2,3])
print("End effector coordinates are:")
print("x-coordinate: {0}".format(X[c]))
print("y-coordinate: {0}".format(Y[c]))
print("z-coordinate: {0}".format(Z[c]))
# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(X,Y,Z)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()
