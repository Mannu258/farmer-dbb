# save this as app.py
from flask import Flask,render_template,request
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config['SECRET_KEY'] = "12345"
db = SQLAlchemy(app)


admin = Admin(app, name='Farmer Details', template_mode='bootstrap3')

class Farmers(db.Model):
    ID = db.Column(db.Integer,primary_key=True)
    CITY = db.Column(db.String(200),nullable=False)
    Farmer_Code = db.Column(db.String(200),nullable=False)
    SCOPE =  db.Column(db.String(200),nullable=False)
    Farmer_Name = db.Column(db.String(200),nullable=False)
    Father_Husband =  db.Column(db.String(200),nullable=False)
    District =  db.Column(db.String(200),nullable=False)
    Block =  db.Column(db.String(200),nullable=False)
    Village =  db.Column(db.String(200),nullable=False)
    AADHAR =  db.Column(db.String(12),nullable=False)
    Mobile_No =  db.Column(db.String(10),nullable=False)
    Approx_Area_Ha =  db.Column(db.String(200),nullable=False)
    Est_YEILD =  db.Column(db.Integer,nullable=False)
    No_of_Sheep =  db.Column(db.Integer,nullable=False)
    Female = db.Column(db.Integer,nullable=False)
    Male = db.Column(db.Integer,nullable=False)
    Lamb = db.Column(db.Integer,nullable=False)


    def __repr__(self) -> str:
        return f"{self.s_no} - {self.title}"
class ItemView(ModelView):

    column_list = ('ID', 'Farmer_Code', 'Farmer_Name','Mobile_No','AADHAR') 
    column_searchable_list = ['Farmer_Code', 'Farmer_Name','Mobile_No','AADHAR']

admin.add_view(ItemView(Farmers, db.session))

@app.route("/", methods=['POST','GET'])
def index():
    if request.method == 'POST':
        code = request.form['value']  # Replace with the actual search term
        # Use a different variable name for the query result to avoid conflict
        farmer_results = Farmers.query.filter(
            (Farmers.CITY.ilike(f"%{code}%")) | 
            (Farmers.Mobile_No.ilike(f"%{code}%")) | 
            (Farmers.District.ilike(f"%{code}%")) | 
            (Farmers.AADHAR.ilike(f"%{code}%")) |
            (Farmers.SCOPE.ilike(f"%{code}%")) |
            (Farmers.Farmer_Code.ilike(f"%{code}%"))
        ).all()
        return render_template('index.html', Farmer=farmer_results)

    # Use a different variable name for the query result to avoid conflict
    all_farmers = Farmers.query.all()
    return render_template('index.html', Farmer=all_farmers)

@app.route("/Details/<int:ID>", methods=['POST','GET'])
def details(ID):
    Farmer = Farmers.query.filter_by(ID = ID)
    return render_template('Details.html',Farmer=Farmer)


if __name__ == '__main__':
   app.run(debug=True ,port=8000)
