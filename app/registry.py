from __future__ import annotations


class DeadPatternRegistry:
    def burn(self, corpse: dict) -> None:
        _ = corpse
        print("pattern burned")
