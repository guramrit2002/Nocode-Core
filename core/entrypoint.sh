# Run migrations
echo "🚀 Running migrations..."
python manage.py migrate account admin auth contenttypes sessions socialaccount

# Create superuser if not exists
echo "👤 Checking for superuser..."
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')
    print("✅ Superuser created.")
else:
    print("ℹ️ Superuser already exists.")
EOF

# Start server
echo "🟢 Starting Django..."
python manage.py runserver 0.0.0.0:8000
