from flask import Flask, render_template, request, redirect, flash
from flask_login import current_user, login_required
from werkzeug.security import check_password_hash

app = Flask(__name__)

# Route for profile editing
@app.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    if request.method == 'POST':
        # Getting the form data
        username = request.form['username']
        email = request.form['email']
        image_url = request.form['image_url']
        header_image_url = request.form['header_image_url']
        bio = request.form['bio']
        password = request.form['password']

        # Checking if the password is valid
        if not check_password_hash(current_user.password, password):
            flash('Incorrect password. Please try again.', 'error')
            return redirect('/')

        # Update the user's profile
        current_user.username = username
        current_user.email = email
        current_user.profile.image_url = image_url
        current_user.profile.header_image_url = header_image_url
        current_user.profile.bio = bio

        # Save the changes 
        db.session.commit()

        # Redirect to the user detail page
        return redirect('/user-detail')

    return render_template('edit_profile.html')