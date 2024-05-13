import numpy as np
import matplotlib.pyplot as plt
import os

from utils import mean

cblue = "#2980B9"
cgreen = "#17A589"
cred = "#E74C3C"
cgray = "#808080"

DPI = 800

def f(x, y):
    return np.sqrt(x ** 2 + y ** 2)

u, v = np.mgrid[0:2*np.pi:100j, 0:np.pi:100j]
x = np.cos(u)*np.sin(v)
y = np.sin(u)*np.sin(v)

def plot_cone30():
    fig = plt.figure(figsize=(8, 4), dpi=DPI)
    ax = plt.axes(projection='3d')
    ax.plot_surface(x, y, 4*f(x, y), alpha=0.2)

    ax1, ay1, az1  = np.array([[-2.4,0,0],[0,-2.4,0],[0,0,-0.8]])
    ax2, ay2, az2 = np.array([[4.8,0,0],[0,4.8,0],[0,0,4.8]])
    ax.quiver(ax1, ay1, az1, ax2, ay2, az2, arrow_length_ratio=0.06, color="black", linewidth=0.6)
    ax.text(0,-0.05,4.04, "$x_1$", fontsize=4)

    ax.view_init(azim=36, elev=10)
    ax.set_xlim((-4,4))
    ax.set_ylim((-4,4))
    ax.set_zlim((-4,4))
    ax.set_axis_off()
    plt.savefig("fig/cone30.pdf")

def plot_cone60():
    fig = plt.figure(figsize=(8, 4), dpi=DPI)
    ax = plt.axes(projection='3d')
    ax.plot_surface(x, y, 0.9*f(x, y), alpha=0.2)

    ax1, ay1, az1 = np.array([[-0.6,0,0],[0,-0.6,0],[0,0,-0.2]])
    ax2, ay2, az2 = np.array([[1.2,0,0],[0,1.2,0],[0,0,1.2]])
    ax.quiver(ax1, ay1, az1, ax2, ay2, az2, arrow_length_ratio=0.06, color="black", linewidth=0.6)
    ax.text(0,-0.025,1.02, "$x_1$", fontsize=4)

    ax.view_init(azim=36, elev=10)
    ax.set_xlim((-1,1))
    ax.set_ylim((-1,1))
    ax.set_zlim((-1,1))
    ax.set_axis_off()
    plt.savefig("fig/cone60.pdf")


def plot_cone30_min_A():
    vec1 = np.array([1.7,0.3,-0.1])
    vec2 = np.array([1.7,0,0.56])
    m = mean(vec1, vec2, np.pi/6)
    test = m.A - m.min

    fig = plt.figure(figsize=(8, 4), dpi=DPI)
    ax = plt.axes(projection='3d')
    ax.plot_surface(x, y, 2*f(x, y), alpha=0.08)

    ax1, ay1, az1 = np.array([[-1.2,0,0],[0,-1.2,0],[0,0,-0.4]])
    ax2, ay2, az2= np.array([[2.4,0,0],[0,2.4,0],[0,0,2.4]])
    ax.quiver(ax1, ay1, az1, ax2, ay2, az2, arrow_length_ratio=0.06, color="black", linewidth=0.6)
    ax.text(0,-0.05,2.04, "$x_1$", fontsize=4)

    ax.scatter(vec1[1], vec1[2], vec1[0], s=1, c=cgray)
    ax.scatter(vec2[1], vec2[2], vec2[0], s=1, c=cgray)
    ax.text(vec1[1], vec1[2]-0.08, vec1[0]+0.08, "$x$", fontsize=4, c=cgray)
    ax.text(vec2[1], vec2[2]+0.06, vec2[0]+0.08, "$y$", fontsize=4, c=cgray)

    ax.scatter(m.A[1], m.A[2], m.A[0], s=1, c=cblue)
    ax.scatter(m.min[1], m.min[2], m.min[0], s=1, c=cgreen)
    ax.scatter(test[1], test[2], test[0], s=1, c=cred)
    ax.text(m.A[1], m.A[2]-0.08, m.A[0]+0.08, "$A(x,y)$", fontsize=4, c=cblue)
    ax.text(m.min[1], m.min[2]-0.2, m.min[0]-0.2, "$x∧y$", fontsize=4, c=cgreen)
    ax.text(test[1], test[2]+0.08, test[0], "$A-x∧y$", fontsize=4, c=cred)

    ax.view_init(azim=36, elev=10)
    ax.set_xlim((-2,2))
    ax.set_ylim((-2,2))
    ax.set_zlim((-2,2))
    ax.set_axis_off()
    plt.savefig("fig/cone30_min_A.pdf")

