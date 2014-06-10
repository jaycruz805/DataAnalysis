DataAnalysis
============

These programs analyze data using mathematical models and produces useful data/results. 

Instructions: Download Files and Run files individually using any Python IDE or Command Line Interpreter.

**Interpolation.py:**
                    Data: To represent data points create a matrix where the 
                          first row represents your x-points and your second row
                          represents your y points.
                          EX: data = [ [1.0,2,3], [4,5.5,6.3] ]
                    
      Interpolating Methods: All methods return a interpolating function 
                             in array format. Which can be used to evaluate any 
                             point. In spline the case of spline methods, 
                             the methods will return a matrix where each row 
                             represents a linear equation based on interval. 
                                                      
                            Langrange:  LMethod(data)
                            Hermite:    HMethod(data)
                            Linear Spline: LSMethod(data)
                            Cubic Spline: CSMethod(data)

             Other Methods: showMatrix(mat)   #shows any matrix
                            printPoly(Poly)   #prints polynomial in regular form
                            evalPoly(Poly, x) #evaluates a Polynomial in array 
                                               format with point x
              Example Code:
                            data = [[1.1,2.2,3.3],[4.4,5.5,6.6]]
                            lp = LMethod(data)
                            print "\nLangrange P(x) = "
                            printPoly(lp)
                            print("P(0.58) = %f \n"% (evalPoly(lp,7.0/12)))
                            ...
                            cs = CSMethod(data)
                            print(evalPoly(S[0], 5.35)

**plotInterp.py:**
               This file depends on interpolation.py and uses its methods to 
               graph interpolating polynomials. interpolation.py must be in the 
               same file directory as this file. 
               
               Data: To represent data points create a matrix where the 
                          first row represents your x-points and your second row
                          represents your y points.
                          EX: data = [ [1.0,2,3], [4,5.5,6.3] ]

               Method:  All methods, besides plot All must be followed by a
                        'restConfig' function in order to display graphs. If you 
                        need to graph more than one method you can call multiple
                        'show..' functions and then a restConfig().
                        
                        Plot Data using:
                            Langrange Meethod: showLan(data)
                            Hermite Method: showHerm(data)
                            Linear Spline Method: showLinSpline(data)
                            Cubic Spline Method: showCubicSpline(data)
                            Display: restConfig()
                        
                            plotAll(data)       #plots and displays all methods

Enjoy!
