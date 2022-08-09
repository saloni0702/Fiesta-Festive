from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


class RegistrationForm(FlaskForm):
	username=StringField('Username',validators=[DataRequired(), Length(min=2,max=20)])
	name=StringField('Name',validators=[DataRequired()])
	email=StringField('E-mail',validators=[DataRequired(), Email()])
	District=SelectField('District',validators=[DataRequired()],choices=[('1','Ahmedabad'),('2','Amreli'),('3','Anand'),('4','Aravalli'),('5','Banaskantha'),('6','Bharuch'),('7','Bhavnagar'),('8','Botad'),('9','Chota Udaipur'),('10','Dahod'),('11','Dang'),('12','Dwarka'),('13','Gandhinagar'),('14','Gir Somnath'),('15','Jamnagar'),('16','Junagrah'),('17','Kutch'),('18','Kheda'),('19','Mahisagar'),('20','Mehsana'),('21','Morvi'),('22','Narmada'),('23','Navsari'),('24','Panchmahal'),('25','Patan'),('26','Porbandar'),('27','Rajkot'),('28','Sabarkantha'),('29','Surat'),('30','Surendranagar'),('31','Tapi'),('32','Vadodra'),('33','Valsad')])
	Taluka=SelectField('Taluka',validators=[DataRequired()],choices=[('1', 'Ahmedabad'), ('2', 'Ambaji'), ('3', 'Amboli'),('4','Amod'),('5','Amreli'),('6','Anand'),('7','Anandpar'),('8','Ananda'),('9','Anjar'),('10','Ankleshwar'),('11','Antalia'),('12','Balasinor'),('13','Bardoli'),('14','Bareja'),('15','Bhachav'),('16','Bhanvad'),('17','Bharuch'),('18','Bhavnagar'),('19','Bhiloda'),('20','Bhuj'),('21','Borsad'),('22','Botad'),('23','Chota Udaipur'),('24','Chotila'),('25','Dahod'),('26','Damnagar'),('27','Danta'),('28','Dediapada'),('29','Deesa'),('30','Dehgam'),('31','Deodar'),('32','Dholka'),('33','Dhangadhra'),('34','Dhrol'),('35','Gadhada'),('36','Gandhinagar'),('37','Godhra'),('38','Gondal'),('39','Halol'),('40','Halvad'),('41','Himatnagar'),('42','Idar'),('43','Jamjodhpur'),('44','Jamnagar'),('45','Jetpur'),('46','Junagrah'),('47','Kalawad'),('48','Keshod'),('49','Khambhat'),('50','Khambhaliya'),('51','Khavda'),('52','Lakhpat'),('53','Mahuva'),('54','Mandvi'),('55','Mangrol'),('56','Mehmedabad'),('57','Mehsana'),('58','Modasa'),('59','Morvi'),('60','Mundra'),('61','Nadiad'),('62','Nakhatrana'),('63','Nalia'),('64','Navsari'),('65','Okha'),('66','Palanpur'),('67','Palitana'),('68','Patan'),('69','Porbandar'),('70','Radhanpur'),('71','Rajkot'),('72','Sanand'),('73','Surat'),('74','Surendranagar'),('75','Vadodra'),('76','Valsad'),('77','Vapi'),('78','Wankaner')])
	Area=StringField('Area',validators=[DataRequired()])
	House_no=StringField('House_No',validators=[DataRequired()])
	pincode=StringField('Pincode',validators=[DataRequired()])
	PhoneNumber=IntegerField('PhoneNumber',validators=[DataRequired()])
	example = RadioField('Type Of User', choices=[('0','Vendor'),('1','Customer'),('2','Service')])
	password=PasswordField('Password',validators=[DataRequired(), Length(min=4,max=20)])
	confirm_password=PasswordField('Confirm_Password',
						validators=[DataRequired(),EqualTo('password')])
	submit=SubmitField('Sign Up')


class AdminForm(FlaskForm):
	username=StringField('Username',
						validators=[DataRequired(), Length(min=2,max=20)])
	password=PasswordField('Password',
					validators=[DataRequired(), Length(min=4,max=20)])
	submit=SubmitField('Login')



class LoginForm(FlaskForm):
	username=StringField('Username',
						validators=[DataRequired(), Length(min=2,max=20)])
	password=PasswordField('Password',
					validators=[DataRequired(), Length(min=4,max=20)])
	example = RadioField('Type Of User', choices=[('0','Vendor'),('1','Customer'),('2','Service')])
	remember=BooleanField('Remember Me')
	submit=SubmitField('Login')


