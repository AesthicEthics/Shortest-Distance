import math
import numpy as np
import matplotlib.pyplot as plt


def distance(point_A):
    #going to pass the vectors as arrays, so need to iterate to find the distance between them 
    #[X1,Y1,Z1]

    point_A = np.array(point_A)

    x1 = float(point_A[0])
    y1 = float(point_A[1])
    z1 = float(point_A[2]) 

    pre_root = (x1)**2 + (y1)**2 + (z1)**2

    distance_from_center = math.sqrt(pre_root)

    return distance_from_center


def cross(vector_1, vector_2):
    #going to passed as an array 

    vector_1 = np.array(vector_1)
    vector_2 = np.array(vector_2)

    x_0 = float(vector_1[0])
    y_0 = float(vector_1[1])
    z_0 = float(vector_1[2])

    x_1 = float(vector_2[0])
    y_1 = float(vector_2[1])
    z_1 = float(vector_2[2])

    nx = (y_0*z_1) - (z_0*y_1)
    ny = (z_0*x_1) - (z_1*x_0)
    nz = (x_0*y_1) - (x_1*y_0)
    
    n = np.array([nx, ny, nz])

    return n




def path_vector(intial, final, r):
    #the intial and final are also going to be parsed as array vectors 
    #After they are checked for distance they are going to need to be defined
    #After this I need to find vectors from the center to each of the points

    if distance(intial) and distance(final) == float(r):
        n_0 = cross(intial, final)
        n_final = cross(n_0, intial)

        return n_final


    else:
        raise ValueError('The Chosen Point Is Not On The Surface Of The Sphere')



vector_path = []
vectors = []
intial = [0,0,16]


vector_path.append(intial)
final = [16,0,0]
r = 16


fig = plt.figure()
ax = plt.axes(projection='3d')



ax.set_xlim([-20,20])
ax.set_ylim([-20,20])
ax.set_zlim([-20,20])

ax.scatter(final[0],final[1],final[2], color="black")

#plotting a sphere:

u = np.linspace(0, 2*np.pi, 50)
v = np.linspace(0, np.pi, 50)

x = r * np.outer(np.cos(u), np.sin(v))
y = r * np.outer(np.sin(u), np.sin(v))
z = r * np.outer(np.ones(np.size(u)), np.cos(v))


for i in range(len(x)):
    value_vec = [x[i][i],y[i][i],z[i][i]]
    vector = path_vector(value_vec, final, r)

    ax.scatter(value_vec[0],value_vec[1],value_vec[2])
    ax.plot_surface(x,y,z, rstride=5, cstride=5)

    ax.quiver(value_vec[0], value_vec[1], value_vec[2], vector[0],vector[1],vector[2], length=7, normalize=True)

plt.show()
