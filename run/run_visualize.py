import sys

from internal.visualization.tools import VisualizeTool
from utils import file_processor

def run(team: str):
    data = file_processor.read_json(f"./var/{team}_shot_data_analysis.json")
    visualize_tool = VisualizeTool(data)
    visualize_tool.plot_total_shots_by_player()
    visualize_tool.plot_chance_vs_quality()
    visualize_tool.plot_avg_skills_ratio()
    visualize_tool.plot_avg_shot_chance()
    visualize_tool.plot_avg_shot_quality()

if __name__ == '__main__':
    args = sys.argv[1:]
    run(args[0])