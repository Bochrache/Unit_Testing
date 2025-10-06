import numpy as np
from utils import normalize_vector  # Import our function

def test_normalize_vector_happy_path():
    # 1. Setup
    input_vector = np.array([10, 20, 30])
    expected_output = np.array([-1.22474487, 0.0, 1.22474487])

    # 2. Action
    actual_output = normalize_vector(input_vector)

    # 3. Expectation
    # For floating point numbers, it's better to check for "close enough"
    assert np.allclose(actual_output, expected_output)

def test_normalize_vector_with_nas():
    input_with_na = np.array([10, 20, 30, np.nan])
    expected_output = np.array([-1.22474487, 0.0, 1.22474487, np.nan])

    actual_output = normalize_vector(input_with_na)

    # `np.allclose` doesn't handle NaNs, but `np.testing.assert_allclose` does!
    np.testing.assert_allclose(actual_output, expected_output)