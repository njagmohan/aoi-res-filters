# Author: Jordan Edmunds, Ph.D. Student, UC Berkeley
# Contact: jordan.e@berkeley.edu
# Creation Date: 11/01/2019
#
from rcwa import Material, Layer, LayerStack, Source, Solver, Plotter
import numpy as np
from matplotlib import pyplot as plt

def solve_system():
    designWavelength = 0.63
    startWavelength = 0.57 #freq
    stopWavelength = 1.70 #freq
    stepWavelength = 0.01 #freq
    
    
    n1 = 2.5 # refractive index of layer 1 (Ti02)
    n2 = 1.5 # refractive index of layer 2 (SiO2)
    ns=n2
    t1 = designWavelength/4/n1
    t2 = designWavelength/4/n2
    t3= designWavelength/2/n1

    reflectionLayer = Layer(n=1)
    transmissionLayer = Layer(n=ns)
    #N=6 DBR STACK
    layer0 = Layer(n=n1, thickness=t1)
    layer1 = Layer(n=n2, thickness=t2)
    layer2 = Layer(n=n1, thickness=t1)
    layer3 = Layer(n=n2, thickness=t2)
    layer4 = Layer(n=n1, thickness=t1)
    layer5 = Layer(n=n2, thickness=t2)
    layer6 = Layer(n=n1, thickness=t1)
    layer7 = Layer(n=n2, thickness=t2)
    layer8 = Layer(n=n1, thickness=t1)
    layer9 = Layer(n=n2, thickness=t2)
    layer10 = Layer(n=n1, thickness=t1)
    layer11 = Layer(n=n2, thickness=t2)
    #CAVITY
    layer12 = Layer(n=n1, thickness=t3)
    #N=6 DBR STACK
    layer13 = Layer(n=n2, thickness=t2)
    layer14 = Layer(n=n1, thickness=t1)
    layer15 = Layer(n=n2, thickness=t2)
    layer16 = Layer(n=n1, thickness=t1)
    layer17 = Layer(n=n2, thickness=t2)
    layer18 = Layer(n=n1, thickness=t1)
    layer19 = Layer(n=n2, thickness=t2)
    layer20 = Layer(n=n1, thickness=t1)
    layer21 = Layer(n=n2, thickness=t2)
    layer22 = Layer(n=n1, thickness=t1)
    layer23 = Layer(n=n2, thickness=t2)
    layer24 = Layer(n=n1, thickness=t1)
    
    
    stack = LayerStack(layer0, layer1, layer2, layer3, layer4, layer5, layer6, layer7, 
                       layer8, layer9, layer10, layer11, layer12, layer13, layer14, layer15, 
                       layer16, layer17, layer18, layer19, layer20, layer21, layer22, layer23, layer24,
                       incident_layer=reflectionLayer, transmission_layer=transmissionLayer)
    source = Source(wavelength=designWavelength, pTEM=[1,0])

    print("\n Solving system...")
    TMMSolver = Solver(stack, source, 1)
    wavelengths = np.arange(startWavelength, stopWavelength + stepWavelength,
            stepWavelength)
    thetas = np.linspace(0,np.pi/1,50)
    
    # results = TMMSolver.solve(wavelength=wavelengths)
    results = TMMSolver.solve(theta=thetas)
    # results = TMMSolver.solve(wavelength=wavelengths)
    return results


if __name__ == '__main__':
    results = solve_system()
    angles, R = results['theta'], results['RTot']
    # wavelengths, R = results['wavelength'], results['RTot']
    plt.plot(angles, R)
    # plt.plot(wavelengths, R)
    # plt.plot(wavelengths, angles, R)
    
    # plt.plot(wavelengths, R, angles, R)

    # plt.plot(results['theta'], results['RTot'])
    # plt.plot(results['theta'], results['TTot'])
    plt.grid()
    # plt.xlim(0,2)
    # plt.ylim(0,1)
    # plt.axvline(np.pi/2)
    plt.show()
    

