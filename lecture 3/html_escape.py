from functools import wraps, reduce

escapes = {
    '"':'&quot;',
    '<':'&lt;',
    '>':'&gt;',
    '&':'&amp;',
    }

def html_escape(func):
    @wraps(func)
    def change_escapes(txt):
       return reduce( lambda s, pair: s.replace(pair[0], pair[1]),
                      sorted(escapes.items(), key = lambda x: x[1]),
                      txt
                    )
    return change_escapes

@html_escape
def my_txt(txt):
    return txt

print(my_txt('<&dsad>"'))