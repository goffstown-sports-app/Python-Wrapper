import sys

sys.path.append("..")
from ghsapp import ghsApp

def test_calendarEvents():
    result = ghsApp().calendarEvents()
    assert type({}), result
    
def test_fieldInfo():
    result = ghsApp().fieldInfo()
    assert type({}), result
    

def test_footballFieldInfo():
    result = ghsApp().footballFieldInfo()
    assert type({}), result
    

def test_gymInfo():
    result = ghsApp().gymInfo()
    assert type({}), result
    

def test_softballFieldInfo():
    result = ghsApp().softballFieldInfo()
    assert type({}), result
