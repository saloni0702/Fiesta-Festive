from __main__ import db, login_manager
from flask_login import UserMixin
import json

@login_manager.user_loader
def load_user(ad_id):
	return Admin.query.get(int(ad_id))

@login_manager.user_loader
def load_user(fee_id):
	return Feedback.query.get(int(fee_id))

@login_manager.user_loader
def load_user(cus_id):
	return Customer.query.get(int(cus_id))

@login_manager.user_loader
def load_user(ven_id):
	return Vendor.query.get(int(ven_id))

@login_manager.user_loader
def load_user(ser_id):
	return Service.query.get(int(ser_id))

@login_manager.user_loader
def load_user(rak_id):
	return Rakshabandhan.query.get(int(rak_id))

@login_manager.user_loader
def load_user(diw_id):
	return Diwali.query.get(int(diw_id))


@login_manager.user_loader
def load_user(ho_id):
	return Holi.query.get(int(ho_id))

@login_manager.user_loader
def load_user(chr_id):
	return Christmas.query.get(int(chr_id))

@login_manager.user_loader
def load_user(new_id):
	return Newyear.query.get(int(new_id))

@login_manager.user_loader
def load_user(utt_id):
	return Uttrayan.query.get(int(utt_id))

@login_manager.user_loader
def load_user(nav_id):
	return Navratri.query.get(int(nav_id))

@login_manager.user_loader
def load_user(gan_id):
	return Ganeshchaturthi.query.get(int(gan_id))

@login_manager.user_loader
def load_user(jan_id):
	return Janmashtmi.query.get(int(jan_id))

@login_manager.user_loader
def load_user(serv_id):
	return Servicedetail.query.get(int(serv_id))

class Admin(db.Model,UserMixin):
	id = db.Column(db.Integer,primary_key=True)
	username = db.Column(db.String(20),unique=True,nullable=False)
	name = db.Column(db.String(20),nullable=False)
	password = db.Column(db.String(20),nullable=False,unique=True)

	def __repr__(self):
		return f"Admin('{self.username}','{self.name}','{self.password}')"

class Feedback(db.Model,UserMixin):
	id = db.Column(db.Integer,primary_key=True)
	customer_id = db.Column(db.String(20),nullable=False)
	feedback = db.Column(db.String(100),nullable=False)
	def __repr__(self):
		return f"Admin('{self.customer_id}','{self.feedback}')"


class Customer(db.Model,UserMixin):
	id = db.Column(db.Integer,primary_key=True)
	username = db.Column(db.String(20),unique=True,nullable=False)
	name = db.Column(db.String(20),nullable=False)
	email = db.Column(db.String(120),nullable=False)
	houseno = db.Column(db.Integer,nullable=False)
	area = db.Column(db.String(120),nullable=False)
	taluka = db.Column(db.String(120),nullable=False)
	district = db.Column(db.String(120),nullable=False)
	pincode = db.Column(db.Integer,nullable=False)
	PhoneNumber = db.Column(db.Integer,nullable=False)
	password = db.Column(db.String(20),nullable=False)

	def __repr__(self):
		 return f"Customer('{self.username}','{self.name}','{self.email}','{self.houseno}','{self.area}','{self.taluka}','{self.district}','{self.pincode}','{self.PhoneNumber}','{self.password}')"

class Vendor(db.Model,UserMixin):
	id = db.Column(db.Integer,primary_key=True)
	username = db.Column(db.String(20),unique=True,nullable=False)
	name = db.Column(db.String(20),nullable=False)
	email = db.Column(db.String(120),nullable=False)
	houseno = db.Column(db.Integer,nullable=False)
	area = db.Column(db.String(120),nullable=False)
	taluka = db.Column(db.String(120),nullable=False)
	district = db.Column(db.String(120),nullable=False)
	pincode = db.Column(db.Integer,nullable=False)
	PhoneNumber = db.Column(db.Integer,nullable=False)
	password = db.Column(db.String(20),nullable=False)

	def __repr__(self):
		 return f"Vendor('{self.username}','{self.name}','{self.email}','{self.houseno}','{self.area}','{self.taluka}','{self.district}','{self.pincode}','{self.PhoneNumber}','{self.password}')"

