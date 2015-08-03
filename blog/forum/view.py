from flask import ( 
        render_template, 
        request, 
        Blueprint,
        url_for,
        redirect)

from blog.helpers.ext import db
from blog.models import User, Post, Comment 

forum = Blueprint("forum", __name__)

@forum.route("/")
def home():
    return render_template('layout.html', posts=posts)


@forum.route('/post')
def post_home():
    posts = []
    for post in Post.query.order_by(Post.created_at.desc()).all():
        print "forum: {} by {} ".format(post.title, post.writer.username)
        print "-" * 60
        print post.body
        print "-" * 60
        print "Upvotes: {}, DownVotes: {}".format(post.upvotes, post.downvotes)
        print "-" * 60
        comments = Comment.query.filter(Comment.postid == post.id).all()
        print "{} comments".format(len(comments))
        commentlist = []

        for comment in comments:
            print "   {}: {}".format(comment.author.username, comment.text) 
            commentlist.append(dict(commentedby=comment.author.username, text=comment.text))
        print 
        print "-" * 60
        posts.append(dict(postid=post.id, 
            title=post.title, 
            upvotes=post.upvotes, 
            downvotes=post.downvotes, 
            author=post.writer.username, 
            body=post.body,
            timestamp=post.created_at,
            comments=commentlist))

    return render_template('forum/index.html', posts=posts)
