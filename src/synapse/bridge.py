"""
Eidolon Concept: Synapse Link Bridge
====================================
The conceptual bridge mapping swarm intelligence to somatic hardware signals.
"""

from dataclasses import dataclass
from typing import List, Dict, Any, Optional
from ..telemetry.models import GameState, Entity
from ..engine.swarm import EidolonSwarm, SwarmResult

@dataclass
class PreCognitiveSignal:
    intent: str
    signal_classification: str
    eidolon_consensus: float
    simulation_entropy: float
    lead_time_ms: int
    hardware_target: str
    metadata: dict

    def to_dict(self) -> dict:
        return {
            "intent": self.intent,
            "signal_classification": self.signal_classification,
            "eidolon_consensus": round(self.eidolon_consensus, 3),
            "simulation_entropy": round(self.simulation_entropy, 3),
            "lead_time_ms": self.lead_time_ms,
            "hardware_target": self.hardware_target,
            "metadata": self.metadata,
        }

class SynapseLinkBridge:
    def __init__(self):
        self.swarm = EidolonSwarm(500)

    def process(self, game_state: GameState, hardware_target: str = "CONTROLLER") -> List[PreCognitiveSignal]:
        """Conceptual processing of game state into somatic signals."""
        signals = []
        
        # Scenario: Minimal conceptual check for Flank Detection
        player = next((e for e in game_state.entities if e.entity_type == "player"), None)
        enemies = [e for e in game_state.entities if e.entity_type == "enemy"]
        
        for enemy in enemies:
            # Physics-based condition (for concept)
            dx = enemy.position.x - player.position.x
            dy = enemy.position.y - player.position.y
            dist = (dx*dx + dy*dy)**0.5
            
            # Simple condition logic for FLANK_DETECTION concept
            is_flanking = dist < 100
            result = self.swarm.evaluate_intent(is_flanking)
            
            if result.consensus > 0.5:
                # Ghost Layer: Entropy check (concept)
                classification = "PROBABLE"
                intensity = 0.5
                ramp = "SHARP"
                
                if result.entropy > 0.5:
                    classification = "POSSIBILITY"
                    intensity = 0.2
                    ramp = "SHIMMER"
                
                signals.append(PreCognitiveSignal(
                    intent="FLANK_DETECTION",
                    signal_classification=classification,
                    eidolon_consensus=result.consensus,
                    simulation_entropy=result.entropy,
                    lead_time_ms=2000 if classification == "PROBABLE" else 500,
                    hardware_target="HEADSET" if classification == "PROBABLE" else "CUSHION",
                    metadata={"direction": "RIGHT", "intensity_scalar": intensity, "ramp_profile": ramp}
                ))
                
        return signals
