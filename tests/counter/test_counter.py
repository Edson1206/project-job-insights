from src.pre_built.counter import count_ocurrences


def test_counter():
    javascript = count_ocurrences("data/jobs.csv", "JavaScript")
    python = count_ocurrences("data/jobs.csv", "Python")

    assert javascript == 122
    assert python == 1639
