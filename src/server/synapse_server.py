"""
Eidolon Concept: Synapse Server
===============================
Conceptual real-time WebSocket and REST API.
"""

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from typing import Dict, Any, List

from ..telemetry.models import GameState, Entity, Vec2
from ..synapse.bridge import SynapseLinkBridge

app = FastAPI(title="Eidolon Synapse: Conceptual Server")
bridge = SynapseLinkBridge()

@app.post("/api/v1/process")
async def process_frame(payload: Dict[str, Any]):
    """Synchronous single-frame processing conceptually."""
    try:
        # Extract Bare GameState from dict (for demo)
        entities = []
        for e in payload.get("entities", []):
            entities.append(Entity(
                entity_id=e.get("entity_id", "unknown"),
                entity_type=e.get("entity_type", "unknown"),
                position=Vec2(**e.get("position", {"x": 0, "y": 0})),
                velocity=Vec2(**e.get("velocity", {"x": 0, "y": 0}))
            ))
        
        gs = GameState(entities=entities, timestamp_ms=payload.get("timestamp_ms", 0))
        signals = bridge.process(gs)
        
        return JSONResponse(content={
            "signals": [s.to_dict() for s in signals],
            "count": len(signals),
            "latency_ms": 1.25 # Conceptual baseline
        })
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Concept error: {str(e)}")

# This ensures `uvicorn src.server.synapse_server:app` works.
# No advanced connection management — concept only.
