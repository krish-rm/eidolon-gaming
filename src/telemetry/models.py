"""
Eidolon Concept Models
======================
Core data structures for representing game-state and telemetry.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional

@dataclass
class Vec2:
    x: float = 0.0
    y: float = 0.0

@dataclass
class Entity:
    entity_id: str
    entity_type: str
    position: Vec2 = field(default_factory=Vec2)
    velocity: Vec2 = field(default_factory=Vec2)
    health: float = 1.0

@dataclass
class GameState:
    entities: List[Entity] = field(default_factory=list)
    timestamp_ms: float = 0.0
    tick: int = 0
