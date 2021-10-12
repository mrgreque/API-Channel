class Video:

    def __init__(self, titulo, views, href):
        self.titulo = titulo
        self.views = views
        self.href = href

    def export(self):
        return {'titulo': self.titulo, 'views': self.views, 'href': self.href}