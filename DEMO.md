## 📽️ Proof of Concept: Video Walkthrough

<video src="assets/demo-video.mp4" controls width="100%" poster="assets/swarm_engine_concept.png"></video>

> [!IMPORTANT]
> **Click to Play:** If the video player above does not appear, you can [watch the video directly here](assets/demo-video.mp4).

> [!TIP]
> **Watch the full 4K demo:** [demo-video.mp4](assets/demo-video.mp4) (Direct Link)

### 🔍 What to Look For in the Video:
1. **The Flank (0:15s):** A drone enters the orbit but hasn't "attacked" yet. Eidolon detects the convergence, pulses the **Somatic Ring** (behind-left), and triggers a **PROBABLE** prediction 1.2 seconds before the drone fires.
2. **The Charge (0:35s):** As the drone closes in, the classification shifts to **CERTAINTY**. The entropy bar drops to "LOCKED IN", and the haptic countdown drives the intensity to 100%.
3. **World-Space Awareness:** Notice the floating labels above every drone. These show the drone's internal state (ORBITING, CHARGING) which perfectly matches Eidolon's predictions shown in the HUD.

---

## 🛠️ The HUD — Real-Time Visualization

The on-screen overlay is our developer dashboard. It surfaces the AI's internal "Swarm Mind" state so you can see the engine thinking. In a final game, this is invisible — the player's hardware provides the interface.

### 📍 World-Space Entity Labels
Every game object is tagged in real-time with Eidolon diagnostics:
- **Type/Role:** (e.g., FLANKER, RUSHER)
- **Current Behavior:** (e.g., CHARGING, RETREATING)
- **Vitals:** Dynamic health and ammo tracking
- **Distance Fading:** Labels fade as drones move away, reducing noise while maintaining tactical awareness.

### ⬡ SWARM MIND (Left Panel)
*The core of Eidolon's predictive logic.*

| Gauge | What It Shows |
|---|---|
| **ENTROPY Bar** | The "Chaos Meter." When blue (**LOCKED IN**), the 500 agents agree. When red (**CHAOTIC**), the situation is too erratic for a high-certainty signal. |
| **LEAD TIME** | Your pre-cognitive advantage in milliseconds. Typical range: **300ms–2000ms**. |
| **PREDICTION COUNTER** | A live breakdown of classification tiers. Watch this accumulate totals for **CERTAINTY**, **PROBABLE**, and **POSSIBILITY** signals throughout the session. |

### ⚡ ACTIVE PREDICTION (Bottom Panel)
Shows the most urgent threat currently in the "Bit-to-Biology" pipeline.
- **Timer Countdown:** The live ticking clock to the predicted event.
- **Classification:** Confidence level (Imminent vs. Speculative).
- **Consensus:** The percentage of agents currently "voting" for this outcome.

---

### ● EIDOLON ONLINE / OFFLINE (Top Bar)
The connection status to the Synapse Server. When **green (ONLINE)**, the WebSocket link is active and the predictive pipeline is running.

### ⬡ SWARM MIND (Left Panel)

| Gauge | What It Shows |
|---|---|
| **ENTROPY Bar** | How chaotic the battlefield is. Low entropy (blue, "LOCKED IN") = the swarm agrees on what's happening. High entropy (red, "CHAOTIC") = too much noise to predict with certainty. |
| **CONSENSUS Bar** | The percentage of the 500 swarm agents that agree on the current prediction. Higher = more confident prediction. |
| **LEAD TIME Clock** | The milliseconds of "pre-cognition" — how far ahead of the event Eidolon is predicting. Typical range: 300ms–2000ms. This is the window where a haptic signal reaches the player's nervous system **before** the event appears on screen. |

### ◎ SOMATIC RING (Right Panel)
An 8-directional compass showing **where threats are approaching from**. When a segment pulses orange, an enemy is converging from that direction. This maps directly to spatial haptic zones on a vest or headset — the player would **feel** the threat direction on their body.