def plot_cone30_H_A():
    vec1 = np.array([1.7,0.3,-0.1])
    vec2 = np.array([1.7,0,0.56])
    m = mean(vec1, vec2, np.pi/6)
    test = m.A - m.H

    fig = plt.figure(figsize=(8, 4), dpi=DPI)
    ax = plt.axes(projection='3d')
    ax.plot_surface(x, y, 2*f(x, y), alpha=0.08)

    ax1, ay1, az1 = np.array([[-1.2,0,0],[0,-1.2,0],[0,0,-0.4]])
    ax2, ay2, az2= np.array([[2.4,0,0],[0,2.4,0],[0,0,2.4]])
    ax.quiver(ax1, ay1, az1, ax2, ay2, az2, arrow_length_ratio=0.06, color="black", linewidth=0.6)
    ax.text(0,-0.05,2.04, "$x_1$", fontsize=4)

    ax.scatter(vec1[1], vec1[2], vec1[0], s=1, c=cgray)
    ax.scatter(vec2[1], vec2[2], vec2[0], s=1, c=cgray)
    ax.text(vec1[1], vec1[2]-0.08, vec1[0]+0.08, "$x$", fontsize=4, c=cgray)
    ax.text(vec2[1], vec2[2]+0.06, vec2[0]+0.08, "$y$", fontsize=4, c=cgray)


    ax.scatter(m.A[1], m.A[2], m.A[0], s=1, c=cblue)
    ax.scatter(m.H[1], m.H[2], m.H[0], s=1, c=cgreen)
    ax.scatter(test[1], test[2], test[0], s=1, c=cred)
    ax.text(m.A[1], m.A[2]-0.08, m.A[0]+0.08, "$A(x,y)$", fontsize=4, c=cblue)
    ax.text(m.H[1], m.H[2]-0.18, m.H[0]-0.24, "$H(x,y)$", fontsize=4, c=cgreen)
    ax.text(test[1], test[2]-0.46, test[0], "$A-H$", fontsize=4, c=cred)

    ax.view_init(azim=36, elev=10)
    ax.set_xlim((-2,2))
    ax.set_ylim((-2,2))
    ax.set_zlim((-2,2))
    ax.set_axis_off()
    plt.savefig("fig/cone30_H_A.pdf")

