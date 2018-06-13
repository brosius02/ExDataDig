
print("Hello Deere")
try:
    import numpy
except ImportError:
    print("numpy is not installed")
try:
    import pywin
except ImportError:
    print("pywin is not installed")
try:
    import wx
except ImportError:
    print("wx is not installed")

try:
    import openpyxl
except ImportError:
    print("openpyxl is not installed")