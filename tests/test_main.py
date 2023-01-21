import pytest
import numpy as np
from nestify.nestify import TokenRow
import sys

'''
Pytest:
- prefix your class with 'Test', and functions with 'test' otherwise they will be skipped.
'''

class Test_TokenRow_Class:
    def test_AddChild():
        """
        function tests the add child function
        """
        with pytest.raises(TypeError):
            dummyRoot = TokenRow(-1, "", -1, sys.maxsize)
            dummyRoot.AddChild("test_token")