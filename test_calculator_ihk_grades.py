import pytest

testdata_percentage_calculator__positive_tests = [
    (10, 100, 10),
    (0, 100, 0),
    (0, 6, 0)
]

testdata_percentage_calculator__negative_tests = [
    (-1, 100, "ValueError"),
    (0, 5, "ValueError"),
    (11, 10, "ValueError"),
    ("text", 100, "TypeError"),
    (10, "text", "TypeError")
]

testdata_calc_ihk_grade__positive_tests = [
    (100, "sehr gut"),
    (92, "sehr gut"),
    (91, "gut"),
    (81, "gut"),
    (80, "befriedigend"),
    (67, "befriedigend"),
    (66, "ausreichend"),
    (50, "ausreichend"),
    (49, "mangelhaft"),
    (30, "mangelhaft"),
    (29, "ungenügend"),
    (0, "ungenügend")
]

testdata_calc_ihk_grade__negative_tests = [
    (101, "ValueError"),
    (-1, "ValueError"),
    ("text", "TypeError")
]

@pytest.mark.parametrize("points, max_points, result", testdata_percentage_calculator__positive_tests)
def test_percentage_calculator__positive_tests(points, max_points, result):
    assert percentage_calculator(points, max_points) == result

@pytest.mark.parametrize("points, max_points, result", testdata_percentage_calculator__negative_tests)
def test_percentage_calculator__negative_tests(points, max_points, result):
    assert percentage_calculator(points, max_points) == result

@pytest.mark.parametrize("percentage_value, grade", testdata_calc_ihk_grade__positive_tests)
def test_calc_ihk_grade__positive_tests(percentage_value, grade):
    assert calc_ihk_grade(percentage_value) == grade

@pytest.mark.parametrize("percentage_value, grade", testdata_calc_ihk_grade__negative_tests)
def test_calc_ihk_grade__negative_tests(percentage_value, grade):
    assert calc_ihk_grade(percentage_value) == grade
