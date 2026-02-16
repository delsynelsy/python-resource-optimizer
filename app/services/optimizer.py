from typing import List, Dict
from math import ceil

class ResourceOptimizer:
    """Senior-level logic: Handles complex resource allocation."""
    
    @staticmethod
    def calculate_machinery(task_hours: float, deadline_days: int) -> Dict:
        if deadline_days <= 0:
            raise ValueError("Deadline must be at least 1 day.")
            
        # Example logic: 8-hour work shifts
        total_shifts = deadline_days * 8
        units_required = ceil(task_hours / total_shifts)
        
        return {
            "units_needed": units_required,
            "efficiency_rate": round(task_hours / (units_required * total_shifts), 2),
            "status": "Optimal" if units_required > 0 else "Idle"
        }