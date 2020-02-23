#!/usr/bin/env python3
# -*- coding: utf-8 -*-
try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass
# end try


def main():
    from .core import start_app
    start_app()
# end def

def search(search_string):
    from .core import start_app_module
    import requests

    requests.urllib3.disable_warnings(
        requests.urllib3.exceptions.InsecureRequestWarning)

    app = start_app_module()
    app.initialize()

    app.user_input = search_string
    app.init_search()
    app.search_novel()

    return app.search_results
# end def

def get_novel_info(novel_url):
    from .core import start_app_module
    import requests

    requests.urllib3.disable_warnings(
        requests.urllib3.exceptions.InsecureRequestWarning)

    app = start_app_module()
    app.initialize()
    app.init_crawler(novel_url)

    if not app.crawler:
        raise Exception('No crawler initialized')
    app.get_novel_info()

    if len(app.crawler.volumes) == 0:
        raise Exception('Empty volume list')
    # end if

    if len(app.crawler.chapters) == 0:
        raise Exception('Empty chapter list')
    # end if

    return {'title': app.crawler.novel_title, 'cover': app.crawler.novel_cover, 'author': app.crawler.novel_author, 'chapters': app.crawler.chapters, 'volumes': app.crawler.volumes}
# end def