def plot_cone30_A_max():
    vec1 = np.array([1.7,0.3,-0.1])
    vec2 = np.array([1.7,0,0.56])
    m = mean(vec1, vec2, np.pi/6)
    test = m.max - m.A

    fig = plt.figure(figsize=(8, 4), dpi=DPI)
    ax = plt.axes(projection='3d')
    ax.plot_surface(x, y, 2*f(x, y), alpha=0.08)

    ax1, ay1, az1 = np.array([[-1.2,0,0],[0,-1.2,0],[0,0,-0.4]])
    ax2, ay2, az2= np.array([[2.4,0,0],[0,2.4,0],[0,0,2.4]])
    ax.quiver(ax1, ay1, az1, ax2, ay2, az2, arrow_length_ratio=0.06, color="black", linewidth=0.6)
    ax.text(0,-0.05,2.04, "$x_1$", fontsize=4)

    ax.scatter(vec1[1], vec1[2], vec1[0], s=1, c=cgray)
    ax.scatter(vec2[1], vec2[2], vec2[0], s=1, c=cgray)
    ax.text(vec1[1], vec1[2]-0.08, vec1[0]+0.08, "$x$", fontsize=4, c=cgray)
    ax.text(vec2[1], vec2[2]+0.06, vec2[0]+0.08, "$y$", fontsize=4, c=cgray)

    ax.scatter(m.A[1], m.A[2], m.A[0], s=1, c=cblue)
    ax.scatter(m.max[1], m.max[2], m.max[0], s=1, c=cgreen)
    ax.scatter(test[1], test[2], test[0], s=1, c=cred)
    ax.text(m.A[1], m.A[2]-0.08, m.A[0]+0.08, "$A(x,y)$", fontsize=4, c=cblue)
    ax.text(m.max[1], m.max[2], m.max[0]+0.08, "$x∨y$", fontsize=4, c=cgreen)
    ax.text(test[1], test[2]+0.08, test[0], "x∨y-$A$", fontsize=4, c=cred)

    ax.view_init(azim=36, elev=10)
    ax.set_xlim((-2,2))
    ax.set_ylim((-2,2))
    ax.set_zlim((-2,2))
    ax.set_axis_off()
    plt.savefig("fig/cone30_A_max.pdf")

def plot_cone60_H_A():
    vec1 = np.array([0.6, 0, 0.4])
    vec2 = np.array([0.6, -0.2, 0.4])
    m = mean(vec1, vec2, np.pi/3)
    test = m.A - m.H

    fig = plt.figure(figsize=(8, 4), dpi=DPI)
    ax = plt.axes(projection='3d')
    ax.plot_surface(x, y, 0.5*f(x, y), alpha=0.08)

    ax1, ay1, az1 = np.array([[0,0,0],[0,-0.6,0],[0,0,-0.2]])
    ax2, ay2, az2 = np.array([[0,0,0],[0,1.2,0],[0,0,1.2]])
    ax.quiver(ax1, ay1, az1, ax2, ay2, az2, arrow_length_ratio=0.06, color="black", linewidth=0.6)
    ax1, ay1, az1 = np.array([[-0.6,0,0],[0,0,0],[0,0,0]])
    ax2, ay2, az2 = np.array([[1.2,0,0],[0,0,0],[0,0,0]])
    ax.quiver(ax1, ay1, az1, ax2, ay2, az2, arrow_length_ratio=0.06, color="black", linewidth=0.6, alpha=0.3)
    ax.text(0,-0.025,1.02, "$x_1$", fontsize=4)

    ax.scatter(vec1[1], vec1[2], vec1[0], s=1, c=cgray)
    ax.scatter(vec2[1], vec2[2], vec2[0], s=1, c=cgray)
    ax.text(vec1[1], vec1[2], vec1[0]+0.04, "$x$", fontsize=4, c=cgray)
    ax.text(vec2[1], vec2[2]+0.02, vec2[0]+0.04, "$y$", fontsize=4, c=cgray)

    ax.scatter(m.A[1], m.A[2], m.A[0], s=1, c=cblue)
    ax.scatter(m.H[1], m.H[2], m.H[0], s=1, c=cgreen)
    ax.scatter(test[1], test[2], test[0], s=1, c=cred)
    ax.text(m.A[1], m.A[2]-0.08, m.A[0]-0.12, "$A(x,y)$", fontsize=4, c=cblue)
    ax.text(m.H[1], m.H[2]-0.08, m.H[0]-0.12, "$H(x,y)$", fontsize=4, c=cgreen)
    ax.text(test[1], test[2], test[0]-0.08, "$A-H$", fontsize=4, c=cred)

    ax.view_init(azim=36, elev=10)
    ax.set_xlim((-1,1))
    ax.set_ylim((-1,1))
    ax.set_zlim((-1,1))
    ax.set_axis_off()
    plt.savefig("fig/cone60_H_A.pdf")

