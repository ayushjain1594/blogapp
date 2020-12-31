from flask import render_template, request, Blueprint
from blogapp.models import Post, User

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
	page = request.args.get('page', 1, type=int)
	posts = Post.query.order_by(Post.date_posted.desc()
		).paginate(page=page, per_page=5)
	topusers = User.query.limit(5).all()
	return render_template('home.html', posts=posts, topusers=topusers)

@main.route("/about")
def about():
	return render_template('about.html', title='About')
