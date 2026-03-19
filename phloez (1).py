import math
from typing import Dict

class ResonanceSDK:
    def __init__(self, node_id: str):
        self.node_id = node_id
        self.PHI = 1.6180339887

    def calculate_logic_heat(self, signal: str) -> Dict[str, float]:
        """Calculates the Metabolic Rate (r) to ensure logic stability."""
        b = signal.encode('utf-8')
        length = len(b)
        if length < 2: return {"r": 1.0, "drift": abs(1.0 - self.PHI)}
        sum_b = sum(b)
        sum_diff = sum(abs(b[i] - b[i-1]) for i in range(1, length))
        r = (sum_b / sum_diff) * (math.log(length) / 2.0) if sum_diff != 0 else 0.0
        while r > 2.0: r /= self.PHI
        while r < 1.0: r *= self.PHI
        return {"r": r, "drift": abs(r - self.PHI)}

    def sync_lattice(self, signal: str):
        heat = self.calculate_logic_heat(signal)
        return {
            "node": self.node_id,
            "status": "RESONANT" if heat['drift'] <= 0.005 else "DRIFT",
            "metrics": heat
        }