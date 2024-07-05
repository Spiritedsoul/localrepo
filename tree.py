class treenode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None
    def add_child(self,child):
        child.parent=self
        self.children.append(child)

    def get_level(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent
        return level

    def print_tree(self):
        spaces=' '*self.get_level()*3
        prefix=spaces+'|--' if self.parent else ""
        print(prefix+self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

def build_product_tree():
    root=treenode('Electronics')

    laptop=treenode("laptop")
    laptop.add_child(treenode('mac'))
    laptop.add_child(treenode('windows'))
    laptop.add_child(treenode('linux'))

    cellphone=treenode("Cell phone")
    cellphone.add_child(treenode('redmi'))
    cellphone.add_child(treenode('iphone'))
    cellphone.add_child(treenode('vivo'))

    root.add_child(laptop)
    root.add_child(cellphone)
    #print(laptop.get_level())
    return root

if __name__=='__main__':
    root=build_product_tree()
    #print(root.get_level())
    root.print_tree()


