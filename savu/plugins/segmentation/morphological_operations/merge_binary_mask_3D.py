# Copyright 2019 Diamond Light Source Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
.. module:: merge_binary_mask_3D
   :platform: Unix
   :synopsis: module to remove gaps in the provided 3D binary mask by merging the boundaries

.. moduleauthor:: Daniil Kazantsev <scientificsoftware@diamond.ac.uk>
"""

from savu.plugins.plugin import Plugin
#from savu.plugins.driver.cpu_plugin import CpuPlugin
from savu.plugins.driver.multi_threaded_plugin import MultiThreadedPlugin
from savu.plugins.utils import register_plugin

import numpy as np
from larix.methods.segmentation import MASK_MORPH

@register_plugin
class MergeBinaryMask3d(Plugin, MultiThreadedPlugin):
    """
    A plugin to remove gaps in the provided 3D binary mask by merging the boundaries

    :param primeclass: class to start morphological processing from. Default: 0.
    :param correction_window: The size of the correction window. Default: 7.
    :param iterations: The number of iterations for segmentation. Default: 3.
    """

    def __init__(self):
        super(MergeBinaryMask3d, self).__init__("MergeBinaryMask3d")

    def setup(self):
    
        in_dataset, out_dataset = self.get_datasets()
        out_dataset[0].create_dataset(in_dataset[0], dtype=np.uint8)
        in_pData, out_pData = self.get_plugin_datasets()
        in_pData[0].plugin_data_setup('VOLUME_3D', 'single')
        out_pData[0].plugin_data_setup('VOLUME_3D', 'single')
        
    def pre_process(self):
        # extract given parameters
        self.primeclass = self.parameters['primeclass']
        self.CorrectionWindow = self.parameters['correction_window']        
        self.iterationsNumb = self.parameters['iterations']       

    def process_frames(self, data):
        # run class merging here:
        inputdata = data[0].copy(order='C')
        
        pars = {'maskdata' : np.uint8(inputdata),\
        'primeClass': self.primeclass,\
        'CorrectionWindow' : self.CorrectionWindow ,\
        'iterationsNumb' : self.iterationsNumb}               
        
        mask_merged = MASK_MORPH(pars['maskdata'], pars['primeClass'], 
                          pars['CorrectionWindow'], pars['iterationsNumb'])        
        return mask_merged
    
    def nInput_datasets(self):
        return 1
    def nOutput_datasets(self):
        return 1