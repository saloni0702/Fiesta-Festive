import os
import datetime
import secrets
from sqlalchemy.exc import IntegrityError
from flask import Flask, render_template, flash,redirect, url_for, request ,session
from festival.forms import RegistrationForm, LoginForm, ForgetForm, FestivalSelection, AddproductForm, RemoveproductForm, AdminForm, Bikeform, ValidationForm
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager,login_user,current_user,logout_user
from flask_bcrypt import Bcrypt
import smtplib
import sqlite3
from flask_mail import Mail, Message
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from datetime import date




app= Flask(__name__,template_folder='template')
app.config['Mail_SERVER']='smtp.googlemail.com'
app.config['Mail_PORT']=587
app.config['Mail_USE_TLS']=True
token='eyJhbGciOiJIUzUxMiIsImlhdCI6MTU5OTEyNzY1MywiZXhwIjoxNTk5MTI3NjgzfQ.eyJ1c2VyX2lkIjoxfQ.SNfr7ggQfeaHv5du_cWtZv5du9PxqCWuKjVCYMmxzzN4TtiB2581AYIkL1n6cVNscACAHOqrWo71AMdHXqK2Hg'
mail=Mail(app)



app.config['SECRET_KEY']='7025eeaa16af636e4028ddcc624e254b'
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feast.db'
db=SQLAlchemy(app)
login_manager = LoginManager(app)
bcrypt=Bcrypt(app)
from database import Admin,Customer,Vendor,Service,Holi,Diwali,Navratri,Janmashtmi,Ganeshchaturthi,Rakshabandhan,Uttrayan,Newyear,Christmas,Servicedetail
login_manager.login_message_category='info'


@app.route("/")
def n():
	return  render_template('n.html')


@app.route("/home",methods=['GET','POST'])
def home():
	form=FestivalSelection()
	if form.validate_on_submit():
		if form.Festival.data=='0':
			return redirect(url_for('diwali'))
		if form.Festival.data=='1':
			return redirect(url_for('holi'))
		if form.Festival.data=='2':
			return redirect(url_for('uttrayan'))
		if form.Festival.data=='4':
			return redirect(url_for('rakshabandhan'))
		if form.Festival.data=='5':
			return redirect(url_for('janmashtmi'))
		if form.Festival.data=='6':
			return redirect(url_for('ganeshchaturthi'))
		if form.Festival.data=='7':
			return redirect(url_for('navratri'))
		if form.Festival.data=='8':
			return redirect(url_for('christmas'))
		if form.Festival.data=='9':
			return redirect(url_for('newyear'))
	return render_template('home.html',title='home',form=form)

@app.route("/home1",methods=['GET','POST'])
def home1():
	form=FestivalSelection()
	if form.validate_on_submit():
		if form.Festival.data=='0':
			return redirect(url_for('diwali'))
		if form.Festival.data=='1':
			return redirect(url_for('holi'))
		if form.Festival.data=='2':
			return redirect(url_for('uttrayan'))
		if form.Festival.data=='4':
			return redirect(url_for('rakshabandhan'))
		if form.Festival.data=='5':
			return redirect(url_for('janmashtmi'))
		if form.Festival.data=='6':
			return redirect(url_for('ganeshchaturthi'))
		if form.Festival.data=='7':
			return redirect(url_for('navratri'))
		if form.Festival.data=='8':
			return redirect(url_for('christmas'))
		if form.Festival.data=='9':
			return redirect(url_for('newyear'))
	return render_template('home1.html',title='home1',form=form)

@app.route('/diwali/<int:id>')
def single_page1(id):
	product = Diwali.query.get_or_404(id)
	return render_template('single_page1.html',products=product)

@app.route('/holi/<int:id>')
def single_page4(id):
	product=Holi.query.get_or_404(id)
	return render_template('single_page4.html',products=product)

@app.route('/uttrayan/<int:id>')
def single_page9(id):
	product=Uttrayan.query.get_or_404(id)
	return render_template('single_page9.html',products=product)

@app.route('/rakshabandhan/<int:id>')
def single_page8(id):
	product=Rakshabandhan.query.get_or_404(id)
	return render_template('single_page8.html',products=product)

@app.route('/janmashtmi/<int:id>')
def single_page5(id):
	product=Janmashtmi.query.get_or_404(id)
	return render_template('single_page5.html',products=product)

