import time
from blog_handler import BlogHandler
from models import Like
from utility import user_logged_in, post_exists

class LikeButton(BlogHandler):
    @user_logged_in
    @post_exists
    def post(self, post):
        like_button = self.request.get('like_button')
        like = self.user.user_likes.filter("post =", post).get()
        if like_button == 'like' and not like:
            like = Like.create(self.user, post)
            like.put()
        elif like_button =='unlike' and like:
            like.delete()
        time.sleep(0.1)
        self.redirect('/blog/' + str(post.key().id()))