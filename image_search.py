from img_search_engine import googleimagesdownload

def img_search(query, limit):
    arguments = {
        'keywords': query,
        'limit': limit,
        'print_urls': False,
        'silent_mode': True
    }

    response = googleimagesdownload()
    _, _, images = response.download(arguments)

    return images