@app.route('/ganeshchaturthi/<int:id>')
def single_page3(id):
	product=Ganeshchaturthi.query.get_or_404(id)
	return render_template('single_page3.html',products=product)

@app.route('/navratri/<int:id>')
def single_page6(id):
	product=Navratri.query.get_or_404(id)
	return render_template('single_page6.html',products=product)

@app.route('/christmas/<int:id>')
def single_page2(id):
	product=Christmas.query.get_or_404(id)
	return render_template('single_page2.html',products=product)

@app.route('/newyear/<int:id>')
def single_page7(id):
	product=Newyear.query.get_or_404(id)
	return render_template('single_page7.html',products=product)

@app.route("/diwali")
def diwali():
	return render_template('diwali.html',products=Diwali.query.all())

def MagerDicts(dict1,dict2):
	if isinstance (dict1,list) and isinstance(dict2,list):
		returndict1+dict2
	elif isinstance(dict1,dict) and isinstance(dict2,dict):
		return dict(list(dict1.items())+list(dict2.items()))
	return False

@app.route('/addcart',methods=['POST'])

def AddCart():
	try:
		product_id=request.form.get('product_id')
		quantity=request.form.get('quantity')
		onsubmit=request.form.get('onsubmit')
		if onsubmit=='1':
			product = Diwali.query.filter_by(id=product_id).first()
		elif onsubmit=='2':
			product = Christmas.query.filter_by(id=product_id).first()
		elif onsubmit=='3':
			product = Ganeshchaturthi.query.filter_by(id=product_id).first()
		elif onsubmit=='4':
			product = Holi.query.filter_by(id=product_id).first()
		elif onsubmit=='5':
			product = Janmashtmi.query.filter_by(id=product_id).first()
		elif onsubmit=='6':
			product = Navratri.query.filter_by(id=product_id).first()
		elif onsubmit=='7':
			product = Newyear.query.filter_by(id=product_id).first()
		elif onsubmit=='8':
			product = Rakshabandhan.query.filter_by(id=product_id).first()
		elif onsubmit=='9':
			product = Uttrayan.query.filter_by(id=product_id).first()
		if product_id and quantity and request.method=="POST":
			DictItems={product_id:{'name':product.name ,'price':product.price, 'quantity':quantity ,'image':product.image}}
			if 'Shoppingcart' in session:
				print(session['Shoppingcart'])
				if product_id in session['Shoppingcart']:
					for key, item in session['Shoppingcart'].items():
						if int(key)==int(product_id):
							session.modified=True
							item['quantity']+=1
				else:
					session['Shoppingcart']=MagerDicts(session['Shoppingcart'],DictItems)
					return redirect(request.referrer)
			else:
				session['Shoppingcart']=DictItems
				return redirect(request.referrer)

	except Exception as e:
		print(e)
	finally:
		return redirect(request.referrer)

@app.route('/carts')
def getcart():
	if 'Shoppingcart' not in session and len(session['Shoppingcart'])<=0:
		return redirect(url_for('home1'))
	subtotal=0
	grandtotal=0
	tax=0
	for key, product in session['Shoppingcart'].items():
		subtotal+=float(product['price'])*int(product['quantity'])
		tax=("%.2f" % (0.01*float(subtotal)))
		grandtotal=float("%.2f"%(1.01*subtotal))


	return render_template('carts.html',tax=tax,grandtotal=grandtotal)




@app.route('/updatecart/<int:code>',methods=['POST'])
def updatecart(code):
	if 'Shoppingcart' not in session and len(session['Shoppingcart'])<=0:
		return redirect(url_for('home1'))
	if request.method=="POST":
		quantity=request.form.get('quantity')
		try:
			session.modified=True
			for key, item in session['Shoppingcart'].items():
				if int(key)==code:
					item['quantity']=quantity
					return redirect(url_for('getcart'))
		except Exception as e:
			print(e)
			return redirect(url_for('getcart'))

@app.route('/deleteitem/<int:id>')
def deleteitem(id):
	if 'Shoppingcart' not in session and len(session['Shoppingcart'])<=0:
		return redirect(url_for('home1'))
	try:
		session.modified=True
		for key, item in session['Shoppingcart'].items():
			if int(key)==id:
				session['Shoppingcart'].pop(key,None)
				return redirect(url_for('getcart'))
	except Exception as e:
		print(e)
		return redirect(url_for('getcart'))


