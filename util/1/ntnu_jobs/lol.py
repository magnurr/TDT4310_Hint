import requests
import json
with open("dump.json", "w") as file:
    file.write(json.dumps(requests.get(
        "https://www.ntnu.edu/vacancies?p_p_id=vacanciesportlet_WAR_vacanciesportlet&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_resource_id=feed&p_p_cacheability=cacheLevelPage").json()))
