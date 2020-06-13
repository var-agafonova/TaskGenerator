import node

class LGraph:
    def __init__(self):
        self.nodes = dict()
        self.nodes[0] = node.Node("begin", "")
        self.numb = 1

    def add_node(self, typo, code, pred):
        for i in pred:
            self.nodes[i].set_link(self.numb)
        self.nodes[self.numb] = node.Node(typo, code)
        self.numb += 1

    def get_node(self, node):
        return self.nodes[node]

    def end(self, node):
        return not self.nodes[node].get_link()

        def len(self):
            return len(self.nodes)
