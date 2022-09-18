from __future__ import annotations

import random
from typing import TYPE_CHECKING, Sequence

from common import util
from common.event import EventType, GameEvent
from entities.base_entity import BaseEntity

if TYPE_CHECKING:
    from worlds.world import World

logger = util.get_logger(__name__)


class Sonic(BaseEntity):
    def __init__(
        self,
        animation_interval_ms: int = 80,
        speed: int = 0,
        gravity: int = 0,
        init_dx: int = 0,
        init_dy: int = 0,
        jump_vertical_speed: int = 0,
        damage : int = 0,
        *args,
        **kwargs,
    ) -> None:
        super().__init__(*args, **kwargs)

        # The gravity value unique to this subject.
        self.gravity = gravity

        # How fast this subject moves.
        self.speed: int = speed
        self.jump_vertical_speed: int = jump_vertical_speed
        self.damage = damage

        # Amount of delta (change) in position, along the 2 axis.
        self.dx: int = init_dx
        self.dy: int = init_dy

        # Tracking the states of this subject
        self.moving_left: bool = False
        self.moving_right: bool = False
        self.is_landed: bool = False  # Let subject fall to stable position
        self.is_dying: bool = False

        # minimal time until switching to next sprite
        self.animation_interval_ms: int = animation_interval_ms
        self.last_animation_ms: int = 0

    def update(self, events: Sequence[GameEvent], world: World) -> None:
        super().update(events, world)
        # Knowing the current state of the subject, we calculate the amount of changes
        # - dx and dy - that should occur to the player position during this current game tick.

        # Step 1: calculate would-be dx, dy when unobstructed
        self.dx = 0

        if self.is_landed:
            self.dy = 0
        self.dy += self.gravity

        if self.moving_left:
            self.dx = -self.speed
        if self.moving_right:
            self.dx = self.speed

        # Step 2: update current position by the deltas
        self.rect.x += self.dx
        self.rect.y += self.dy

    def move_left(self, enabled=True):
        self.moving_left = enabled
        if self.moving_left:
            self.moving_right = False



