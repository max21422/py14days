import math

from src.stats_utils import mean, median, parse_numbers, stddev_population, summary



def test_parse_numbers_commas_and_spaces():
    nums = parse_numbers("1, 2 3,4")
    assert nums == [1.0, 2.0, 3.0, 4.0]


def test_mean():
    assert mean([1.0, 2.0, 3.0, 4.0]) == 2.5


def test_median_odd():
    assert median([3.0, 1.0, 2.0]) == 2.0


def test_median_even():
    assert median([1.0, 2.0, 3.0, 4.0]) == 2.5


def test_stddev_population():
    # 對 [1,2,3]：平均=2，方差=((1-2)^2+(2-2)^2+(3-2)^2)/3 = 2/3
    assert math.isclose(stddev_population([1.0, 2.0, 3.0]), math.sqrt(2 / 3), rel_tol=1e-9)


def test_summary_keys():
    info = summary([1.0, 2.0, 3.0])
    assert info["count"] == 3
    assert info["min"] == 1.0
    assert info["max"] == 3.0
    assert info["mean"] == 2.0

def test_summary_can_disable_sorted():
    info = summary([3.0, 1.0, 2.0], include_sorted=False)
    assert "sorted" not in info