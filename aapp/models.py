##from django.db import models
#https://www.youtube.com/watch?v=z5e_8FgKZig&list=PLCC34OHNcOtqW9BJmgQPPzUpJ8hl49AGy&index=4
#15;18
# Create your models here.
from email.headerregistry import Address
from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Serial(models.Model):
	name = models.CharField('Serial Name', max_length=120)
	address = models.CharField(max_length=300)
	zip_code = models.CharField('Zip Code', max_length=15)
	phone = models.CharField('Contact Phone', max_length=25, blank=True)
	web = models.URLField('Website Address', blank=True)
	email_address = models.EmailField('Email Address', blank=True)
	#owner = models.IntegerField("Owner", blank=False, default=1)
	#serial_image = models.ImageField(null=True, blank=True, upload_to="images/")
	
	def __str__(self):
		return self.name


class User(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField('User Email')

	def __str__(self):
	    return self.first_name + ' ' + self.last_name
 
class Associates(models.Model):
	name = models.CharField('Crypto Name', max_length=120)
	serial_date = models.DateTimeField('Date')
	serial = models.ForeignKey(Serial, blank=True, null=True, on_delete=models.CASCADE)
	#venue = models.CharField(max_length=120)
	manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
	description = models.TextField(blank=True)
	#clients = models.ManyToManyField(User, blank=True)
	approved = models.BooleanField('Aprroved', default=False)

	def __str__(self):
		return self.name
 
 
class Cryptocurrency(models.Model):
	name = models.CharField('Crypto Name', max_length=120)
	serial_date = models.DateTimeField('Date')
	serial = models.ForeignKey(Serial, blank=True, null=True, on_delete=models.CASCADE)
	#venue = models.CharField(max_length=120)
	manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
	description = models.TextField(blank=True)
	#attendees = models.ManyToManyField(User, blank=True)
	approved = models.BooleanField('Aprroved', default=False)

	def __str__(self):
		return self.name
class NFT(models.Model):
	name = models.CharField('NFT Name', max_length=120)
	serial_date = models.DateTimeField('Date')
	serial = models.ForeignKey(Serial, blank=True, null=True, on_delete=models.CASCADE)
	#venue = models.CharField(max_length=120)
	manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
	description = models.TextField(blank=True)
	#attendees = models.ManyToManyField(User, blank=True)
	approved = models.BooleanField('Aprroved', default=False)

	def __str__(self):
		return self.name
#Financial

class Market(models.Model):
	name = models.CharField('Market', max_length=120)
	serial_date = models.DateTimeField('Date')
	serial = models.ForeignKey(Serial, blank=True, null=True, on_delete=models.CASCADE)
	#venue = models.CharField(max_length=120)
	manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
	description = models.TextField(blank=True)
	#attendees = models.ManyToManyField(User, blank=True)
	approved = models.BooleanField('Aprroved', default=False)

	def __str__(self):
		return self.name

class Trade(models.Model):
	name = models.CharField('Trade', max_length=120)
	serial_date = models.DateTimeField('Date')
	serial = models.ForeignKey(Serial, blank=True, null=True, on_delete=models.CASCADE)
	#venue = models.CharField(max_length=120)
	manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
	description = models.TextField(blank=True)
	#attendees = models.ManyToManyField(User, blank=True)
	approved = models.BooleanField('Aprroved', default=False)

	def __str__(self):
		return self.name

class Derivatives(models.Model):
	name = models.CharField('Derivatives', max_length=120)
	serial_date = models.DateTimeField('Date')
	serial = models.ForeignKey(Serial, blank=True, null=True, on_delete=models.CASCADE)
	#venue = models.CharField(max_length=120)
	manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
	description = models.TextField(blank=True)
	#attendees = models.ManyToManyField(User, blank=True)
	approved = models.BooleanField('Aprroved', default=False)

	def __str__(self):
		return self.name

class Earn(models.Model):
	name = models.CharField('Earn', max_length=120)
	serial_date = models.DateTimeField('Date')
	serial = models.ForeignKey(Serial, blank=True, null=True, on_delete=models.CASCADE)
	#venue = models.CharField(max_length=120)
	manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
	description = models.TextField(blank=True)
	#attendees = models.ManyToManyField(User, blank=True)
	approved = models.BooleanField('Aprroved', default=False)

	def __str__(self):
		return self.name
class Finance(models.Model):
	name = models.CharField('Finance', max_length=120)
	serial_date = models.DateTimeField('Date')
	serial = models.ForeignKey(Serial, blank=True, null=True, on_delete=models.CASCADE)
	#venue = models.CharField(max_length=120)
	manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
	description = models.TextField(blank=True)
	#attendees = models.ManyToManyField(User, blank=True)
	approved = models.BooleanField('Aprroved', default=False)

	def __str__(self):
		return self.name
#class Legist(models.Model):
#	name = models.CharField('Serial Name', max_length=120)
#	serial_date = models.DateTimeField('Date')
#	serial = models.ForeignKey(Serial, blank=True, null=True, on_delete=models.CASCADE)
#	sserial = models.CharField(max_length=120)
 
#	manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
#	description = models.TextField(blank=True)
#	attendees = models.ManyToManyField(User, blank=True)
#	approved = models.BooleanField('Aprroved', default=False)

#	def __str__(self):
#		return self

#class Burial(models.Model):
#	name = models.CharField('Serial Name', max_length=120)
#	serial_date = models.DateTimeField('Date')
#	serial = models.ForeignKey(Serial, blank=True, null=True, on_delete=models.CASCADE)
#	serial = models.CharField(max_length=120)
 
#	manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
#	description = models.TextField(blank=True)
#	attendees = models.ManyToManyField(User, blank=True)
#	approved = models.BooleanField('Aprroved', default=False)

#	def __str__(self):
#		return self.name

	#@property
	#def Days_till(self):
		#today = date.today()
		#days_till = self.event_date.date() - today
		#days_till_stripped = str(days_till).split(",", 1)[0]
		#return days_till_stripped
	
	#@property
	#def Is_Past(self):
		#today = date.today()
		#if self.event_date.date() < today:
		#	thing = "Past"
		#else:
		#	thing = "Future"
		#return thing