@app.route('/final',methods=['GET','POST'])
def final():
	form=ValidationForm()
	if form.validate_on_submit():
		cus = Customer.query.filter_by(username=form.username.data).first()
		if cus:
			if cus.password == form.password.data:
				email=cus.email
				message="your order successfully registered!!"
				server = smtplib.SMTP('smtp.gmail.com:587')
				server.ehlo()
				server.starttls()
				server.login("abcfest2020@gmail.com","fest2020q")
				server.sendmail("abcfest2020@gmail.com",email,message)
				return redirect(url_for("success"))
			else:
				flash(f'Login Unsuccess, Check username & password!!!','danger')
				return redirect(url_for("final"))
		else:
			flash(f'you are not register plz Registration yourself')
			return redirect(url_for("register"))

	return render_template('final.html',form=form)

@app.route('/success')
def success():
	return render_template('success.html')

@app.route("/holi")
def holi():
	return render_template('holi.html',products=Holi.query.all())

@app.route("/uttrayan")
def uttrayan():
	return render_template('uttrayan.html',products=Uttrayan.query.all())


@app.route("/rakshabandhan")
def rakshabandhan():
	return render_template('rakshabandhan.html',products=Rakshabandhan.query.all())

@app.route("/janmashtmi")
def janmashtmi():
	return render_template('janmashtmi.html',products=Janmashtmi.query.all())

@app.route("/ganeshchaturthi")
def ganeshchaturthi():
	return render_template('ganeshchaturthi.html',products=Ganeshchaturthi.query.all())

@app.route("/navratri")
def navratri():
	return render_template('navratri.html',products=Navratri.query.all())

@app.route("/christmas")
def christmas():
	return render_template('christmas.html',products = Christmas.query.all())

@app.route("/newyear")
def newyear():
	return render_template('newyear.html',products=Newyear.query.all())


@app.route("/navratriimp")
def navimp():
	return render_template('navratriimp.html')

@app.route("/christmasimp")
def chriimp():
	return render_template('christmasimp.html')

@app.route("/diwaliimp")
def diwimp():
	return render_template('diwaliimp.html')

@app.route("/uttrayanimp")
def uttimp():
	return render_template('uttrayanimp.html')

@app.route("/holiimp")
def holiimp():
	return render_template('holiimp.html')

@app.route("/janmashtmiimp")
def janimp():
	return render_template('janmashtmiimp.html')

@app.route("/ganeshimp")
def ganimp():
	return render_template('ganeshimp.html')

@app.route("/newyearimp")
def newimp():
	return render_template('newyearimp.html')

@app.route("/rakhiimp")
def rakhiimp():
	return render_template('rakhiimp.html')


@app.route("/about",methods=['GET','POST'])
def about():
	form=AdminForm()
	if form.validate_on_submit():
		adm = Admin.query.filter_by(username=form.username.data).first()
		if adm:
			if adm.password==form.password.data:
				return redirect(url_for('admin'))
			else:
				flash(f'Check your username and password')
				return redirect(url_for('about'))
		else:
			flash(f'you are not admin,Access Denied!!!')

	return render_template('about.html',title='About',form=form)



@app.route("/admin")
def admin():
	return render_template('admin.html')

@app.route("/function")

def function():
	return render_template('function.html')

@app.route("/detail")

def detail():
	return render_template('detail.html')


