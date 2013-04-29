class Sort_Tag:

    def __init__(self, name, tag_n, count):
        self.name = name
        self.tag_n = tag_n
        self.count = count

    def __repr__(self):
        return repr((self.name, self.tag_n, self.count))


sort_tag = Sort_Tag('ysyong', 12, 98)
print sort_tag.name
print sort_tag.tag_n
print sort_tag.count
