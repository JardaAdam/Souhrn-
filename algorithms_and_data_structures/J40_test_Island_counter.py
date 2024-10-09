import pytest


from J40_Island_counter import number_of_islands


def test_number_of_islands():
    # Test case 1: Standard case with multiple islands
    grid1 = [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 1],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1]
    ]
    assert number_of_islands(grid1) == 5, "Test case 1 failed"

    # Test case 2: All water
    grid2 = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    assert number_of_islands(grid2) == 0, "Test case 2 failed"

    # Test case 3: All land
    grid3 = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    assert number_of_islands(grid3) == 1, "Test case 3 failed"

    # Test case 4: Single cell island
    grid4 = [
        [1]
    ]
    assert number_of_islands(grid4) == 1, "Test case 4 failed"

    # Test case 5: No cells (empty grid)
    grid5 = []
    assert number_of_islands(grid5) == 0, "Test case 5 failed"

    # Test case 6: One row with alternating land and water
    grid6 = [
        [1, 0, 1, 0, 1]
    ]
    assert number_of_islands(grid6) == 3, "Test case 6 failed"

    # Test case 7: Large grid with one big island
    grid7 = [
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]
    ]
    assert number_of_islands(grid7) == 1, "Test case 7 failed"

    print("All test cases passed!")


# Run the test function
if __name__ == "__main__":
    pytest.main()
