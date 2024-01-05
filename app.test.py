import unittest
from flask import url_for
from app import app, db, User

class TestApp(unittest.TestCase):
    def setUp(self):
        """Set up the test environment."""
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        """Tear down the test environment."""
        db.session.remove()
        db.drop_all()

    def test_login_valid_credentials(self):
        """Test login with valid credentials."""
        user = User(username='testuser', password='testpassword')
        db.session.add(user)
        db.session.commit()

        response = self.app.post('/login', data=dict(
            username='testuser',
            password='testpassword'
        ), follow_redirects=True)

        self.assertIn(b'Hello, testuser!', response.data)

    def test_login_invalid_credentials(self):
        """Test login with invalid credentials."""
        response = self.app.post('/login', data=dict(
            username='testuser',
            password='wrongpassword'
        ), follow_redirects=True)

        self.assertIn(b'Invalid credentials.', response.data)

    def test_logout(self):
        """Test logout functionality."""
        response = self.app.get('/logout', follow_redirects=True)

        self.assertIn(b'You have been logged out successfully.', response.data)

    def test_list_users(self):
        """Test listing of users."""
        response = self.app.get('/users')

        self.assertEqual(response.status_code, 200)

    def test_user_profile(self):
        """Test user profile page."""
        user = User(username='testuser')
        db.session.add(user)
        db.session.commit()

        response = self.app.get(f'/users/{user.id}')

        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()