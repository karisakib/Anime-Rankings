from app import db, AnimeTable
from bs4 import BeautifulSoup 
import requests

r = requests.get("https://myanimelist.net/topanime.php")

soup = BeautifulSoup(r.text, features="html.parser")

for_removal_1 = soup.find_all(class_="information")
for_removal_2 = soup.find_all(class_="manga-store-information")
for_removal_3 = soup.find_all(class_=lambda x: x is not None and "watch" in x)

for to_remove in for_removal_1 + for_removal_2 + for_removal_3:
    to_remove.extract()

table = soup.find("table", class_="top-ranking-table")

rows = table.find_all("tr")

clean_data = []
for row in rows[1:]:
    link = row.find('a')["href"]
    stripped_list = list(row.stripped_strings)
    stripped_list.append(link)    
    clean_data.append(stripped_list)


def main():
    db.drop_all()
    db.create_all()

    for row in clean_data:
        new_row = AnimeTable(rank=row[0], title=row[1], rating=row[2], link=row[4])
        db.session.add(new_row)
        db.session.commit()

if __name__ == "__main__":
    main()