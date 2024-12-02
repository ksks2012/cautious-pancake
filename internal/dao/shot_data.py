from sqlalchemy import (
    Column,
    String,
    Float,
    Integer,
)

import hashlib
import uuid

from internal.dao import Base

class ShotData(Base):
    __tablename__ = 'ShotData'

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False)
    game_id = Column(String, nullable=False)
    team_id = Column(String, nullable=False)
    team_name = Column(String, nullable=False)
    player_id = Column(String, nullable=False)
    player_name = Column(String, nullable=False)
    shot_class = Column(String, nullable=False)
    shot_chance = Column(Integer, nullable=False)
    skill_rate = Column(Integer, nullable=False)
    quality_rate = Column(Integer, nullable=False)
    defender_id = Column(String, nullable=False)
    defender_name = Column(String, nullable=False)

    def __str__(self):
        return (
            f"ShotData(\n"
            f"  game_id={self.game_id},\n"
            f"  team_id={self.team_id},\n"
            f"  team_name={self.team_name},\n"
            f"  player_id={self.player_id},\n"
            f"  player_name={self.player_name},\n"
            f"  shot_class={self.shot_class},\n"
            f"  shot_chance={self.shot_chance},\n"
            f"  skill_rate={self.skill_rate},\n"
            f"  quality_rate={self.quality_rate},\n"
            f"  defender_id={self.defender_id},\n"
            f"  defender_name={self.defender_name}\n"
            f")"
        )