class Service(db.Model,UserMixin):
	id = db.Column(db.Integer,primary_key=True)
	username = db.Column(db.String(20),unique=True,nullable=False)
	name = db.Column(db.String(20),nullable=False)
	email = db.Column(db.String(120),nullable=False)
	houseno = db.Column(db.Integer,nullable=False)
	area = db.Column(db.String(120),nullable=False)
	taluka = db.Column(db.String(120),nullable=False)
	district = db.Column(db.String(120),nullable=False)
	pincode = db.Column(db.Integer,nullable=False)
	PhoneNumber = db.Column(db.Integer,nullable=False)
	password = db.Column(db.String(20),nullable=False)

	def __repr__(self):
		 return f"Service('{self.username}','{self.name}','{self.email}','{self.houseno}','{self.area}','{self.taluka}','{self.district}','{self.pincode}','{self.PhoneNumber}','{self.password}')"

class Diwali(db.Model,UserMixin):
	id = db.Column(db.Integer,primary_key=True)
	image = db.Column(db.String(120),nullable=False)
	name = db.Column(db.String(120),nullable=False,unique=True)
	types = db.Column(db.String(120),nullable=False)
	category = db.Column(db.String(120),nullable=False)
	price = db.Column(db.Integer,nullable=False)
	companyname = db.Column(db.String(120),nullable=False)
	quantity = db.Column(db.Integer,nullable=False)
	detail = db.Column(db.String(200),nullable=False)
	username = db.Column(db.String(120),nullable=False)

	def __repr__(self):
		return f"Diwali('{self.image}','{self.name}','{self.types}','{self.category}','{self.price}','{self.companyname}','{self.quantity}','{self.detail}','{self.username}')"

class Holi(db.Model,UserMixin):
	id = db.Column(db.Integer,primary_key=True)
	image = db.Column(db.String(120),nullable=False)
	name = db.Column(db.String(120),nullable=False,unique=True)
	types = db.Column(db.String(120),nullable=False)
	category = db.Column(db.String(120),nullable=False)
	price = db.Column(db.Integer,nullable=False)
	companyname = db.Column(db.String(120),nullable=False)
	quantity = db.Column(db.Integer,nullable=False)
	detail = db.Column(db.String(200),nullable=False)
	username = db.Column(db.String(120),nullable=False)

	def __repr__(self):
		return f"Holi('{self.image}','{self.name}','{self.types}','{self.category}','{self.price}','{self.companyname}','{self.quantity}','{self.detail}','{self.username}')"

class Uttrayan(db.Model,UserMixin):
	id = db.Column(db.Integer,primary_key=True)
	image = db.Column(db.String(120),nullable=False)
	name = db.Column(db.String(120),nullable=False,unique=True)
	types = db.Column(db.String(120),nullable=False)
	category = db.Column(db.String(120),nullable=False)
	price = db.Column(db.Integer,nullable=False)
	companyname = db.Column(db.String(120),nullable=False)
	quantity = db.Column(db.Integer,nullable=False)
	detail = db.Column(db.String(200),nullable=False)
	username = db.Column(db.String(120),nullable=False)

	def __repr__(self):
		return f"Uttrayan('{self.image}','{self.name}','{self.types}','{self.category}','{self.price}','{self.companyname}','{self.quantity}','{self.detail}','{self.username}')"

class Navratri(db.Model,UserMixin):
	id = db.Column(db.Integer,primary_key=True)
	image = db.Column(db.String(120),nullable=False)
	name = db.Column(db.String(120),nullable=False,unique=True)
	types = db.Column(db.String(120),nullable=False)
	category = db.Column(db.String(120),nullable=False)
	price = db.Column(db.Integer,nullable=False)
	companyname = db.Column(db.String(120),nullable=False)
	quantity = db.Column(db.Integer,nullable=False)
	detail = db.Column(db.String(200),nullable=False)
	username = db.Column(db.String(120),nullable=False)

	def __repr__(self):
		return f"Navratri('{self.image}','{self.name}','{self.types}','{self.category}','{self.price}','{self.companyname}','{self.quantity}','{self.detail}','{self.username}')"

