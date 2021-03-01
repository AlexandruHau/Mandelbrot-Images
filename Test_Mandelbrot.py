import numpy as np
import matplotlib.pyplot as plt
from Mandelbrot2 import Mandelbrot2

class Test(object):
    def main(self):

        x_inf = -2.025
        x_sup = 0.6
        y_inf = -1.125
        y_sup = 1.125
        no_points = 400
        N = 255 

        grid = Mandelbrot2(x_inf, x_sup, y_inf, y_sup, no_points)
        final_grid = grid.N_iterations(no_points, N, -1, -0)      
        
        plt.imshow(final_grid, extent = (x_inf, x_sup, y_inf, y_sup), interpolation = 'none', cmap='hot', origin= 'lower')
        plt.title('Mandelbrot Set')
        plt.xlabel('Re(z)')
        plt.ylabel('Im(z)')
        plt.colorbar()
        plt.show()

t = Test()
t.main()