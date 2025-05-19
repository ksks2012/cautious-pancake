import utils.text as TEXT

from utils import file_processor    
from utils.html_parser import list_draft

def main():
    draft_name = f"{TEXT.SEASON}-{TEXT.LEAGUE}-draft"
    player_list = list_draft(draft_name)
    file_processor.write_csv(f"./var/{draft_name}", player_list) 

if __name__ == '__main__':
    main()