class Newyear(db.Model,UserMixin):
	id = db.Column(db.Integer,primary_key=True)
	image = db.Column(db.String(120),nullable=False)
	name = db.Column(db.String(120),nullable=False,unique=True)
	types = db.Column(db.String(120),nullable=False)
	category = db.Column(db.String(120),nullable=False)
	price = db.Column(db.Integer,nullable=False)
	companyname = db.Column(db.String(120),nullable=False)
	quantity = db.Column(db.Integer,nullable=False)
	detail = db.Column(db.String(200),nullable=False)
	username = db.Column(db.String(120),nullable=False)

	def __repr__(self):
		return f"Newyear('{self.image}','{self.name}','{self.types}','{self.category}','{self.price}','{self.companyname}','{self.quantity}','{self.detail}','{self.username}')"

class Christmas(db.Model,UserMixin):
	id = db.Column(db.Integer,primary_key=True)
	image = db.Column(db.String(120),nullable=False)
	name = db.Column(db.String(120),nullable=False,unique=True)
	types = db.Column(db.String(120),nullable=False)
	category = db.Column(db.String(120),nullable=False)
	price = db.Column(db.Integer,nullable=False)
	companyname = db.Column(db.String(120),nullable=False)
	quantity = db.Column(db.Integer,nullable=False)
	detail = db.Column(db.String(200),nullable=False)
	username = db.Column(db.String(120),nullable=False)

	def __repr__(self):
		return f"Christmas('{self.image}','{self.name}','{self.types}','{self.category}','{self.price}','{self.companyname}','{self.quantity}','{self.detail}','{self.username}')"

class Rakshabandhan(db.Model,UserMixin):
	id = db.Column(db.Integer,primary_key=True)
	image = db.Column(db.String(120),nullable=False)
	name = db.Column(db.String(120),nullable=False,unique=True)
	types = db.Column(db.String(120),nullable=False)
	category = db.Column(db.String(120),nullable=False)
	price = db.Column(db.Integer,nullable=False)
	companyname = db.Column(db.String(120),nullable=False)
	quantity = db.Column(db.Integer,nullable=False)
	detail = db.Column(db.String(200),nullable=False)
	username = db.Column(db.String(120),nullable=False)

	def __repr__(self):
		return f"Rakshabandhan('{self.image}','{self.name}','{self.types}','{self.category}','{self.price}','{self.companyname}','{self.quantity}','{self.detail}','{self.username}')"


class Ganeshchaturthi(db.Model,UserMixin):
	id = db.Column(db.Integer,primary_key=True)
	image = db.Column(db.String(120),nullable=False)
	name = db.Column(db.String(120),nullable=False,unique=True)
	types = db.Column(db.String(120),nullable=False)
	category = db.Column(db.String(120),nullable=False)
	price = db.Column(db.Integer,nullable=False)
	companyname = db.Column(db.String(120),nullable=False)
	quantity = db.Column(db.Integer,nullable=False)
	detail = db.Column(db.String(200),nullable=False)
	username = db.Column(db.String(120),nullable=False)

	def __repr__(self):
		return f"Ganeshchaturthi('{self.image}','{self.name}','{self.types}','{self.category}','{self.price}','{self.companyname}','{self.quantity}','{self.detail}','{self.username}')"

class Janmashtmi(db.Model,UserMixin):
	id = db.Column(db.Integer,primary_key=True)
	image = db.Column(db.String(120),nullable=False)
	name = db.Column(db.String(120),nullable=False,unique=True)
	types = db.Column(db.String(120),nullable=False)
	category = db.Column(db.String(120),nullable=False)
	price = db.Column(db.Integer,nullable=False)
	companyname = db.Column(db.String(120),nullable=False)
	quantity = db.Column(db.Integer,nullable=False)
	detail = db.Column(db.String(200),nullable=False)
	username = db.Column(db.String(120),nullable=False)

	def __repr__(self):
		return f"Janmashtmi('{self.image}','{self.name}','{self.types}','{self.category}','{self.price}','{self.companyname}','{self.quantity}','{self.detail}','{self.username}')"


class Servicedetail(db.Model,UserMixin):
	id = db.Column(db.Integer,primary_key=True)
	username = db.Column(db.String(20),unique=True,nullable=False)
	bikeno = db.Column(db.String(20),nullable=False)
	bikename = db.Column(db.String(20),nullable=False,unique=True)

	def __repr__(self):
		return f"Servicedetail('{self.username}','{self.bikeno}','{self.bikename}')"

class Reminder(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    date = db.Column(db.DateTime())
    email = db.Column(db.String())
    text = db.Column(db.Text())

    def __repr__(self):
        return "<Reminder '{}'>".format(self.text[:20])

