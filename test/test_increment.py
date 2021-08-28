import pytest
from Program.increment import increment

def test_increment():
    result = increment(5)
    assert result == 6
