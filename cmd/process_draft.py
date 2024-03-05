import utils.text as TEXT

from utils import file_processor    
from utils.html_parser import list_draft

def main():
    player_list = list_draft()
    file_processor.write_csv(f"./var/{TEXT.SEASON}-3.3-draft", player_list) 

if __name__ == '__main__':
    main()

