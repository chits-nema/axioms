from dataclasses import dataclass, field
from typing import Dict

@dataclass
class WeightProfile: 
    buyer_id: str
    weights: Dict[str, float] = field(default_factory=dict)

    #Slider
    def set_weights(self, metric: str, value: float):
        if not 0.0 <= value <= 1.0: 
            raise ValueError("Value is out of bounds")
        self.weights[metric] = value
    
    #We normalize to 100 here
    def normalize_weight(self) -> Dict[str, float]:
        total = sum(self.weights.values())
        if total == 0: 
            return self.weights
        return {k: v / total for k, v in self.weights.item()}