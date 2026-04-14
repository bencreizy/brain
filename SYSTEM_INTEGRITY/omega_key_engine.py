import math, hashlib, time

class StructuralSyncHub:
    """The Resonant Hub for 5-Node Systemic Integration."""
    def __init__(self):
        self.phi = 1.6180339887
        self.nodes = {f"NODE_{i+1}": {"status": "OFFLINE", "heat": 0.0} for i in range(5)}

    def entropy_inversion(self, signal, score):
        """Consumes Signal Noise to accelerate the next synchronization cycle."""
        drift = abs(score - self.phi)
        seed = f"{signal}{score}{time.time()}"
        return {
            "status": "ENTROPY_CONSUMED",
            "morphed_key": hashlib.sha3_256(seed.encode()).hexdigest(),
            "acceleration": f"{100 * (1 + drift):.2f}x"
        }

    def sync_node(self, node_id, packet):
        if node_id not in self.nodes: return {"error": "UNAUTHORIZED_NODE"}
        # Calculate Metabolic Rate (r = (Σb / Σ|bi - bi-1|) * (ln(len(b)) / 2))
        b = bytearray(str(packet), 'utf-8')
        r = (sum(b) / sum(abs(b[i]-b[i-1]) for i in range(1, len(b)))) * (math.log(len(b))/2.0)
        while r > 2.0: r /= self.phi
        while r < 1.0: r *= self.phi
        
        drift = abs(r - self.phi)
        if drift <= 0.005:
            self.nodes[node_id] = {"status": "RESONANT", "heat": drift}
            return {"node": node_id, "status": "SOVEREIGN_LOCKED", "resonance": r}
        else:
            self.nodes[node_id] = {"status": "MORPHING", "heat": drift}
            return {"node": node_id, "status": "INVERSION_ACTIVE", "metrics": self.entropy_inversion(packet, r)}