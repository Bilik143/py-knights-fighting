"""Main entry point for the knights fighting game."""

from typing import Any, Dict

from app.battle import BattleSimulation
from app.constants import KNIGHTS


def battle(knights_config: Dict[str, Dict[str, Any]]) -> Dict[str, int]:
    """Execute a tournament battle simulation.

    Args:
        knights_config: Configuration dict with knights' stats and equipment.

    Returns:
        Dictionary mapping knight names to their final HP values.
    """
    tournament = BattleSimulation(knights_config)
    return tournament.run_tournament()


if __name__ == "__main__":
    print(battle(KNIGHTS))
