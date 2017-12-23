class HTMLRenderer:
    def start_paragraph(self):
        print('<p>')

    def end_paragraph(self):
        print('</p>')

    def sub_emphasis(self,match):
        return '<em>{}</em>'.format(match.group(1))

    def feed(self,data):
        print(data)

    
class Handler:
    def callback(self,prefix,name,*args):
        method = getattr(self, prefix+name, None)
        if callable(method):
            return method(*args)

    def start(self,name):
        self.callback('start_', name)
    
    def end(self,name):
        self.callback('end_',name)

    def sub(self,name):
        def substitution(match):
            result = self.callback('sub_',name,match)
            if result is None:
                result = match.group(0)
            return result
        return substitution
