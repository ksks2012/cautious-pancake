from collections import defaultdict
from typing import List, Mapping

from utils import file_processor
import utils.text as TEXT

def analyze_shot_data(shot_data: Mapping, team: str) -> List[Mapping]:
    stats = defaultdict(lambda: defaultdict(lambda: {
        "total_shots": 0, "skills_ratio_sum": 0, "shot_chance_sum": 0, "shot_quality_sum": 0
    }))

    # Aggregate data for each player under different shot classes
    for entry in shot_data:
        player_name = entry["player_name"]
        shot_class = TEXT.SHOT_CLASS_MAPPING.get(entry["shot_class"], "Unknown") 
        stats[player_name][shot_class]["total_shots"] += 1
        stats[player_name][shot_class]["skills_ratio_sum"] += entry["skills_ratio"]
        stats[player_name][shot_class]["shot_chance_sum"] += entry["shot_chance"]
        stats[player_name][shot_class]["shot_quality_sum"] += entry["shot_quality"]

    # Calculate averages and prepare output
    results = []
    for player_name, shot_classes in stats.items():
        for shot_class, values in shot_classes.items():
            total_shots = values["total_shots"]
            avg_skills_ratio = values["skills_ratio_sum"] / total_shots
            avg_shot_chance = values["shot_chance_sum"] / total_shots
            avg_shot_quality = values["shot_quality_sum"] / total_shots
            results.append({
                "player_name": player_name,
                "shot_class": shot_class,
                "total_shots": total_shots,
                "avg_skills_ratio": round(avg_skills_ratio, 2),
                "avg_shot_chance": round(avg_shot_chance, 2),
                "avg_shot_quality": round(avg_shot_quality, 2)
            })

    for result in results:
        print(result)

    file_processor.write_json(f"./var/{team}_shot_data_analysis.json", results)
