from rcwa import Layer, LayerStack, Source, Solver, Plotter
import numpy as np
from matplotlib import pyplot as plt
from rcwa.shorthand import complexArray

def solve_system():
    designWavelength = 0.63
    startWavelength = 0.5
    stopWavelength = 1.5
    stepWavelength = 0.001
    
    
    n1 = 2.5 # refractive index of layer 1 (Ti02)
    n2 = 1.5 # refractive index of layer 2 (SiO2)
    ns=n2
    t1 = designWavelength/4/n1
    t2 = designWavelength/4/n2

    reflectionLayer = Layer(n=1)
    transmissionLayer = Layer(n=ns)
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
    stack = LayerStack(layer0, layer1, layer2, layer3, layer4, layer5, layer6, layer7, layer8, layer9, layer10,
                       incident_layer=reflectionLayer, transmission_layer=transmissionLayer)
    
    source = Source(wavelength=designWavelength, pTEM = [0, 1])

    print("Solving system...")
    TMMSolver = Solver(stack, source, 1)
    wavelengths = np.arange(startWavelength, stopWavelength + stepWavelength,
            stepWavelength)

    thetas = np.linspace(0,np.pi/3,50)
    
    results = TMMSolver.solve(theta=thetas)
    # results = TMMSolver.solve(wavelength=wavelengths)
    return results


if __name__ == '__main__':
    results = solve_system()
    # angles, wavelengths, R = results['theta'], results['wavelength'], results['RTot']
    # plt.plot(angles, R)
    # plt.show()
    
    # plt.plot(wavelengths, R)
    # plt.show()
    
    # fig, ax = results.plot(x='wavelength', y=['RTot'])
    # plt.show()
    
    fig, ax = results.plot(x='theta', y=['RTot'])
    plt.grid()
    # plt.xlim(0,2)
    # plt.ylim(0,1)
    # plt.axvline(np.pi/2)
    plt.show()
    

