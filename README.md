# Web_Scraper

# CS600 Advanced Algorithms Project

This repository contains two main components:

1. **Online Version** — A Flask-based web application that scrapes any public HTML page for a keyword and displays its frequency.
2. **Offline Version** — A command-line search engine built from scratch using Trie data structures to index and search a set of local HTML files.

---

## Online Version: HTML Keyword Frequency Finder (Flask)

### Description

A lightweight web app that allows users to:

- Input a URL and a keyword.
- Scrape the contents of the webpage.
- Return whether the keyword exists and how many times it appears.

### Tech Stack

- Python
- Flask
- Requests
- BeautifulSoup

### Usage

#### 1. Install dependencies

```bash
pip install flask requests beautifulsoup4
