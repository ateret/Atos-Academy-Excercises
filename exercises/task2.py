def wow(number: int):
    os = ('o'*number)
    return('W'+os+'w')

assert wow(1) == 'Wow'
assert wow(4) == 'Woooow'
assert wow(0) == 'Ww'