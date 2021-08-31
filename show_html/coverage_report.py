from flask import Flask, render_template

# Create a flask app
app = Flask(
  __name__,
  template_folder='htmlcov',
  static_folder='static'
)

# Index page (now using the index.html file)
@app.route('/')
def index():
  return render_template('gilded_rose_test_py.html')

if __name__ == '__main__':
  # Run the Flask app
  app.run(
	host='0.0.0.0',
	debug=True,
	port=8080
  )
