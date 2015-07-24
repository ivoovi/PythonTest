import tornado.ioloop
from tornado.httpclient import AsyncHTTPClient
import bs4
import tornado.web


def handle_request(response):
    if response.error:
        print("Error:", response.error)
    else:
        for ele in [x.getText() for x in parse_response(response.body)]:
            print(ele)



def parse_response(body, selector=''):
    raw_html = bs4.BeautifulSoup(body)
    if selector == '':
        elements = raw_html.select('h2.title3')
        return elements
    else:
        elements = raw_html.select(selector)
        return elements


http_client = AsyncHTTPClient()
http_client.fetch('https://automatetheboringstuff.com/chapter11/', callback=handle_request)



print('next')

tornado.ioloop.IOLoop.instance().start()
