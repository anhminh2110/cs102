from __future__ import annotations

from typing import TYPE_CHECKING

from common.event import EventType, GameEvent
from common.types import FLAG_PART_TYPES, EntityType, QuestName

if TYPE_CHECKING:
    from worlds.world import World

def event_handler(world: World) -> None:
    """
    Logics for some specific events in level 2.
    """
    for event in world.events:
        npc_lil_buddy_id = world.get_entity_id_by_type(EntityType.NPC_LIL_BUDDY)

        # Player finishes FLAG quest.
        if (
            event.get_sender_id() == npc_lil_buddy_id
            and event.is_type(EventType.NPC_DIALOGUE_END)
            and world.player.count_inventory(FLAG_PART_TYPES) >= 2
        ):
            GameEvent(
                EventType.QUEST_END,
                listener_id=npc_lil_buddy_id,
                quest_name=QuestName.FLAG,
            ).post()

            world.player.discard_inventory(FLAG_PART_TYPES)

            # NPC makes the Flag
            npc = world.get_entity(npc_lil_buddy_id)
            world.add_entity(
                EntityType.LEVEL_END_FLAG,
                npc.rect.x + 56 + 14*34,
                npc.rect.y + 117 - 2*34,
            )