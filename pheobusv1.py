from rcwa import Source, Layer, LayerStack, Crystal, Solver, RectangularGrating
import numpy as np
from matplotlib import pyplot as plt
from rcwa.shorthand import complexArray
from scipy import signal



def solve_system():
    
    n_ZnS = 2.24 #nL
    n_Ge = 4.11 #nH

    #stopband arises from refractive index contrast, higher contrast bigger stopband
    #need to work on the "bandgap" analogy
    wavelength = 4.884 #um, design wavlength (center)
    #stopband supposedly 4um to 5.5 um
    startWavelength = 3.00 #um
    stopWavelength = 8.00 #um
    stepWavelength=0.02
     

    n1 = n_ZnS # refractive index of layer 1 
    n2 = n_Ge # refractive index of layer 2 
    ns=n2
    t1 = wavelength/4/n1
    t2 = wavelength/4/n2
    # t3= designWavelength/2/n1
    t3=2 #um, given by phoebus papers
    
    reflection_layer = Layer(n=1)
    transmission_layer = Layer(n=ns) #CHECK VALIDITY
    
    deg = np.pi / 180
    k0 = 2*np.pi/wavelength
    theta = 1 * deg
    phi = 1*deg
    # pTEM = 1/np.sqrt(2)*complexArray([1,1j]) #RCP Pol. 
    pTEM= [1,1]
    
    source = Source(wavelength=wavelength, theta=theta, phi=phi, pTEM=pTEM, layer=reflection_layer)
    
    
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
    #grating layer
    layer14 = Layer(n=n1, thickness=t3)
    #N=6 DBR STACK
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
    layer25 = Layer(n=n2, thickness=t2)
    layer26 = Layer(n=n1, thickness=t1)
    
    #grating layer parameters (defect layer)
    period= 1.436 #um
    thickness= 1 #um, careful with repeated variables
    n= n_Ge
    n_void= n_ZnS
    groove_width= 0.436
    nx= 1500 #What does nx really do? Understand N_harmonics too; What type of polarization? (TE) ; Circ/ Lin/ Elliptical?
    
    grating_layer = RectangularGrating(period=period, thickness=thickness, n=n, n_void=n_void, groove_width= groove_width, nx=nx)
    # print(grating_layer.groove_width)
    
    #defining the layer stack
    layer_stack = LayerStack(layer0, layer1, layer2, layer3, layer4, layer5, layer6, layer7, 
                       layer8, layer9, layer10, layer11, layer12,grating_layer, layer14, layer15, 
                       layer16, layer17, layer18, layer19, layer20, layer21, layer22, layer23, 
                       layer24, layer25, layer26, incident_layer=reflection_layer, 
                       transmission_layer=transmission_layer)
    
    #pass to the solver
    N_harmonics=11
    solver_1d = Solver(layer_stack, source, N_harmonics)
    #wavelength sweep
    wavelengths = np.arange(startWavelength, stopWavelength + stepWavelength,
            stepWavelength)
    
    results = solver_1d.solve(wavelength=wavelengths) #in argument pass variables to be swept (wavelengths, thetas, etc. )
    
    return results

if __name__ == '__main__': #edit this portion to reflect desired simulation
    results = solve_system()
    
    # fig, ax = results.plot(x='wavelength', y=['RTot'])
    fig, ax = results.plot(x='wavelength', y=['TTot'])
    plt.show()