@app.route("/register", methods=['GET','POST'])
def register():
	form=RegistrationForm()
	if form.validate_on_submit():
		if(form.example.data=='0'):
			ven = Vendor.query.filter_by(username=form.username.data).first()
			if ven:
				flash(f'Please use another username because it is already exist','danger')
				return redirect(url_for('register'))
			else:
				ven = Vendor(username = form.username.data,name = form.name.data,email = form.email.data,houseno=form.House_no.data,area=form.Area.data,taluka=form.Taluka.data,district=form.District.data,pincode = form.pincode.data,PhoneNumber = form.PhoneNumber.data,password =form.password.data)
				db.session.add(ven)
				try:
					db.session.commit()
					print("\n ")
					flash(f'Account created for {form.username.data}!','success')
					email=request.form.get("email")
					message="you have successfully registered!!"
					server = smtplib.SMTP('smtp.gmail.com:587')
					server.ehlo()
					server.starttls()
					server.login("abcfest2020@gmail.com","fest2020q")
					server.sendmail("abcfest2020@gmail.com",email,message)
					return redirect(url_for('login'))
				except IntegrityError:
					flash(f'Please use another username because it is already exist','danger')
		if(form.example.data=='1'):
			cus = Customer.query.filter_by(username=form.username.data).first()
			if cus:
				flash(f'Please use another username because it is already exist','danger')
				return redirect(url_for('register'))
			else:
				cus = Customer(username = form.username.data,name = form.name.data,email = form.email.data,houseno=form.House_no.data,area=form.Area.data,taluka=form.Taluka.data,district=form.District.data,pincode = form.pincode.data,PhoneNumber = form.PhoneNumber.data,password =form.password.data)
				db.session.add(cus)
				try:
					db.session.commit()
					print("\n ")
					flash(f'Account created for {form.username.data}!','success')
					email=request.form.get("email")
					message="you have successfully registered!!"
					server = smtplib.SMTP('smtp.gmail.com:587')
					server.ehlo()
					server.starttls()
					server.login("abcfest2020@gmail.com","fest2020q")
					server.sendmail("abcfest2020@gmail.com",email,message)
					return redirect(url_for('login'))
				except IntegrityError:
					flash(f'Please use another username because it is already exist','danger')
		if(form.example.data=='2'):
			ser = Service.query.filter_by(username=form.username.data).first()
			if ser:
				flash(f'Please use another username because it is already exist','danger')
				return redirect(url_for('register'))
			else:
				ser = Service(username = form.username.data,name = form.name.data,email = form.email.data,houseno=form.House_no.data,area=form.Area.data,taluka=form.Taluka.data,district=form.District.data,pincode = form.pincode.data,PhoneNumber = form.PhoneNumber.data,password =form.password.data)
				db.session.add(ser)
				try:
					db.session.commit()
					print("\n ")
					flash(f'Account created for {form.username.data}!','success')
					email=request.form.get("email")
					message="you have successfully registered!!"
					server = smtplib.SMTP('smtp.gmail.com:587')
					server.ehlo()
					server.starttls()
					server.login("abcfest2020@gmail.com","fest2020q")
					server.sendmail("abcfest2020@gmail.com",email,message)
					return redirect(url_for('login'))
				except IntegrityError:
					flash(f'Please use another username because it is already exist','success')



	return render_template('register.html',title='Register',form=form)



@app.route("/login", methods=['GET','POST'])
def login():
	form=LoginForm()
	if form.validate_on_submit():
		if form.example.data=='0':
			ven = Vendor.query.filter_by(username=form.username.data).first()
			if ven:
				if ven.password == form.password.data:
					login_user(ven,remember=form.remember.data)
					return redirect(url_for("function"))
				else:
					flash(f'Login Unsuccess, Check username & password!!!','danger')
			else:
				flash(f'you are not register plz Registration yourself')
				return redirect(url_for("register"))
		if form.example.data=='1':
			cus = Customer.query.filter_by(username=form.username.data).first()
			if cus:
				if cus.password == form.password.data:
					login_user(cus,remember=form.remember.data)
					return redirect(url_for("home1"))
				else:
					flash(f'Login Unsuccess, Check username & password!!!','danger')
			else:
				flash(f'you are not register plz Registration yourself')
				return redirect(url_for("register"))
		if form.example.data=='2':
			ser = Service.query.filter_by(username=form.username.data).first()
			if ser:
				if ser.password == form.password.data:
					login_user(ser,remember=form.remember.data)
					return redirect(url_for("detail"))
				else:
					flash(f'Login Unsuccess, Check username & password!!!','danger')
			else:
				flash(f'you are not register plz Registration yourself')
				return redirect(url_for("register"))

	return render_template('login.html',title='login',form=form)


@app.route("/forget", methods=['GET','POST'])
def forget():
	form=ForgetForm()
	if form.validate_on_submit():
		if form.example.data=='0':
			ven = Vendor.query.filter_by(username=form.username.data).first()
			if ven.username == form.username.data:
				ven.password = form.password.data
				db.session.commit()
				flash(f'your password is changed','success')
				return redirect(url_for("login"))
			else:
				flash(f'your Account is not available please create your Account','danger')
		if form.example.data=='1':
			cus = Customer.query.filter_by(username=form.username.data).first()
			if cus.username == form.username.data:
				cus.password = form.password.data
				db.session.commit()
				flash(f'your password is changed','success')
				return redirect(url_for("login"))
			else:
				flash(f'your Account is not available please create your Account','danger')
		if form.example.data=='2':
			ser = Service.query.filter_by(username=form.username.data).first()
			if ser.username == form.username.data:
				ser.password = form.password.data
				db.session.commit()
				flash(f'your password is changed')
				return redirect(url_for("login"))
			else:
				flash(f'your Account is not available please create your Account','danger')

	return render_template('forget.html',title='forget',form=form)