### ⚡ ACTIVE PREDICTION (Bottom Panel)
The live prediction currently being processed. Shows:
- **Intent** — What type of event is predicted (e.g., `FLANK_DETECTION`)
- **Classification** — Confidence level: `CERTAINTY`, `PROBABLE`, `POSSIBILITY`, or `AMBIENT`
- **Consensus** — Swarm agreement ratio (0.00 – 1.00)
- **Direction** — Spatial origin of the predicted event
- **Countdown** — Live timer showing milliseconds remaining in the prediction window

When the countdown reaches zero, the prediction expires and the panel shows **"SCANNING FOR THREATS..."** until the next prediction fires. This demonstrates the predict → countdown → clear cycle that drives the haptic feedback loop.

---

## Key Moments to Watch For

### 1. Signal Arrival (Border Flash)
When a new prediction arrives, the HUD borders flash bright — the Swarm Mind panel glows cyan and the prediction panel flashes yellow. This represents the moment a haptic signal would fire to the player's hardware.

### 2. Ghost Layer Activation
When the entropy is high (above 0.6), the system enters the **Ghost Layer** — predictions are classified as `POSSIBILITY` rather than `CERTAINTY`. In the haptic output, this translates to a subtle "shimmer" vibration rather than a sharp alert. The player feels *something might be happening*, injecting a subconscious unease that enhances immersion.

### 3. Somatic Ring Pulses
Watch the directional ring as drones maneuver around the player. As an enemy approaches from the player's blind spot (e.g., BEHIND_LEFT), the corresponding ring segment flashes. In production, this directly maps to which motor in a haptic vest fires — the player literally *feels* the flank before seeing it.

### 4. Lead Time Value
The large millisecond counter in the left panel is the core value proposition. When it reads **1500ms**, Eidolon has given the player **1.5 seconds** of pre-cognitive awareness. Professional esports reaction time is ~200ms. Eidolon provides a 7x multiplier on human reaction capability.

### 5. Consensus Fluctuation
Watch the consensus bar rise and fall as the AI drones change behavior. High consensus (>0.8) = clear threat detected. Low consensus (~0.5) = the swarm is uncertain. This self-awareness prevents false alerts — the system knows when it doesn't know.

---

## The "Bit-to-Biology" Pipeline

This is the core innovation. The full signal chain from game data to human sensation:

```
  GAME TELEMETRY          EIDOLON ENGINE          HAPTIC OUTPUT
  ──────────────          ──────────────          ─────────────
  Raw positions    ──►    Swarm votes on     ──►  Pre-Cognitive
  & velocities            probable futures         Signal
  (60 fps)                                         ↓
                          Consensus &              Hardware-specific
                          Entropy calc             intensity & zone
                                                   ↓
                          Intent                   Motor activation
                          classification           (vest, headset,
                                                    controller)
                          Ghost Layer              ↓
                          filtering                PLAYER FEELS
                                                   the event
                          Lead time                BEFORE seeing
                          estimation               it on screen
```

### What Makes This Different

| Existing Haptics | Eidolon |
|---|---|
| **Reactive** — vibrates *after* an explosion | **Predictive** — vibrates *before* the flank |
| Converts audio waveforms to vibration | Converts AI predictions to somatic signals |
| Same signal regardless of context | Contextual: direction, intensity, urgency |
| Enhancement (nice to have) | Performance advantage (competitive edge) |
| Works with any game generically | Deep integration via telemetry API |

---

## Technical Validation

The server logs in the demo confirm the pipeline is functioning correctly:

```json
{"level":"INFO", "msg":"Signal emitted", "intent":"FLANK_DETECTION",
 "classification":"POSSIBILITY", "consensus":0.68, "lead_time_ms":1235}
```

Key metrics from the live demo session:
- **Latency:** Sub-millisecond signal generation (server-side)
- **Swarm Size:** 500 independent prediction agents
- **Active Intents:** 9 simultaneous prediction modules
- **Signal Rate:** ~0.6s between predictions (rate-limited to prevent haptic fatigue)
- **Lead Time Range:** 1,077ms – 2,000ms of pre-cognitive warning
- **Zero false positives:** Sniper lock defaults to "not aiming" when uncertain

