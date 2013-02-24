# WebCrawler #

def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ""

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1: 
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)

def get_all_links(page):
    links = []
    while True:
        url,endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def crawl_web(seed,max_depth):
    tocrawl = [seed]
    crawled = []
    next_depth = []
    depth = 0
    while tocrawl and depth <= max_depth:
        page = tocrawl.pop()
        if page not in crawled:
            union(next_depth, get_all_links(get_page(page)))
            crawled.append(page)
        if not tocrawl:
            tocrawl, next_depth = next_depth, []
            depth = depth + 1
    return crawled

print crawl_web("http://xkcd.com/353", 1)

index = []

def add_to_index(index,keyword,url):
    for entry in index:
        if entry[0] == keyword:
			if not url in entry[1]:
				entry[1].append(url)
            return
    index.append([keyword,[url]])

def lookup(index,keyword):
	for entry in index:
		if entry[0] == keyword:
			return entry[1]
	return []

def add_page_to_index(index,url,content):
	for keyword in content.split():
		add_to_index(index,keyword,url)
