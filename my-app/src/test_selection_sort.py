from selection_sort import selection_sort


def test_empty_list(capsys):
    data = []
    result = selection_sort(data)
    captured = capsys.readouterr().out.strip().splitlines()

    assert result == []
    assert data == []
    assert captured == ["Step 0 (already sorted): []"]


def test_single_element_zero(capsys):
    data = [0]
    result = selection_sort(data)
    captured = capsys.readouterr().out.strip().splitlines()

    assert result == [0]
    assert data == [0]
    assert captured == ["Step 0 (already sorted): [0]"]


def test_single_element_positive(capsys):
    data = [3]
    result = selection_sort(data)
    captured = capsys.readouterr().out.strip().splitlines()

    assert result == [3]
    assert data == [3]
    assert captured == ["Step 0 (already sorted): [3]"]


def test_single_element_negative(capsys):
    data = [-7]
    result = selection_sort(data)
    captured = capsys.readouterr().out.strip().splitlines()

    assert result == [-7]
    assert data == [-7]
    assert captured == ["Step 0 (already sorted): [-7]"]


def test_four_elements_with_zero_and_negative(capsys):
    data = [-4, 0, 1, -9]
    result = selection_sort(data)
    captured = capsys.readouterr().out.strip().splitlines()

    assert result == [-9, -4, 0, 1]
    assert data == [-9, -4, 0, 1]
    assert captured == [
        "Step 1: [-9, 0, 1, -4]",
        "Step 2: [-9, -4, 1, 0]",
        "Step 3: [-9, -4, 0, 1]",
    ]