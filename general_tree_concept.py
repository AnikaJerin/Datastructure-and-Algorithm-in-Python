# TREE IS A RECURSIVE DATA STRUCTURE 

"""
->ELECTRONICS ITSELF A NODE
  -->DATA: ELECTRONICS
    --> CHILDREN = [LAPTIOP,CELL PHONE,TV]
      -->PARENT = NONE
-->LAPTOP,ITSELF A NODE                     -->CELL PHONE,ITSELF A NODE                   -->TV,ITSELF A NODE
  -->DATA:LAPTOP                              -->DATA:CELL PHONE                            -->DATA:TV
    -->CHILDREN:[MAC,SURFACE,THINKPAD]          -->CHILDREN:[IPHONE GOOGLE PIXEL,VIVO]        -->CHILDREN:[SAMSUNG,LG]
       (SIMILARLY EACH OF THESE CHILDREN IS ITSELF A NODE LIKE DATA:MAC,CHILDREN:[NONE],PARENT:LAPTOP)
      -->PARENT: ELECTRONICS                     --PARENT:ELECTRONICS                           -->PARENT:ELECTRONICS
"""


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    root.print_tree()

if __name__ == '__main__':
    build_product_tree()