def save_image(form_image):
	random_hex = secrets.token_hex(10)
	_,f_ext = os.path.splitext(form_image.filename)
	image_fn = random_hex + f_ext
	image_path = os.path.join(app.root_path,'static', image_fn)
	form_image.save(image_path)

	return image_fn

@app.route("/addproduct",methods=['GET','POST'])

def addproduct():
	form=AddproductForm()
	if form.validate_on_submit():
		ven = Vendor.query.filter_by(username=form.username.data).first()
		if ven:
			if form.festival.data=='diwali':
				pro = Diwali.query.filter_by(name=form.product_name.data).first()
				if pro:
					flash(f'this product is already exist')
				else:
					if form.image.data:
						image_file = save_image(form.image.data)
						pro = Diwali(image=image_file,name = form.product_name.data,types=form.product_type.data,category=form.categories.data,price = form.price.data,companyname=form.company_name.data,quantity=form.quantity.data,detail=form.product_detail.data,username=form.username.data)
						db.session.add(pro)
						try:
							db.session.commit()
							flash(f'your product added successfully!!',"success")
							email=ven.email
							msg1="you have successfully added a product!!"
							server = smtplib.SMTP('smtp.gmail.com:587')
							server.ehlo()
							server.starttls()
							server.login("abcfest2020@gmail.com","fest2020")
							server.sendmail("abcfest2020@gmail.com",email,msg1)
							return redirect(url_for("function"))
						except IntegrityError:
							flash(f'error')
			if form.festival.data=='holi':
				pro = Holi.query.filter_by(name=form.product_name.data).first()
				if pro:
					flash(f'this product is already exist')
				else:
					if form.image.data:
						image_file = save_image(form.image.data)
						pro = Holi(image=image_file,name = form.product_name.data,types=form.product_type.data,category=form.categories.data,price = form.price.data,companyname=form.company_name.data,quantity=form.quantity.data,detail=form.product_detail.data,username=form.username.data)
						db.session.add(pro)
						try:
							db.session.commit()
							flash(f'your product added successfully!!',"success")
							email=ven.email
							msg1="you have successfully added a product!!"
							server = smtplib.SMTP('smtp.gmail.com:587')
							server.ehlo()
							server.starttls()
							server.login("abcfest2020@gmail.com","fest2020")
							server.sendmail("abcfest2020@gmail.com",email,msg1)
							return redirect(url_for("function"))
						except IntegrityError:
							flash(f'error')
			if form.festival.data=='uttrayan':
				pro = Uttrayan.query.filter_by(name=form.product_name.data).first()
				if pro:
					flash(f'this product is already exist')
				else:
					if form.image.data:
						image_file = save_image(form.image.data)
						pro = Uttrayan(image=image_file,name = form.product_name.data,types=form.product_type.data,category=form.categories.data,price = form.price.data,companyname=form.company_name.data,quantity=form.quantity.data,detail=form.product_detail.data,username=form.username.data)
						db.session.add(pro)
						try:
							db.session.commit()
							flash(f'your product added successfully!!',"success")
							email=ven.email
							msg1="you have successfully added a product!!"
							server = smtplib.SMTP('smtp.gmail.com:587')
							server.ehlo()
							server.starttls()
							server.login("abcfest2020@gmail.com","fest2020")
							server.sendmail("abcfest2020@gmail.com",email,msg1)
							return redirect(url_for("function"))
						except IntegrityError:
							flash(f'error')
			if form.festival.data=='rakshabandhan':
				pro = Rakshabandhan.query.filter_by(name=form.product_name.data).first()
				if pro:
					flash(f'this product is already exist')
				else:
					if form.image.data:
						image_file = save_image(form.image.data)
						pro = Rakshabandhan(image=image_file,name = form.product_name.data,types=form.product_type.data,category=form.categories.data,price = form.price.data,companyname=form.company_name.data,quantity=form.quantity.data,detail=form.product_detail.data,username=form.username.data)
						db.session.add(pro)
						try:
							db.session.commit()
							flash(f'your product added successfully!!',"success")
							email=ven.email
							msg1="you have successfully added a product!!"
							server = smtplib.SMTP('smtp.gmail.com:587')
							server.ehlo()
							server.starttls()
							server.login("abcfest2020@gmail.com","fest2020")
							server.sendmail("abcfest2020@gmail.com",email,msg1)
							return redirect(url_for("function"))
						except IntegrityError:
							flash(f'error')
			if form.festival.data=='janmashtmi':
				pro = Janmashtmi.query.filter_by(name=form.product_name.data).first()
				if pro:
					flash(f'this product is already exist')
				else:
					if form.image.data:
						image_file = save_image(form.image.data)
						pro = Janmashtmi(image=image_file,name = form.product_name.data,types=form.product_type.data,category=form.categories.data,price = form.price.data,companyname=form.company_name.data,quantity=form.quantity.data,detail=form.product_detail.data,username=form.username.data)
						db.session.add(pro)
						try:
							db.session.commit()
							flash(f'your product added successfully!!',"success")
							email=ven.email

							msg1="you have successfully added a product!!"
							server = smtplib.SMTP('smtp.gmail.com:587')
							server.ehlo()
							server.starttls()
							server.login("abcfest2020@gmail.com","fest2020")
							server.sendmail("abcfest2020@gmail.com",email,msg1)
							return redirect(url_for("function"))
						except IntegrityError:
							flash(f'error')
			if form.festival.data=='ganeshchaturthi':
				pro = Ganeshchaturthi.query.filter_by(name=form.product_name.data).first()
				if pro:
					flash(f'this product is already exist')
				else:
					if form.image.data:
						image_file = save_image(form.image.data)
						pro = Ganeshchaturthi(image=image_file,name = form.product_name.data,types=form.product_type.data,category=form.categories.data,price = form.price.data,companyname=form.company_name.data,quantity=form.quantity.data,detail=form.product_detail.data,username=form.username.data)
						db.session.add(pro)
						try:
							db.session.commit()
							flash(f'your product added successfully!!',"success")
							email=ven.email
							msg1="you have successfully added a product!!"
							server = smtplib.SMTP('smtp.gmail.com:587')
							server.ehlo()
							server.starttls()
							server.login("abcfest2020@gmail.com","fest2020")
							server.sendmail("abcfest2020@gmail.com",email,msg1)
							return redirect(url_for("function"))
						except IntegrityError:
							flash(f'error')
			if form.festival.data=='navratri':
				pro = Navratri.query.filter_by(name=form.product_name.data).first()
				if pro:
					flash(f'this product is already exist')
				else:
					if form.image.data:
						image_file = save_image(form.image.data)
						pro = Navratri(image=image_file,name = form.product_name.data,types=form.product_type.data,category=form.categories.data,price = form.price.data,companyname=form.company_name.data,quantity=form.quantity.data,detail=form.product_detail.data,username=form.username.data)
						db.session.add(pro)
						try:
							db.session.commit()
							flash(f'your product added successfully!!',"success")
							email=ven.email
							msg1="you have successfully added a product!!"
							server = smtplib.SMTP('smtp.gmail.com:587')
							server.ehlo()
							server.starttls()
							server.login("abcfest2020@gmail.com","fest2020")
							server.sendmail("abcfest2020@gmail.com",email,msg1)
							return redirect(url_for("function"))
						except IntegrityError:
							flash(f'error')
			if form.festival.data=='christmas':
				pro = Christmas.query.filter_by(name=form.product_name.data).first()
				if pro:
					flash(f'this product is already exist')
				else:
					if form.image.data:
						image_file = save_image(form.image.data)
						pro = Christmas(image=image_file,name = form.product_name.data,types=form.product_type.data,category=form.categories.data,price = form.price.data,companyname=form.company_name.data,quantity=form.quantity.data,detail=form.product_detail.data,username=form.username.data)
						db.session.add(pro)
						try:
							db.session.commit()
							flash(f'your product added successfully!!',"success")
							email=ven.email
							msg1="you have successfully added a product!!"
							server = smtplib.SMTP('smtp.gmail.com:587')
							server.ehlo()
							server.starttls()
							server.login("abcfest2020@gmail.com","fest2020")
							server.sendmail("abcfest2020@gmail.com",email,msg1)
							return redirect(url_for("function"))
						except IntegrityError:
							flash(f'error')
			if form.festival.data=='newyear':
				pro = Newyear.query.filter_by(name=form.product_name.data).first()
				if pro:
					flash(f'this product is already exist')
				else:
					if form.image.data:
						image_file = save_image(form.image.data)
						pro = Newyear(image=image_file,name = form.product_name.data,types=form.product_type.data,category=form.categories.data,price = form.price.data,companyname=form.company_name.data,quantity=form.quantity.data,detail=form.product_detail.data,username=form.username.data)
						db.session.add(pro)
						try:
							db.session.commit()
							flash(f'your product added successfully!!',"success")
							email=ven.email
							msg1="you have successfully added a product!!"
							server = smtplib.SMTP('smtp.gmail.com:587')
							server.ehlo()
							server.starttls()
							server.login("abcfest2020@gmail.com","fest2020")
							server.sendmail("abcfest2020@gmail.com",email,msg1)
							return redirect(url_for("function"))
						except IntegrityError:
							flash(f'error')
		else:
			flash(f'you are not register as a user,please register yourself')
			return redirect(url_for("register"))

	return render_template('addproduct.html',title='addproduct',form=form)

