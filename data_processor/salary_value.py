import pprint
import re

import utils.text as TEXT

from utils.html_parser import list_improvement_jumps, list_salary

def calculate_salary_value(jumps, salarys):
    value = {}

    jumps_dict = {}

    for jump in jumps:
        name = jump[0].replace(' ', '')
        league = jump[1].split('.')[1]
        game_play = jump[5].split(' / ')[0]
        minute = jump[6].split(' / ')[0]
        eff = jump[8].split(' / ')[0]

        # ignore player with less data
        if(int(game_play) > TEXT.MIN_GAME_PLAY and float(minute) > TEXT.MIN_GAME_MINUTE):
            jumps_dict[name] = {}
            jumps_dict[name]["league"] = int(league)
            jumps_dict[name]["minute"] = float(minute)
            jumps_dict[name]["eff"] = float(eff)

    name_regex = re.compile("[a-zA-Z\.]+")
    salary_regex = re.compile("\d")
    for salary_row in salarys:
        name = "".join(name_regex.findall(salary_row[0]))
        salary = int("".join(salary_regex.findall(salary_row[8])))
        if name in jumps_dict.keys():
            value[name] = {}
            value[name]["salary"] = salary
            value[name]["value"] = int(jumps_dict[name]["eff"] / jumps_dict[name]["minute"] * TEXT.SALARY_WEIGHT[jumps_dict[name]["league"]])
            value[name]["rate"] =  format(value[name]["value"] / value[name]["salary"], '.2f')
    return value

def main():
    jumps = list_improvement_jumps()
    salary = list_salary()
    value = calculate_salary_value(jumps, salary) 
    pprint.pprint(value)

if __name__ == '__main__':
    main()