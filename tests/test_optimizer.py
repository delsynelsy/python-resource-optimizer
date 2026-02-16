import pytest
from app.services.optimizer import ResourceOptimizer

def test_allocation_logic():
    # Test a 40-hour task with a 5-day deadline (1 machine needed)
    result = ResourceOptimizer.calculate_machinery(40, 5)
    assert result["units_needed"] == 1
    assert result["status"] == "Optimal"

def test_invalid_deadline():
    with pytest.raises(ValueError):
        ResourceOptimizer.calculate_machinery(40, 0)