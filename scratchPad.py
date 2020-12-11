a = '\'
b = '_'
for x in parameter:
    try:
        x.replace(a,b)
    except:
        pass
