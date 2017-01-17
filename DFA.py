import tree
class DFA(object):
    #root = tree.Node('start')
    def __init__(self,fname):
        self.root = tree.Node('start')
        lines = open(fname).readlines()
        self.keywords = []
        for line in lines:
            word = line.strip()
            if not word=='':
                self.keywords.append(word)
        for word in self.keywords:
            self.add_keyword(word)
    
    def display_keywords(self):
        for word in self.keywords:
            print(word)
        
        
    def add_keyword(self,keyword):
        cur_Node = self.root
        for letter in keyword:
            if letter not in cur_Node.children:
                temp = tree.Node(letter)
                cur_Node.add_child(temp)
                cur_Node = temp
            else:
                cur_Node = cur_Node.children[letter]
            
    
    def run(self,input):
        flag = 1
        length = len(input)
        counter = 0
        cur_Node = self.root
        while counter<length:
            if input[counter] in cur_Node.children:
                cur_Node = cur_Node.children[input[counter]]
                counter = counter+1
            else:
                flag = 0
                break
        if flag==1:
            return True
        else:
            return False
            
        
    
            
        
        
    
