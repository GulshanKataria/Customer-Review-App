
from flask import Flask,render_template,redirect,request,url_for,flash
from flask_sqlalchemy import SQLAlchemy
 
 
 
 
app=Flask(__name__,template_folder='templates')

app.secret_key = "Secret Key"
 
#SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/crud'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)
 
 
#Creating model table for our CRUD database
class Data(db.Model):
    user = db.Column(db.String(100) ,primary_key=True)
    nameofproduct = db.Column(db.String(100))
    productreview = db.Column(db.String(300))
    
 
 
    def __init__(self,user,nameofproduct,productreview):
        self.user=user
        self.nameofproduct=nameofproduct
        self.productreview=productreview
        
 
     
 
 
 
 
#This is the index route where we are going to
#query on all our employee data
@app.route('/')



def index():
    all_data = Data.query.all()
 
    return render_template("index.html", reviews = all_data)


@app.route('/insert', methods = ['POST'])
def insert():
 
    if request.method == 'POST':
 
        user = request.form['user']
        nop = request.form['nop']
        rop = request.form['rop']
 
 
        my_data = Data(user,nop,rop)
        db.session.add(my_data)
        db.session.commit()
 
        flash("Review added successfully")
 
        return redirect(url_for('index'))
 
if __name__=="__main__":
      app.run(debug=True)

