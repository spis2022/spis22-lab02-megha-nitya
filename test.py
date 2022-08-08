import pytest
from main import convertWageMtoW

def test_convertWageMtoW_100():
  assert convertWageMtoW(100) == 81.8

def test_convertWageMtoW_76_2():
  assert convertWageMtoW(76.2) == 62.3316

def test_convertWageMtoW0():
  assert convertWageMtoW(0) == 0

def test_convertWageMtoW200():
  assert convertWageMtoW(200) == 163.6

def test_convertWageMtoW3000():
  assert convertWageMtoW(3000) == 2454