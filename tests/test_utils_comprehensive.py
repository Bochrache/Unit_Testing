import numpy as np
import pytest
from utils import normalize_vector


def test_normalize_vector_basic():
    """Test basic functionality of normalize_vector."""
    input_vector = np.array([10, 20, 30])
    expected_output = np.array([-1.22474487, 0.0, 1.22474487])
    
    actual_output = normalize_vector(input_vector)
    
    assert np.allclose(actual_output, expected_output)


def test_normalize_vector_with_nas():
    """Test normalize_vector handles NaN values correctly."""
    input_with_na = np.array([10, 20, 30, np.nan])
    expected_output = np.array([-1.22474487, 0.0, 1.22474487, np.nan])

    actual_output = normalize_vector(input_with_na)

    # `np.allclose` doesn't handle NaNs, but `np.testing.assert_allclose` does!
    np.testing.assert_allclose(actual_output, expected_output)


def test_normalize_vector_single_value():
    """Test normalize_vector with a single value."""
    input_vector = np.array([42])
    
    actual_output = normalize_vector(input_vector)
    
    # Single value should result in NaN when normalized
    assert np.isnan(actual_output[0])


def test_normalize_vector_all_same_values():
    """Test normalize_vector when all values are identical."""
    input_vector = np.array([5, 5, 5, 5])
    
    actual_output = normalize_vector(input_vector)
    
    # All same values should result in NaN when normalized (std dev = 0)
    assert np.all(np.isnan(actual_output))


def test_normalize_vector_negative_values():
    """Test normalize_vector with negative values."""
    input_vector = np.array([-10, 0, 10])
    expected_output = np.array([-1.22474487, 0.0, 1.22474487])
    
    actual_output = normalize_vector(input_vector)
    
    assert np.allclose(actual_output, expected_output)


def test_normalize_vector_empty_array():
    """Test normalize_vector with empty array."""
    input_vector = np.array([])
    
    actual_output = normalize_vector(input_vector)
    
    # Empty array should return empty array
    assert len(actual_output) == 0
    assert actual_output.shape == (0,)


@pytest.mark.parametrize("input_data,expected", [
    (np.array([1, 2, 3]), np.array([-1.22474487, 0.0, 1.22474487])),
    (np.array([0, 0, 0]), np.array([np.nan, np.nan, np.nan])),
    (np.array([100]), np.array([np.nan])),
])
def test_normalize_vector_parametrized(input_data, expected):
    """Parametrized test for multiple input scenarios."""
    actual = normalize_vector(input_data)
    
    if np.any(np.isnan(expected)):
        # Handle NaN comparisons
        assert np.array_equal(np.isnan(actual), np.isnan(expected))
        # Check non-NaN values
        mask = ~np.isnan(expected)
        if np.any(mask):
            assert np.allclose(actual[mask], expected[mask])
    else:
        assert np.allclose(actual, expected)


class TestNormalizeVectorClass:
    """Class-based tests for normalize_vector function."""
    
    def test_normalize_preserves_shape(self):
        """Test that normalization preserves the input array shape."""
        input_vector = np.array([[1, 2], [3, 4]])
        
        actual_output = normalize_vector(input_vector)
        
        assert actual_output.shape == input_vector.shape
    
    def test_normalize_vector_float_precision(self):
        """Test normalize_vector with different float precisions."""
        input_vector = np.array([1.1, 2.2, 3.3], dtype=np.float32)
        
        actual_output = normalize_vector(input_vector)
        
        # Should work with float32 input
        assert actual_output.dtype == np.float32
        assert len(actual_output) == 3