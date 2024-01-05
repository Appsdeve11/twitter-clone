from flask import redirect, url_for, flash
from flask_login import logout_user

@app.route('/logout')
def logout():
    """Handle logout of user."""

    # Log the user out using Flask-Login's logout_user() function
    logout_user()

    # Flash a success message
    flash('You have been logged out successfully.', 'success')

    # Redirect the user to the login page
    return redirect(url_for('login'))