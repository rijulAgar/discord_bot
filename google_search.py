class SearchGoogle:
    def __init__(self, query,num=5):
        self.query = query
        self.num = num
    
    def search(self):
        from googlesearch import search
        return search(self.query,lang='en',num=self.num,stop=5,pause=1.0)