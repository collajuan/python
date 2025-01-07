from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

soup = BeautifulSoup(response.text, "html.parser")

movies_titles = soup.select(".article-title-description__text > h3")
# print(movies_titles)
movies_list = [movie.getText() for movie in movies_titles]
movies_list.reverse()
print(movies_list)
with open("movies.txt", "w", encoding='utf-8') as file:
    for movie in movies_list:
        file.write(movie)
        file.write("\n")
