class SearchGoogle:
    def __init__(self, query):
        self.query = query
    
    def search(self):
        from googlesearch import search
        # results=[]
        # for i in search(self.query,lang='en',num=5,stop=5,pause=1.0):
        #     results.append(i)
        return search(self.query,lang='en',num=5,stop=5,pause=1.0)