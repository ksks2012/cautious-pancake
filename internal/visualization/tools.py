from matplotlib.font_manager import FontProperties

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

class VisualizeTool():
    def __init__(self, data):
        self.data = data
        self.df = pd.DataFrame(data)

        # Set font globally
        try:
            plt.rcParams['font.family'] = "WenQuanYi Micro Hei"
        except:
            print("Font not found, using default font.")
            pass

    def plot_total_shots_by_player(self):
        plt.figure(figsize=(10, 6))
        sns.barplot(data=self.df, x='shot_class', y='total_shots', hue='player_name')
        plt.title('Total Shots by Player and Shot Class')
        plt.xlabel('Shot Class')
        plt.ylabel('Total Shots')
        plt.xticks(rotation=45)
        plt.legend(title='Player Name')
        plt.tight_layout()
        plt.show()
        plt.savefig('./fig/total_shots_by_player.png', dpi=300, bbox_inches='tight')

    def plot_chance_vs_quality(self):
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=self.df, x='avg_shot_chance', y='avg_shot_quality', hue='player_name', style='shot_class', s=100)
        plt.title('Shot Chance vs Shot Quality')
        plt.xlabel('Average Shot Chance')
        plt.ylabel('Average Shot Quality')
        plt.legend(title='Player & Shot Class', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        plt.show()
        plt.savefig('./fig/chance_vs_quality.png', dpi=300, bbox_inches='tight')


    def plot_avg_skills_ratio(self):
        pivot_table = self.df.pivot_table(values='avg_skills_ratio', index='player_name', columns='shot_class')
        plt.figure(figsize=(12, 6))
        sns.heatmap(pivot_table, annot=True, cmap='coolwarm', linewidths=0.5)
        plt.title('Average Skills Ratio by Player and Shot Class')
        plt.xlabel('Shot Class')
        plt.ylabel('Player Name')
        plt.tight_layout()
        plt.show()
        plt.savefig('./fig/avg_skills_ratio.png', dpi=300, bbox_inches='tight')

    def plot_avg_shot_chance(self):
        pivot_table = self.df.pivot_table(values='avg_shot_chance', index='player_name', columns='shot_class')
        plt.figure(figsize=(12, 6))
        sns.heatmap(pivot_table, annot=True, cmap='coolwarm', linewidths=0.5)
        plt.title('Average Shot Chance by Player and Shot Class')
        plt.xlabel('Shot Class')
        plt.ylabel('Player Name')
        plt.tight_layout()
        plt.show()
        plt.savefig('./fig/avg_shot_chance.png', dpi=300, bbox_inches='tight')

    def plot_avg_shot_quality(self):
        pivot_table = self.df.pivot_table(values='avg_shot_quality', index='player_name', columns='shot_class')
        plt.figure(figsize=(12, 6))
        sns.heatmap(pivot_table, annot=True, cmap='coolwarm', linewidths=0.5)
        plt.title('Average Shot Quality by Player and Shot Class')
        plt.xlabel('Shot Class')
        plt.ylabel('Player Name')
        plt.tight_layout()
        plt.show()
        plt.savefig('./fig/avg_shot_quality.png', dpi=300, bbox_inches='tight')
