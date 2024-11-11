import requests
import time

import utils.text as TEXT

def download_html(url):
    time.sleep(3)
    try:
        if url[0:4] != "http":
            url = TEXT.BASE_URL + url
        response = requests.get(url)
        response.raise_for_status()
        html_text = response.text
        return html_text
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None