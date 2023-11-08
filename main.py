from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options)
driver.get('https://sports.tipico.com/de/alle/1101/680910,31201,1201,680810/virtual_europaLeagueMatches,34301,37886301,37885301,33301,17301,72301,84301,virtual_championsLeagueMatches')
all_links = driver.find_element(By.TAG_NAME, 'div')

quoten = all_links.find_elements(By.CLASS_NAME,'EventOddButton-styles-odd-button')
teams = all_links.find_elements(By.CLASS_NAME,'EventTeams-styles-team')
kategorie = all_links.find_elements(By.CLASS_NAME,'EventOddGroup-styles-fixed-param-text')
matches = []
quoten_decoded = []
team_decoded = []
for t in teams:
    team_decoded.append(t.text)

for q in quoten:
    quoten_decoded.append(q.text)

def chunk(lst, size):
    for i in range(0, len(lst), size):
        yield lst[i:i + size]
split_quoten_list = []
for c in chunk(quoten_decoded,12):
    split_quoten_list.append(c)
#print(split_quoten_list)
split_team_list = []
for t in chunk(team_decoded,2):
    split_team_list.append(t)
#print(split_team_list)

for i in range(len(split_quoten_list)):
    matches.append(split_team_list[i]+split_quoten_list[i])
for m in matches:
    print(m)
driver.quit()

