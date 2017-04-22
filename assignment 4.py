import urllib

class ArrayStack:
    def ___init__(self):
        self._data =[]
    def __len__(self):
        return len(self._data)
    def is_empty(self):
        return len(self. _data)==0
    def push(self,e):
        self._data.append(e)
    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]
    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()



def is_matched_html(raw):
    S = ArrayStack
    j = raw.find("<")
    while j!=-1:
        k = raw.find('>',j+1)
        if k == -1:
            return False
        tag = raw[j+1:k]
        if not tag.startswith('/'):
            S.push(tag)
        else:
            if S.is_empty():
                return False
            if tag[1:]!=S.pop():
                return False
        j = raw.find('<',k+1)
    return S.is_empty()

link = "http://www.gutenberg.org/files/54560/54560-h/54560-h.htm"
html = urllib.urlopen(link)
raw = html.read()