class ForgetForm(FlaskForm):
	username=StringField('Username',
						validators=[DataRequired(), Length(min=2,max=20)])
	password=PasswordField('Password',
					validators=[DataRequired(),Length(min=2,max=20)])
	confirm_password=PasswordField('Confirm_Password',
						validators=[DataRequired(),EqualTo('password')])
	example = RadioField('Type Of User', choices=[('0','Vendor'),('1','Customer'),('2','Service')])
	submit=SubmitField('submit')


class FestivalSelection(FlaskForm):
	Festival=SelectField('Festival',validators=[DataRequired()],choices=[('0','diwali'),('1','holi'),('2','uttrayan'),('4','rakshabandhan'),('5','janmashtmi'),('6','ganeshchaturthi'),('7','navratri'),('8','christmas'),('9','newyear')])
	submit=SubmitField('submit')

class Diwali(FlaskForm):
	Diwali=SelectField('Diwali',validators=[DataRequired()],choices=[('0','Diwali')])
	submit=SubmitField('Add Cart')

class AddproductForm(FlaskForm):
	image = FileField('Image',validators=[FileAllowed(['jpg','png','jpeg'])])
	product_name = StringField('Product name',
						validators=[DataRequired(), Length(min=2,max=20)])
	product_type = SelectField('Types',validators=[DataRequired()],choices=[('Light','Light'),('Rangoli-Color','Rangoli-Color'),('Clothes','Clothes'),('Sweets','Sweets'),('Namkeen','Namkeen'),('Colors','Colors'),('Crackers','Crackers'),('Flags','Flags'),('Murti','Murti'),('Rakhi','Rakhi'),('Kites','Kites'),('Fruits','Fruits'),('MedicalKit','MedicalKit'),('Shoes','Shoes'),('Ornaments','Ornaments'),('Watches','Watches'),('Gifts','Gifts'),('Others','Others')])
	categories = SelectField('categories',validators=[DataRequired()],choices=[('Eatable','Eatable'),('Wearable','Wearable'),('Decoratable','Decoratable'),('Usable','Usable'),('Celebratable','Celebratable')])
	price = IntegerField('Price',validators=[DataRequired()])
	company_name = StringField('Company name',validators=[DataRequired(), Length(min=2,max=20)])
	quantity = IntegerField('Quantity',validators=[DataRequired()])
	product_detail = StringField('Product Detail',validators=[DataRequired()])
	username = StringField('Username', validators=[DataRequired(), Length(min=2,max=20)])
	festival=SelectField('Festival',validators=[DataRequired()],choices=[('diwali','diwali'),('holi','holi'),('uttrayan','uttrayan'),('rakshabandhan','rakshabandhan'),('janmashtmi','janmashtmi'),('ganeshchaturthi','ganeshchaturthi'),('navratri','navratri'),('christmas','christmas'),('newyear','newyear')])
	submit  = SubmitField('Add')

class RemoveproductForm(FlaskForm):
	product_name = StringField('Product name',
						validators=[DataRequired(), Length(min=2,max=20)])
	username = StringField('Username', validators=[DataRequired(), Length(min=2,max=20)])
	festival=SelectField('Festival',validators=[DataRequired()],choices=[('diwali','diwali'),('holi','holi'),('uttrayan','uttrayan'),('rakshabandhan','rakshabandhan'),('janmashtmi','janmashtmi'),('ganeshchaturthi','ganeshchaturthi'),('navratri','navratri'),('christmas','christmas'),('newyear','newyear')])
	submit  = SubmitField('Remove')

class Bikeform(FlaskForm):
	username=StringField('Username',
						validators=[DataRequired(), Length(min=2,max=20)])
	bikeno=StringField('Bike_no',
					validators=[DataRequired(),Length(min=2,max=20)])
	bikename=StringField('Bike_name',
						validators=[DataRequired(),Length(min=2,max=20)])
	submit=SubmitField('Add Detail')

class  ValidationForm(FlaskForm):

	username=StringField('Username',
						validators=[DataRequired(), Length(min=2,max=20)])
	password=PasswordField('Password',
					validators=[DataRequired(), Length(min=4,max=20)])
	submit=SubmitField('Validate')