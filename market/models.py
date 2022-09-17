from django.db import models
from django.contrib.auth.models import User
   
 
class Market(models.Model):
    """ Model for reviews of cars """
# The different choices for image filters
    image_filter_choices = [
        ('_1977', '1977'), ('brannan', 'Brannan'),
        ('earlybird', 'Earlybird'), ('hudson', 'Hudson'),
        ('inkwell', 'Inkwell'), ('lofi', 'Lo-Fi'),
        ('kelvin', 'Kelvin'), ('normal', 'Normal'),
        ('nashville', 'Nashville'), ('rise', 'Rise'),
        ('toaster', 'Toaster'), ('valencia', 'Valencia'),
        ('walden', 'Walden'), ('xpro2', 'X-pro II')
    ]
# The different choices for car brand
    brand_choices = [
        (('Alfa Romeo'), ('Alfa Romeo')),
        (('Alpina'), ('Alpina')),
        (('Aston Martin'), ('Aston Martin')),
        (('Audi'), ('Audi')),
        (('Austin'), ('Austin')),
        (('Bentley'), ('Bentley')),
        (('BMW'), ('BMW')),
        (('Buick'), ('Buick')),
        (('Cadillac'), ('Cadillac')),
        (('Chevrolet'), ('Chevrolet')),
        (('Chrysler'), ('Chrysler')),
        (('Citroën'), ('Citroën')),
        (('Cupra'), ('Cupra')),
        (('Dacia'), ('Dacia')),
        (('Dodge'), ('Dodge')),
        (('DS'), ('DS')),
        (('Ferrari'), ('Ferrari')),
        (('Fiat'), ('Fiat')),
        (('Ford'), ('Ford')),
        (('GMC'), ('GMC')),
        (('Honda'), ('Honda')),
        (('Hummer'), ('Hummer')),
        (('Hyundai'), ('Hyundai')),
        (('Infiniti'), ('Infiniti')),
        (('Isuzu'), ('Isuzu')),
        (('Iveco'), ('Iveco')),
        (('Jaguar'), ('Jaguar')),
        (('Jeep'), ('Jeep')),
        (('Kia'), ('Kia')),
        (('Lamborghini'), ('Lamborghini')),
        (('Lancia'), ('Lancia')),
        (('Land Rover'), ('Land Rover')),
        (('Lexus'), ('Lexus')),
        (('Lincoln'), ('Lincoln')),
        (('Lotus'), ('Lotus')),
        (('Maserati'), ('Maserati')),
        (('Maxus'), ('Maxus')),
        (('Mazda'), ('Mazda')),
        (('McLaren'), ('McLaren')),
        (('Mercedes-Benz'), ('Mercedes-Benz')),
        (('Mercury'), ('Mercury')),
        (('MG'), ('MG')),
        (('Mini'), ('Mini')),
        (('Mitsubishi'), ('Mitsubishi')),
        (('Nissan'), ('Nissan')),
        (('Oldsmobile'), ('Oldsmobile')),
        (('Opel'), ('Opel')),
        (('Peugeot'), ('Peugeot')),
        (('Plymouth'), ('Plymouth')),
        (('Polestar'), ('Polestar')),
        (('Pontiac'), ('Pontiac')),
        (('Porsche'), ('Porsche')),
        (('Ram'), ('Ram')),
        (('Renault'), ('Renault')),
        (('Rolls-Royce'), ('Rolls-Royce')),
        (('Rover/BMC'), ('Rover/BMC')),
        (('Saab'), ('Saab')),
        (('SEAT'), ('SEAT')),
        (('Skoda'), ('Skoda')),
        (('Smart'), ('Smart')),
        (('Ssang Yong'), ('Ssang Yong')),
        (('Subaru'), ('Subaru')),
        (('Suzuki'), ('Suzuki')),
        (('Tesla'), ('Tesla')),
        (('Toyota'), ('Toyota')),
        (('Volkswagen'), ('Volkswagen')),
        (('Volvo'), ('Volvo')),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    brand = models.CharField(
        max_length=30,
        choices=brand_choices,
        default='none'
    )
    image = models.ImageField(
        upload_to='images/', blank=True
    )
    image_filter = models.CharField(
        max_length=32, choices=image_filter_choices, default='normal')
    model = models.CharField(max_length=200)
    model_year = models.IntegerField()
    facilities = models.TextField(blank=True)
    problems = models.TextField(blank=True)
    description = models.TextField()
    phone = models.IntegerField()
    email = models.EmailField()
 
 
    class Meta:
        ordering = ['-created_on']
 
    def __str__(self):
        return f'{self.id} {self.brand} {self.model} {self.model_year}'

