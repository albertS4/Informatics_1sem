from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

BASE = "https://ru.wikipedia.org"
HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def article_to_url(title: str) -> str:
    return f"{BASE}/wiki/{title.replace(' ', '_')}"

driver = webdriver.Edge()

#randoms = ["Философия", "Физика", "Систематика", "Биология"]
layers = [[article_to_url("Систематика")]]
used = set()
MX_DEPTH = 5
for i in range(MX_DEPTH):
    print(layers)
    with open("layer" + str(i) +".json", "w") as f:
        f.write(str(layers))
    layers.append([])
    random.shuffle(layers[i])
    for j in range(len(layers[i])):
        if j >= 100:
            break
        try:
            neighbors = []
            driver.get(layers[i][j])
            elements = driver.find_element(By.ID, "bodyContent").find_elements(By.TAG_NAME, 'a')
            e = 0
            n = 0
            while e < len(elements):
                attr = elements[e].get_attribute("href")
                if (not attr in used) and "ru.wikipedia.org" in attr:
                    neighbors.append(attr)
                    n += 1
                if n > 15:
                    break
                e += 1
        except Exception as e:
            print(f"Ошибка при обработке статьи : {e}")
        layers[-1].extend(neighbors)
        used.update(neighbors)
        print(100*j/len(layers[i]))