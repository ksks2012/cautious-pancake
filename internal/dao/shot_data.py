from sqlalchemy import (
    Column,
    String,
    Float,
    Integer,
)
from typing import Mapping

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
    skills_ratio = Column(Integer, nullable=False)
    shot_quality = Column(Integer, nullable=False)
    defender_id = Column(String, nullable=False)
    defender_name = Column(String, nullable=False)

    def __init__(self, shot_data: Mapping):
        self.game_id = shot_data["game_id"]
        self.team_id = shot_data["team_id"]
        self.team_name = shot_data["team_name"]
        self.player_id = shot_data["player_id"]
        self.player_name = shot_data["player_name"]
        self.shot_class = shot_data["shot_class"]
        self.shot_chance = shot_data["shot_chance"]
        self.skills_ratio = shot_data["skills_ratio"]
        self.shot_quality = shot_data["shot_quality"]
        self.defender_id = shot_data["defender_id"]
        self.defender_name = shot_data["defender_name"]

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
            f"  skills_ratio={self.skills_ratio},\n"
            f"  shot_quality={self.shot_quality},\n"
            f"  defender_id={self.defender_id},\n"
            f"  defender_name={self.defender_name}\n"
            f")"
        )