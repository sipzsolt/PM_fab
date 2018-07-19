from app import app
from app import views

views.run(host='0.0.0.0', port=8080, debug=True)

