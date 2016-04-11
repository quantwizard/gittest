import httplib2


def main():
    http = httplib2.Http()
    url = "http://localhost:5555"
    url2 = "http://123.56.9.190:5555"
    body = "just test"
    for i in xrange(10):
        response, data = http.request(url2, 'GET', body=body)
        print response
        print data

if __name__ == '__main__':
    main()