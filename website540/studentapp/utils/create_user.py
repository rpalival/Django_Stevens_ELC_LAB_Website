from django.contrib.auth.models import User

# Create a new user
user = User.objects.create_user(username='rpalival', email='rajnpalival@gmail.com', password='rpalival')

# Save the user
user.save()