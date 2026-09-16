from flask import Flask

app=Flask(__name__)

@app.route("/user/<username>")
def show_user_profile(username):
    return "User %s" % username

@app.route("/post/<int:post_id>")
def show_posr(post_id):
    return "post %d" % post_id


if __name__ == "__main__":
    app.run()