class Node:
    def __init__(self, t, text):
        self.type = t
        self.text = text
        self.link = []

    def get_text(self):
        return self.text
    def set_text(self, text):
        self.text = text
    def get_type(self):
        return self.type
    def set_type(self, typo):
        self.type = typo
    def get_link(self):
        return self.link
    def set_link(self, link):
        self.link.append(link)