@app.route("/removeproduct",methods=['GET','POST'])

def removeproduct():
	form=RemoveproductForm()
	if form.validate_on_submit():
		if form.festival.data=='diwali':
			diw = Diwali.query.filter_by(username=form.username.data).first()
			if diw:
				if diw.name == form.product_name.data:
					diw1 = Diwali.query.filter_by(name=form.product_name.data).first()
					db.session.delete(diw1)
					try:
						db.session.commit()
						flash(f'your product delete successfully')
						return redirect(url_for("function"))
					except IntegrityError:
						flash(f'error')
				else:
					flash(f'this product is not available')
					return redirect(url_for("function"))
			else:
				flash(f'you are not add any product')
				return redirect(url_for("function"))
		if form.festival.data=='holi':
			pro = Holi.query.filter_by(username=form.username.data).first()
			if pro:
				if pro.name == form.product_name.data:
					db.session.delete(pro)
					try:
						db.session.commit()
						flash(f'your product delete successfully')
						return redirect(url_for("function"))
					except IntegrityError:
						flash(f'error')
				else:
					flash(f'this product is not available')
					return redirect(url_for("function"))
			else:
				flash(f'you are not add any product')
				return redirect(url_for("function"))
		if form.festival.data=='uttrayan':
			pro = Uttrayan.query.filter_by(username=form.username.data).first()
			if pro:
				if pro.name == form.product_name.data:
					db.session.delete(pro)
					try:
						db.session.commit()
						flash(f'your product delete successfully')
						return redirect(url_for("function"))
					except IntegrityError:
						flash(f'error')
				else:
					flash(f'this product is not available')
					return redirect(url_for("function"))
			else:
				flash(f'you are not add any product')
				return redirect(url_for("function"))
		if form.festival.data=='janmashtmi':
			pro = Janmashtmi.query.filter_by(username=form.username.data).first()
			if pro:
				if pro.name == form.product_name.data:
					db.session.delete(pro)
					try:
						db.session.commit()
						flash(f'your product delete successfully')
						return redirect(url_for("function"))
					except IntegrityError:
						flash(f'error')
				else:
					flash(f'this product is not available')
					return redirect(url_for("function"))
			else:
				flash(f'you are not add any product')
				return redirect(url_for("function"))
		if form.festival.data=='ganeshchaturthi':
			pro = Ganeshchaturthi.query.filter_by(username=form.username.data).first()
			if pro:
				if pro.name == form.product_name.data:
					db.session.delete(pro)
					try:
						db.session.commit()
						flash(f'your product delete successfully')
						return redirect(url_for("function"))
					except IntegrityError:
						flash(f'error')
				else:
					flash(f'this product is not available')
					return redirect(url_for("function"))
			else:
				flash(f'you are not add any product')
				return redirect(url_for("function"))
		if form.festival.data=='navratri':
			pro = Navratri.query.filter_by(username=form.username.data).first()
			if pro:
				if pro.name == form.product_name.data:
					db.session.delete(pro)
					try:
						db.session.commit()
						flash(f'your product delete successfully')
						return redirect(url_for("function"))
					except IntegrityError:
						flash(f'error')
				else:
					flash(f'this product is not available')
					return redirect(url_for("function"))
			else:
				flash(f'you are not add any product')
				return redirect(url_for("function"))
		if form.festival.data=='christmas':
			pro = Christmas.query.filter_by(username=form.username.data).first()
			if pro:
				if pro.name == form.product_name.data:
					db.session.delete(pro)
					try:
						db.session.commit()
						flash(f'your product delete successfully')
						return redirect(url_for("function"))
					except IntegrityError:
						flash(f'error')
				else:
					flash(f'this product is not available')
					return redirect(url_for("function"))
			else:
				flash(f'you are not add any product')
				return redirect(url_for("function"))
		if form.festival.data=='newyear':
			pro = Newyear.query.filter_by(username=form.username.data).first()
			if pro:
				if pro.name == form.product_name.data:
					db.session.delete(pro)
					try:
						db.session.commit()
						flash(f'your product delete successfully')
						return redirect(url_for("function"))
					except IntegrityError:
						flash(f'error')
				else:
					flash(f'this product is not available')
					return redirect(url_for("function"))
			else:
				flash(f'you are not add any product')
				return redirect(url_for("function"))
		if form.festival.data=='rakshabandhan':
			pro = Rakshabandhan.query.filter_by(username=form.username.data).first()
			if pro:
				if pro.name == form.product_name.data:
					db.session.delete(pro)
					try:
						db.session.commit()
						flash(f'your product delete successfully')
						return redirect(url_for("function"))
					except IntegrityError:
						flash(f'error')
				else:
					flash(f'this product is not available')
					return redirect(url_for("function"))
			else:
				flash(f'you are not add any product')
				return redirect(url_for("function"))

	return render_template('removeproduct.html',title='removeproduct',form=form)

