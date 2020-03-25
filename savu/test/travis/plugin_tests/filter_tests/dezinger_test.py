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
.. module:: dezinger_test
   :platform: Unix
   :synopsis: Tests for the dezinger plugin

.. moduleauthor:: Nicola Wadeson <scientificsoftware@diamond.ac.uk>

"""
import unittest
from savu.test import test_utils as tu

from savu.test.travis.framework_tests.plugin_runner_test import \
    run_protected_plugin_runner


def dezinger_has_been_implemented_in_python():
    try:
        from savu.plugins.filters import dezinger  # noqa: F401
        return True
    except ModuleNotFoundError:
        return False


reason = """Dezinger was a C plugin that was removed during the move to Python 3.
There is a task to reimplement it purely in Python, so once that is done this
test doesn't need to be skipped anymore"""


class DezingerTest(unittest.TestCase):

    @unittest.skipUnless(dezinger_has_been_implemented_in_python(), reason)
    def test_dezinger(self):
        data_file = tu.get_test_data_path('24737.nxs')
        process_file = tu.get_test_process_path('dezinger_test.nxs')
        run_protected_plugin_runner(tu.set_options(data_file,
                                                   process_file=process_file))
if __name__ == "__main__":
    unittest.main()
