import sys

import pytest


@pytest.mark.skip
def test_window_1():
    print("Window 1")

@pytest.mark.skip(reason="Not included in this build")
def test_window_2():
    print("window2")


@pytest.mark.skipif(sys.vesrion_info<(3,6), reason="required python 3.60 or higher")
def test_mac_1():
    print("mac1")

#py.test test_demo_skip.py -v -rxs
@pytest.mark.mac
def test_mac_2():
    print("mac2")

#py.test.mark.skip
#py.test.mark.skip(reason="")
#py.test -v -rxs
#py.test test_demo_skip.py -m mac -v
