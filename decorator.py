def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper


# @log('execute')  # 相当于now=log(now)
# def now():
#     print('2017-10-14')

@log('execute')  # 相当于now=log('execute')(now)
def now():
    print('2017-10-14')


f = now
f()
print(f.__name__)
