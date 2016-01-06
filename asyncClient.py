from tornado import gen

@gen.coroutine
def fetch_coroutine(url):
    http_client = AsyncHTTPClient()
    response = yield http_client.fetch(url)
    print response
    raise gen.Return(response.body)

def main():
    url = "http://www.163.com"
    try:
        gen = fetch_coroutine(url)
    except gen.Return, result:
        print result

if __name__ == '__main__':
    main()