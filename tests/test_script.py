
from project.script import printscript, script_generator


def test_printscript():
    assert printscript() == 'script'


def test_script_generator():
    assert ['script', 'script'] == [s for s in script_generator(2)]
