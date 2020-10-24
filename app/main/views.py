from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required,current_user
from ..models import User,Pitch,Comment
from .forms import UpdateProfile,PitchForm,CommentForm
from .. import db,photos
import markdown2  

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    pitches=Pitch.get_all_pitches()
   
    return render_template('index.html',pitches=pitches)

@main.route('/profile/<username>')
@login_required
def profile(username):

    '''
    View profile page function that returns the profile details of the current user logged in
    '''
    user = User.query.filter_by(username = username).first()
    
    if user is None:
        abort(404)
    pitches = Pitch.get_user_pitches(user.id)
    return render_template("profile/profile.html", user = user,pitches=pitches)    

@main.route('/profile/<username>/update',methods = ['GET','POST'])
@login_required
def update_profile(username):
    user = User.query.filter_by(username = username).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',username=user.username))

    return render_template('profile/update.html',user=user,form =form)



@main.route('/profile/<username>/update/pic',methods= ['POST'])
@login_required
def update_pic(username):
    user = User.query.filter_by(username = username).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.update_profile',username=username))    


@main.route('/pitch/new', methods = ['GET','POST'])
@login_required
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data
        category = form.category.data
        # Updated review instance
        new_pitch = Pitch(pitch_title=title,pitch_body=body,pitch_category=category,user=current_user)

        # save review method
        new_pitch.save_pitch()
        return redirect(url_for('.index'))

    title = 'New Pitch Form'
    return render_template('new_pitch.html',title = title, pitch_form=form)    


@main.route('/pitches/category/<category_name>')
@login_required
def pitch_by_category(category_name):

    '''
    View root page function that returns pitch category page with pitches from category selected
    '''
    pitches=Pitch.query.filter_by(pitch_category=category_name).order_by(Pitch.posted.desc()).all()
    
    return render_template('pitch_by_category.html',pitches=pitches,category=category_name)



@main.route('/pitch_details/<pitch_id>', methods = ['GET','POST'])
@login_required
def pitch_details(pitch_id):

    '''
    View pitch details function that returns pitch_details and comment form
    '''

    form = CommentForm()
    pitch=Pitch.query.get(pitch_id)
    comments=Comment.query.filter_by(pitch_id=pitch_id).order_by(Comment.posted.desc()).all()
    format_comments=[]
    if comments:
        for comment in comments:
            format_comments.append(markdown2.markdown(comment.comment,extras=["code-friendly", "fenced-code-blocks"]))
    
    if form.validate_on_submit():
        comment = form.comment.data
        
        # Updated comment instance
        new_comment = Comment(comment=comment,user=current_user,pitch=pitch)

        # save review method
        new_comment.save_comment()
        pitch.pitch_comments_count = pitch.pitch_comments_count+1

        db.session.add(pitch)
        db.session.commit()
        return redirect(url_for('main.pitch_details',pitch_id=pitch_id))

    return render_template('pitch_details.html',comment_form=form,pitch=pitch,comments=comments,format_comments=format_comments)

@main.route('/pitch_upvote/<pitch_id>')
@login_required
def pitch_upvote(pitch_id):
    '''
    View function to add do upvote on pitch click
    '''
    pitch=Pitch.query.get(pitch_id)
    pitch.pitch_upvotes=pitch.pitch_upvotes+1
    db.session.add(pitch)
    db.session.commit()  
    return redirect(url_for('main.pitch_details',pitch_id=pitch_id)) 


@main.route('/pitch_downvote/<pitch_id>')
@login_required
def pitch_downvote(pitch_id):
    '''
    View function to add do downvote on pitch click
    '''
    pitch=Pitch.query.get(pitch_id)
    pitch.pitch_downvotes=pitch.pitch_downvotes+1
    db.session.add(pitch)
    db.session.commit()  
    return redirect(url_for('main.pitch_details',pitch_id=pitch_id))         



    