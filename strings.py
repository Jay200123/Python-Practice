fname = 'Renyel Jay'
lname = 'Sioc'

print('Hello there!', fname, lname)

if fname == 'Renyel Jay':
    print('Welcome!', fname, lname)
else:
    print('Hello there Stranger!')
    
if isinstance(fname, str):
    print('data is a string')
else:
    print('data is not a string')