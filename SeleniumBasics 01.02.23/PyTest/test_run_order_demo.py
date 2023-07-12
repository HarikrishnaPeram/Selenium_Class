import pytest

@pytest.mark.run(order=2)
def test_run_order_methodA(OnlineTimeSetup,setUp):
    print("Running Method A")

@pytest.mark.run(order=3)
def test_run_order_methodA(OnlineTimeSetup,setUp):
    print("Running Method B")

@pytest.mark.run(order=3)
def test_run_order_methodA(OnlineTimeSetup,setUp):
    print("Running Method C")

@pytest.mark.run(order=4)
def test_run_order_methodA(OnlineTimeSetup,setUp):
    print("Running Method D")

@pytest.mark.run(order=5)
def test_run_order_methodA(OnlineTimeSetup,setUp):
    print("Running Method E")

@pytest.mark.run(order=6)
def test_run_order_methodA(OnlineTimeSetup,setUp):
    print("Running Method F")



#py.test (filename) --html=myreport/report.html

