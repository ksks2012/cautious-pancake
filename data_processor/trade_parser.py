from bs4 import BeautifulSoup
import pandas as pd


def parse_trade_table():
    with open('./var/trade_250411.html', 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    table = soup.find('table', class_='datatable display compact nowrap')

    headers = []
    thead = table.find('thead')
    for th in thead.find_all('th'):
        headers.append(th.text.strip())

    rows = []
    tbody = table.find('tbody')
    for tr in tbody.find_all('tr'):
        row = []
        for td in tr.find_all('td'):
            text = td.text.strip()
            # Special handling for fields containing flags and links (e.g., Name)
            if td.find('a'):
                # If it's the Name column, extract the player's name and ignore the flag
                if td.find('img'):
                    text = td.find('a').text.strip()
            row.append(text)
        rows.append(row)

    # Rename keys in the headers list to match the desired column names
    headers = [header.replace('年齡', 'Age')
                        .replace('高', 'Height')
                        .replace('運動', 'Athletics')
                        .replace('投', 'Shooting')
                        .replace('防', 'Defense')
                        .replace('攻', 'Offense')
                        .replace('潛', 'Potential')
                        .replace('薪資', 'Salary')
                        .replace('限制等級', 'Trade Level')
                        .replace('位置', 'Position')
                        .replace('球隊', 'Team')
                        .replace('名字', 'Name') for header in headers]
    data_dict = [dict(zip(headers, row)) for row in rows]

    # Clean up data in data_dict
    for item in data_dict:
        if 'RT' in item:
            item['RT'] = int(item['RT'].replace(' RT', ''))
        if 'Age' in item:
            item['Age'] = int(item['Age'].replace(' 歲', ''))
        if 'Height' in item:
            item['Height'] = int(item['Height'].replace(' 公分', ''))

    import pprint
    pprint.pprint(data_dict)

    # Convert data_dict to a DataFrame and save it as a CSV file
    df = pd.DataFrame(data_dict)
    df.to_csv('./var/trade_data.csv', index=False, encoding='utf-8-sig')

if __name__ == "__main__":
    parse_trade_table()