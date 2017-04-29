import webapp2

from handlers import *

app = webapp2.WSGIApplication([('/', BlogFront),
                               ('/blog/?', BlogFront),
                               ('/blog/([0-9]+)', PostPage),
                               ('/blog/newpost', NewPost),
                               ('/blog/([0-9]+)/edit', EditPost),
                               ('/blog/([0-9]+)/delete', DeletePost),
                               ('/blog/([0-9]+)/comment/newcomment', NewComment),
                               ('/blog/([0-9]+)/comment/([0-9]+)/edit', EditComment),
                               ('/blog/([0-9]+)/comment/([0-9]+)/delete', DeleteComment),
                               ('/blog/([0-9]+)/like', LikeButton),
                               ('/weclome', Welcome),
                               ('/signup', Signup),
                               ('/login', Login),
                               ('/logout', Logout),
                               ],
                              debug=True)