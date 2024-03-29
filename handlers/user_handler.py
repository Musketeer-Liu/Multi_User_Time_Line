from blog_handler import BlogHandler
from models import User
from utility import valid_email, valid_password, valid_username

class Signup(BlogHandler):
    def get(self):
        self.render("signup.html")

    def post(self):
        self.username = self.request.get("username")
        self.password = self.request.get("password")
        self.verify = self.request.get("verify")
        self.email = self.request.get("email")

        params = dict(username=self.username, email=self.email)
        passed = True

        if not valid_username(self.username):
            params["error_username"] = "Invalid username!"
            passed = False
        else:
            user = User.by_name(self.username)
            if user:
                params["error_username"] = "User already exists!"
                passed = False

        if not valid_username(self.password):
            params["error_password"] = "Invalid password!"
            passed = False
        elif self.password != self.verify:
                params["error_verifyl"] = "Passwords not match!"
                passed = False

        if self.email and not valid_email(self.email):
            params["error_email"] = "Invalid email!"
            passed = False

        if passed:
            user = User.signup(self.username, self.password, self.email)
            user.put()
            self.login(user)
            self.redirect('/welcome')
        else:
            self.render("signup.html", **params)

class Welcome(BlogHandler):
    def get(self):
        if self.user:
            username = self.user.name
            self.render("welcome.html", username=username)
        else:
            self.redirect('/signup')

class Login(BlogHandler):
    def get (self):
        self.render("login.html")

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        user = User.login(username, password)
        if user:
            self.login(user)
            self.redirect('/welcome')
        else:
            self.render("login.html",
                        error="Username and password not match")

class Logout(BlogHandler):
    def get(self):
        self.logout()
        self.redirect('/signup')