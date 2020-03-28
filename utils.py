import numpy as np
import pandas as pd
import functools
import operator
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

class SurfaceSmoothnessSuggestor():
    def __init__(self, layer_thickness, raw_value, surface_smoothness):
        self.layer_thickness = layer_thickness
        self.raw_value = raw_value
        self.surface_smoothness = surface_smoothness
        self.data = pd.read_excel('Mean_data.xlsx')
        self.sp_gridsize = [220, 320, 600, 800, 1000, 1200, 1500, 2000]

    def extract(self):
        if self.layer_thickness in [0.1, 0.2, 0.3]:
            extracted_data = self.data[self.data['Layer_thickness'] == self.layer_thickness]
        else:
            return (0, 'Improper Layer Thickness.')
        extracted_data.drop(['Time', 'Layer_thickness', 'Raw_Value'], axis = 1, inplace = True)
        extracted_data = extracted_data.values.tolist()
        extracted_data = functools.reduce(operator.iconcat, extracted_data, [])

        if self.raw_value > self.surface_smoothness:
            result_value = [index for index, value in enumerate(extracted_data) if self.surface_smoothness <= value and self.raw_value > value] 
        else:
            return (0, 'Already smoothened.')
        if result_value:
            result = []
            for index in result_value:
                result.append(self.sp_gridsize[index])
            return self.message(list(map(str, result)))
        else:
            return(0, 'Improper Smoothness Value.')
    
    def message(self, result):
        if len(result) == 0:
            return 'Surface smoothness should not exceed 40 microns.'
        return (len(result)*4, 'You need to smoothen the surface with ' + ', '.join(result) + ' sandpaper.')
    
