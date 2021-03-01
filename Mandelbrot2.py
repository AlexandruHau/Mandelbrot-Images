import matplotlib.pyplot as plt 
import numpy as np 
import math 

class Mandelbrot2(object):
    
    no_points = 400

    def __init__ (self, x_inf, x_sup, y_inf, y_sup, no_points):
        xx = np.linspace(x_inf, x_sup, no_points)
        yy = np.linspace(y_inf, y_sup, no_points)
        X,Y = np.meshgrid(xx,yy)
        self.grid = X + 1j*Y

    def N_iterations(self, no_points, N, Re, Im):
        final_grid = np.zeros((no_points, no_points))
        count = 0
        help = self.grid 
        while(count<N):

            help = help**2 + ( Re + 1j*Im )
            for i in range (no_points):
                for j in range (no_points):
                    if(abs(help[i][j]) < 2):
                        final_grid[i][j] += 1
            count += 1

        return final_grid