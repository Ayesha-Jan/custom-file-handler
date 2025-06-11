import pytest
import random
from unittest.mock import patch
from dice_simulation import (
    dice_roll,
)


@pytest.fixture
def seed_and_patch():
    random.seed(40)
    with patch("matplotlib.pyplot.show"):
        yield


def test_rolls_values(seed_and_patch):
    """
    Test that dice_roll yields values between 1 and 6.
    """
    rolls = dice_roll(100)
    assert isinstance(rolls, list)
    assert all(1 <= roll <= 6 for roll in rolls)


def test_number_of_rolls(seed_and_patch):
    """
    Test that dice_roll returns correct number of rolls.
    """
    rolls = dice_roll(1000)
    assert len(rolls) == 1000


@pytest.mark.parametrize("n", [10, 100, 1000])
def test_multiple_roll_sizes(n, seed_and_patch):
    """
    Test dice_roll for different input sizes.
    """
    rolls = dice_roll(n)
    assert len(rolls) == n
