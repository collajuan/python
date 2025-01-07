from bs4 import BeautifulSoup
# *********** EJEMPLOS BeautifulSoup ***********************
# with open("website.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title.string)

# all_anchor = soup.find_all(name="a")
# print(all_anchor)

# for tag in all_anchor:
#     print(tag.getText())
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

# headings = soup.select(".heading")
# print(headings)

# **************** *Ejemplos sitios reales* ******************
import requests

response = requests.get("https://news.ycombinator.com/news")
# print(response.text)

soup = BeautifulSoup(response.text, "html.parser")
# print(soup)
articles = soup.select(".titleline > a")
# print(articles)
article_texts = [] 
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    # print(text)
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

articles_upvotes = [int(score.getText().split()[0]) for score in soup.select(".score")]

# print(article_texts)
# print(article_links)
# print(articles_upvotes)

max_value = max(articles_upvotes)
max_index = articles_upvotes.index(max_value)

print(article_texts[max_index])
print(article_links[max_index])
print(articles_upvotes[max_index])