def plot_cone60_H_A_adjust():
    vec1 = np.array([0.6, 0, 0.4])
    vec2 = np.array([0.6, -0.2, 0.4])
    m = mean(vec1, vec2, np.pi/3)
    test = m.A - m.H
    adjust_A = m.A.copy()
    adjust_A[0] = adjust_A[0]*np.tan(np.pi/3)
    adjust = adjust_A - m.H

    fig = plt.figure(figsize=(8, 4), dpi=DPI)
    ax = plt.axes(projection='3d')
    ax.plot_surface(x, y, 0.5*f(x, y), alpha=0.08)

    ax1, ay1, az1 = np.array([[0,0,0],[0,-0.6,0],[0,0,-0.2]])
    ax2, ay2, az2 = np.array([[0,0,0],[0,1.2,0],[0,0,1.2]])
    ax.quiver(ax1, ay1, az1, ax2, ay2, az2, arrow_length_ratio=0.06, color="black", linewidth=0.6)
    ax1, ay1, az1 = np.array([[-0.6,0,0],[0,0,0],[0,0,0]])
    ax2, ay2, az2 = np.array([[1.2,0,0],[0,0,0],[0,0,0]])
    ax.quiver(ax1, ay1, az1, ax2, ay2, az2, arrow_length_ratio=0.06, color="black", linewidth=0.6, alpha=0.3)
    ax.text(0,-0.025,1.02, "$x_1$", fontsize=4)

    ax.scatter(vec1[1], vec1[2], vec1[0], s=1, c=cgray)
    ax.scatter(vec2[1], vec2[2], vec2[0], s=1, c=cgray)
    ax.text(vec1[1], vec1[2], vec1[0]+0.04, "$x$", fontsize=4, c=cgray)
    ax.text(vec2[1], vec2[2]+0.02, vec2[0]+0.04, "$y$", fontsize=4, c=cgray)

    ax.scatter(m.A[1], m.A[2], m.A[0], s=1, c=cblue)
    ax.scatter(m.H[1], m.H[2], m.H[0], s=1, c=cgreen)
    ax.scatter(test[1], test[2], test[0], s=1, c=cred)
    ax.text(m.A[1], m.A[2]-0.08, m.A[0]-0.12, "$A(x,y)$", fontsize=4, c=cblue)
    ax.text(m.H[1], m.H[2]-0.08, m.H[0]-0.12, "$H(x,y)$", fontsize=4, c=cgreen)
    ax.text(test[1], test[2], test[0]-0.08, "$A-H$", fontsize=4, c=cred)

    ax.scatter(adjust_A[1], adjust_A[2], adjust_A[0], s=2, c=cblue, marker="*")
    ax.scatter(adjust[1], adjust[2], adjust[0], s=2, c=cred, marker="*")


    ax.plot([m.A[1], adjust_A[1]], [m.A[2], adjust_A[2]],[m.A[0],adjust_A[0]],'-.', linewidth=0.5, color=cblue)
    ax.plot([test[1], adjust[1]], [test[2], adjust[2]],[test[0],adjust[0]],'-.', linewidth=0.5, color=cred)

    ax.view_init(azim=36, elev=10)
    ax.set_xlim((-1,1))
    ax.set_ylim((-1,1))
    ax.set_zlim((-1,1))
    ax.set_axis_off()
    plt.savefig("fig/cone60_H_A_adjust.pdf")



def main():
    if not os.path.exists("fig"):
        os.makedirs("fig")
    plot_cone30()
    plot_cone60()
    plot_cone30_min_A()
    plot_cone30_H_A()
    plot_cone30_A_max()
    plot_cone60_H_A()
    plot_cone60_H_A_adjust()

if __name__ == '__main__':
    main()  