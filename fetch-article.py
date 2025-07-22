#!/usr/bin/env python3

import sys
from urllib.request import urlopen
from pathlib import Path

from bs4 import BeautifulSoup
from html_to_markdown import convert_to_markdown

url = sys.argv[1]
name = Path(url).name

with urlopen(url) as rsp:
    html = BeautifulSoup(rsp.read())

article = html.find('article')
datetime = article.find('time', attrs = {'class' : ['entry-date', 'published']}).attrs['datetime']
title = article.find('h1', attrs = {'class' : 'entry-title'}).text
thumbnail = article.find('figure', attrs = {'class': ['post-thumbnail']}).find('img')

for fig in article.find_all('figure'):
    img = fig.find('img')
    if img:
        fig.replace_with(img)
        br1 = html.new_tag('br')
        br2 = html.new_tag('br')
        img.insert_after(br1)
        img.insert_after(br2)

images = article.find_all('img')
images_dir = Path('content/images') / name

if len(images) > 0:
    images_dir.mkdir(exist_ok=True, parents=True)

for img in images:
    url = img.get('data-orig-file')
    filename = images_dir / Path(url).name
    img.attrs = { 'alt': 'image', 'src': '/' + str(Path(*filename.parts[1:])) }
    print(url, end=": ")
    with urlopen(url) as rsp:
        with open(filename, 'wb') as f:
            f.write(rsp.read())
    print("✓")

content = article.find('div', attrs = {'class': ['entry-content']})

content.insert(0, thumbnail)
br1 = html.new_tag('br')
br2 = html.new_tag('br')
thumbnail.insert_after(br1)
thumbnail.insert_after(br2)

for div in content.find_all('div'):
    attrs = div.attrs or {}
    _id = attrs.get('id', '')
    if 'atatags' in _id or 'relatedposts' in _id or 'jp-post-flair' == _id:
        div.extract()
        div.decompose()

md = convert_to_markdown(content)

with open(f'content/posts/{name}.md', 'w') as f:
    f.write("---\n")
    f.write(f"date: '{datetime}'\n")
    f.write(f"title: '{title}'\n")
    f.write("---\n")
    f.write("\n")
    f.write(md)
