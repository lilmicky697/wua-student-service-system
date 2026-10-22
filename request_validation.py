import pytest
from service_fee import calcuate_service_fee


def test_zero_amount():
    assert calculate_service_fee(0) == 0


def test_amount_at_free_fee_limit():
    assert calculate_service_fee(100) == 0


def test_amount_above_limit():
    assert calculate_service_fee(200) == 10


def test_negative_amount_is_rejected():
    with pytest.raises(ValueError):
        calculate_service_fee(-10)


def test_large_amount():
    assert calculate_service_fee(1000000) == 50000


def test_decimal_amount():
    assert calculate_service_fee(150.50) == pytest.approx(7.525)
