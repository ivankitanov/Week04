from flask import Blueprint


course =Blueprint('user', __name__, template_folder='templates')

courses=["Python", "Maths", "English",]

@course.route('/')
def course_list():
    return render_template('index.html') 