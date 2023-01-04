spins=[('red','18'),('black','13'),('red','7'),('red','5'),
       ('red','20'),('black','28'),('red','8'),('red','23'),
       ('black','30'),('black','13'),('black','36'),('black','3'),
       ('red','39')]
def countRed(alist):
    count=0
    for color,number in alist:
        if color=='black':
            yield count
            count=0
        else:
            count+=1
    yield count
gap=[gap for gap in countRed(spins)]
print(gap)
