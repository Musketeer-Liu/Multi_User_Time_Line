import webapp2

class MainPage(webapp2.ReuestHandler):
    def get(self):
        self.redirect('/blog')