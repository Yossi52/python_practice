import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

title_list = soup.select(selector=".article-title-description__text>.title")
movie_titles = [title.getText() for title in title_list]
movie_titles.reverse()

movie_text = ""
for title in movie_titles:
    movie_text += f"{title}\n"

with open(file="movies.txt", mode="w", encoding="utf-8") as file:
    file.write(movie_text)