@app.route("/viewdetail.html",methods=['GET','POST'])

def viewdetail():
	return render_template('viewdetail.html')

@app.route("/bike.html",methods=['GET','POST'])

def bike():
	form = Bikeform()
	if form.validate_on_submit():
		ser = Service.query.filter_by(username=form.username.data).first()
		if ser:
			pro = Servicedetail.query.filter_by(bikeno=form.bikeno.data).first()
			if pro:
				flash(f'this bikeno already register')
				return redirect(url_for("detail"))
			else:
				pro1 = Servicedetail(username=form.username.data,bikeno= form.bikeno.data,bikename=form.bikename.data)
				db.session.add(pro1)
				try:
					db.session.commit()
					flash(f'your product added successfully!!',"success")
					return redirect(url_for("detail"))
				except IntegrityError:
					flash(f'error')
		else:
			flash(f'you are not register as a user')
			return redirect(url_for("register"))

	return render_template('bike.html',form=form)


@app.route("/viewcustomer",methods=['GET','POST'])
def viewcustomer():
	data = Customer.query.all()
	return render_template('viewcustomer.html',customers = Customer.query.all())

@app.route("/viewvendor",methods=['GET','POST'])
def viewvendor():
	return render_template('viewvendor.html',vendors = Vendor.query.all())

