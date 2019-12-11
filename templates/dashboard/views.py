# This is where the routes are defined. 
# It may be split into a package of its own (yourapp/views/) 
# with related views grouped together into modules.

from templates import app
from flask import render_template@app.route('/')

@app.route('/dashboard')
def index():
    return render_template("index.html")


# @app.route('/success', methods = ['POST'])  
# def success(): 
    
#     if request.method == 'POST':  
#         file = request.files['file']
#         if file:
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
#             train = training_models.trainer(filename)
#             session["filename"] = filename
#         return render_template('success.html', filename=filename, train=train )   


# @app.route("/results", methods = ['POST'])
# def results():
#     if request.method == 'POST': 
#         fileNamefromSuccess =session.get("filename",None)
#         train = training_models.trainer(fileNamefromSuccess)
#         #return render_template("results.html",fileNamefromSuccess=fileNamefromSuccess, train=train)
#     return  jsonify({'results': str(train)})

# # create route that renders about.html template
# @app.route("/about")
# def About():
#     return render_template("about.html")

# @app.route("/team")
# def Team():
#     return render_template("team.html")

#################################
# Notes
#################################
#We can identify a circular import between metricsdashboard/templates/__init__.py 
# and metricsdashboar/templates/hello/views.py, where, in the __init__.py, 
# we import views from the views.py, and in the views.py, 
# we import the app from the __init__.py. So, this actually makes 
# the two modules depend on each other.