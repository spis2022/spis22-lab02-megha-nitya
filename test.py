import pytest
from main import convertWageMtoW

def test_convertWageMtoW_100France():
  assert convertWageMtoW(100, "France") == 88.2

def test_convertWageMtoW_76_2Norway():
  assert convertWageMtoW(76.2, "Norway") == 72.6948

def test_convertWageMtoW0Canada():
  assert convertWageMtoW(0, "Canada") == 0

def test_convertWageMtoW200US():
  assert convertWageMtoW(200, "United States") == 163.6
