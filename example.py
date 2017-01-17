import DFA as d
mydfa = d.DFA('tokens')
mydfa.display_keywords()
print(mydfa.run('int'))
print(mydfa.run('for'))
print(mydfa.run('integer'))
print(mydfa.run('rohit'))
