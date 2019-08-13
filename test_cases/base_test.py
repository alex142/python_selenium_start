import pytest
import logging


@pytest.mark.usefixtures("driver_init")
class BaseTest:
    pass
