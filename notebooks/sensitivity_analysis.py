import numpy as np
import pandas as pd
def sensitivity_matrix(fcff, wacc_values, g_values):

    results = pd.DataFrame(index=wacc_values, columns=g_values)

    for w in wacc_values:
        for g in g_values:

            tv = (fcff[-1]*(1+g))/(w-g)

            pv = sum([fcff[i]/((1+w)**(i+1)) for i in range(len(fcff))])

            value = pv + tv/((1+w)**len(fcff))

            results.loc[w,g] = value

    return results
  fcff = [100,120,140,160,180]

wacc_range = np.arange(0.07,0.12,0.01)
g_range = np.arange(0.01,0.04,0.005)

matrix = sensitivity_matrix(fcff,wacc_range,g_range)

matrix
