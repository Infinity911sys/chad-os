"""
C.H.A.D OS – Unified Main Entrypoint
Cognitive Heuristic Adaptive Dynamics Operating System
"""

# Kernel
from kernel.bootstrap import bootstrap_system

# Services
from services.registry import ServiceRegistry
from services.identity_service import IdentityService
from services.memory_service import MemoryService
from services.context_engine import ContextEngine
from services.event_service import EventService
from services.continuity_service import ContinuityService

# Intelligence
from intelligence.heuristic_engine import HeuristicEngine
from intelligence.prediction_engine import PredictionEngine
from intelligence.reasoning_core import ReasoningCore
from intelligence.adaptive_hooks import AdaptiveHooks

# Continuity
from continuity.identity_graph import IdentityGraph
from continuity.continuity_engine import ContinuityEngine
from continuity.state_persistence import StatePersistence

# UI + Apps
from ui.rendering_engine import RenderingEngine
from ui.interaction_model import InteractionModel
from apps.system_tools.monitor import heartbeat


def wire_services(runtime: dict) -> dict:
    """
    Create and register all OS services.
    """

    registry = ServiceRegistry()

    # Core services
    identity = IdentityService()
    memory = MemoryService()
    context = ContextEngine(memory_service=memory)
    events = EventService(runtime["message_bus"])

    # Continuity
    graph = IdentityGraph()
    continuity = ContinuityService(graph)
    persistence = StatePersistence()

    # Register services
    registry.register("identity", identity)
    registry.register("memory", memory)
    registry.register("context", context)
    registry.register("events", events)
    registry.register("continuity", continuity)
    registry.register("graph", graph)
    registry.register("persistence", persistence)

    return registry


def wire_intelligence() -> dict:
    """
    Create the AI brain components.
    """

    heuristic = HeuristicEngine()
    prediction = PredictionEngine()
    reasoning = ReasoningCore(heuristic, prediction)
    adaptive = AdaptiveHooks()

    return {
        "heuristic": heuristic,
        "prediction": prediction,
        "reasoning": reasoning,
        "adaptive": adaptive,
    }


def wire_ui() -> dict:
    """
    Create UI components.
    """

    renderer = RenderingEngine()
    interaction = InteractionModel()

    return {
        "renderer": renderer,
        "interaction": interaction,
    }


def run_single_tick(runtime: dict, services: dict, intelligence: dict, ui: dict):
    """
    Run one cycle of the OS to prove the system is alive.
    """

    # Example: update context
    services["context"].set_context("system_status", "booted")

    # Example: AI reasoning
    signal = {"event": "system_boot", "context": services["context"].snapshot()}
    result = intelligence["reasoning"].process(signal)

    # Example: continuity record
    services["continuity"].record_event("system", {"boot": True})

    # Example: UI output
    ui["renderer"].render(f"CHAD OS Booted. Decision: {result['decision']}")

    # Example: heartbeat
    ui["renderer"].render(heartbeat())


def main():
    """
    Boot the OS, wire all components, and run one tick.
    """

    # 1. Boot kernel
    runtime = bootstrap_system()

    # 2. Wire services
    services = wire_services(runtime)

    # 3. Wire intelligence
    intelligence = wire_intelligence()

    # 4. Wire UI
    ui = wire_ui()

    # 5. Run one system tick
    run_single_tick(runtime, services, intelligence, ui)

    print("C.H.A.D OS initialization complete.")


if __name__ == "__main__":
    main()
