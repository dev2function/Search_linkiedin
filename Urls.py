def add_url(url):
    try:
        new_links = url
        with open('new_links.txt', 'r') as links:
            users = links.read()
        with open('new_links.txt', 'w') as li:
            new_links = str(users) + str(url)
            li.write(str(url))

    except IOError:
        with open('new_links.txt', 'w') as links:
            links.write(str(new_links))
    print(new_links)
