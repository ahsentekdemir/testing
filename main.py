import httpx

class TEST:

    def __init__(self):
        self.url = 'http://cemaltiryaki.com'

    def get_content(self):
        return httpx.get(self.url).text

if __name__ == '__main__':
    run = TEST()
    print(run.get_content())
