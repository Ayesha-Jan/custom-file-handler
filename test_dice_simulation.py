import pytest
import random
from unittest.mock import patch
from dice_simulation import (
    dice_rolls,
    simulate_and_plot,
)  # Replace with actual module name


def test_dice_rolls_values():
    """Test that dice_rolls yields values between 1 and 6."""
    random.seed(40)
    rolls = list(dice_rolls(100))
    assert all(1 <= roll <= 6 for roll in rolls)
    assert len(rolls) == 100


def test_dice_rolls_distribution_length():
    """Test that simulate_and_plot returns correct number of rolls."""
    random.seed(40)
    with patch("matplotlib.pyplot.show"):  # Prevent plot from displaying
        results = simulate_and_plot(1000)
    assert isinstance(results, list)
    assert len(results) == 1000
    assert all(1 <= roll <= 6 for roll in results)


@pytest.mark.parametrize("n", [10, 100, 1000])
def test_multiple_roll_sizes(n):
    """Test simulate_and_plot for different input sizes."""
    random.seed(40)
    with patch("matplotlib.pyplot.show"):
        results = simulate_and_plot(n)
    assert len(results) == n


def test_distribution_decorator_plot_called(monkeypatch):
    """Ensure plt.show is called inside the decorator."""
    called = {"show": False}

    def fake_show():
        called["show"] = True

    monkeypatch.setattr("matplotlib.pyplot.show", fake_show)

    random.seed(40)
    simulate_and_plot(50)
    assert called["show"] is True
