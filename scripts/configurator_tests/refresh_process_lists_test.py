# -*- coding: utf-8 -*-
# Copyright 2014 Diamond Light Source Ltd.
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
.. module:: refresh_process_lists_test
   :platform: Unix
   :synopsis: unittest test classes for plugins

.. moduleauthor:: Mark Basham <scientificsoftware@diamond.ac.uk>

"""
import os
import unittest
import savu.test.test_utils as tu
import scripts.config_generator.config_utils as cu
from scripts.config_generator.content import Content


class RefreshProcessListsTest(unittest.TestCase):

    def test_refresh(self):
        cu.populate_plugins()
        path = os.path.dirname(os.path.realpath(__file__)).split('scripts')[0]

        nxs_in_tests, plugins_in_tests = \
            tu.get_process_list(path + '/savu/test/travis')

        lists = tu.get_test_process_list(path + 'test_data/process_lists') \
            + tu.get_test_process_list(path+'test_data/test_process_lists')
        nxs_used = list(set(nxs_in_tests).intersection(set(lists)))

        test_path = path + '/test_data/test_process_lists'
        test_path2 = path + '/test_data/process_lists'
        exclude = ['multimodal/simple_fit_test_XRF.nxs']
        for f in [n for n in nxs_used if n not in exclude]:
            print "Refreshing process list", f, "..."
            if os.path.exists(os.path.join(test_path, f)):
                self._refresh_process_file(os.path.join(test_path, f))
            else:
                self._refresh_process_file(os.path.join(test_path2, f))

    def _refresh_process_file(self, path):
        content = Content()
        # open
        content.fopen(path, update=True)
        # refresh
        positions = content.get_positions()
        for pos_str in positions:
            content.refresh(pos_str)
        # save
        content.save(content.filename)


if __name__ == "__main__":
    unittest.main()