@app.route("/viewservice",methods=['GET','POST'])
def viewservice():
	return render_template('viewservice.html',services = Service.query.all())

@app.route("/diwaliproduct",methods=['GET','POST'])
def diwaliproduct():
	return render_template('diwaliproduct.html',products = Diwali.query.all())

@app.route("/rakshabandhanproduct",methods=['GET','POST'])
def rakshabandhanproduct():
	return render_template('rakshabandhanproduct.html',products = Rakshabandhan.query.all())

@app.route("/holiproduct",methods=['GET','POST'])
def holiproduct():
	return render_template('holiproduct.html',products = Holi.query.all())

@app.route("/ganeshchaturthiproduct",methods=['GET','POST'])
def ganeshchaturthiproduct():
	return render_template('ganeshchaturthiproduct.html',products = Ganeshchaturthi.query.all())

@app.route("/janmashtmiproduct",methods=['GET','POST'])
def janmashtmiproduct():
	return render_template('janmashtmiproduct.html',products = Janmashtmi.query.all())

@app.route("/uttrayanproduct",methods=['GET','POST'])
def uttrayanproduct():
	return render_template('uttrayanproduct.html',products = Uttrayan.query.all())

@app.route("/navratriproduct",methods=['GET','POST'])
def navratriproduct():
	return render_template('navratriproduct.html',products = Navratri.query.all())

@app.route("/christmasproduct",methods=['GET','POST'])
def christmasproduct():
	return render_template('christmasproduct.html',products = Christmas.query.all())

@app.route("/newyearproduct",methods=['GET','POST'])
def newyearproduct():
	return render_template('newyearproduct.html',products = Newyear.query.all())

@app.route("/logout")

def logout():
	logout_user()
	return redirect(url_for("n"))



if __name__=='__main__':
	app.run(debug=True)
