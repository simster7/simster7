import shutil
import requests

shields = {
    "github": "https://img.shields.io/github/followers/simster7.svg?label=GitHub&style=social",
    "twitter": "https://img.shields.io/twitter/follow/simster7?label=Twitter&style=social",
    "linkedin": "https://img.shields.io/badge/LinkedIn--_.svg?style=social&logo=linkedin",
    "gmail": "https://img.shields.io/badge/Email-simbeh7@gmail.com-_.svg?style=social&logo=gmail"
}

for shield, url in shields.items():
    response = requests.get(url)
    if response.status_code == 200:
        with open("img/" + shield + ".svg", 'wb') as f:
            f.write(response.content)
