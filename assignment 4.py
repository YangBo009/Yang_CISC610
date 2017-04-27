class Empty(Exception):
    pass
class ArrayStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def push(self, item):
        self._data.append(item)

    def isEmpty(self):
        return (self._data == [])

    def top(self):
        if self.isEmpty():
            raise Empty('Stack is empty')
            return self._data[-1]
    def pop(self):
        if self.isEmpty():
            raise Empty('Stack is empty')
        return self._data.pop()


def is_matched_html(raw):
    s = ArrayStack()
    j = raw.find("<")
    while j != -1:
        k = raw.find('>',j+1)
        if k == -1:
            return False
        tag = raw[j+1:k]
        if not tag.startswith('/'):
            s.push(tag)
        else:
            if s.isEmpty():
                return False
            if tag[1:]!=s.pop():
                return False
        j = raw.find('<',k+1)
    return s.isEmpty()

Hstr = '<center><h1> Let us to work hard </h1> </center>'
if is_matched_html(Hstr)== False:
    print "False"
else:
    print "True"




