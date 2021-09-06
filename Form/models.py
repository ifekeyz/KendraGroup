from django.db import models
# from state_field.fields import StateField

class Forms(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, default=True)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    # state = StateField(max_length=20)
    STATUS=(('SINGLE','Single'),('MARRIED','Marrried'),('Divorce','Divorce'))
    status=models.CharField(max_length=20,
        choices=STATUS,
        blank=True,
        default='SINGLE',
    )
    SEX = (('MALE','Male'),('FEMALE','Female'))
    sex = models.CharField(max_length=20,
        choices=SEX,
        blank=True,
        default='MALE',
    )
    StateOfOrigin = (('ABUJA (FCT)','Abuja(FCT)'),('ABIA','Abia'),('ANAMBRA','Anambra'),('ADAMAWA','Adamawa'),('BAUCHI','Bauchi'),('BAYELSA','Bayelsa'),
    ('BENUE','Benue'),
    ('Borno','Borno'),('CROSS RIVER','Cross river'),('DELTA','Delta'),('EBONYI','Ebonyi'),('EKITI','Ekiti'),('ENUGU','Enugu'),('GOMBE','Gombe'),
    ('IMO','Imo'),
    ('JIGAWA','Jigawa'),('KADUNA','Kaduna'),('KANO','Kano'),('KASTINA','Katsina'),('KEBBI','Kebbi'),('KWARA','Kwara'),('Kogi','Kogi'),('LAGOS','Lagos'),
    ('NASARAWA','Nasarawa'),('NIGER','Niger'),('OGUN','Ogun'),('ONDO','Ondo'),('OSUN','Osun'),('OYO','Oyo'),('OGUN','Ogun'),('PLATEAU','Plateau'),
    ('RIVERS','Rivers'),('PLATEAU','Plateau'),('SOKOTO','Sokoto'),('TARABA','Taraba'),('YOBE','Yobe'),('ZAMFARA','Zamfara'))
    stateoforigin=models.CharField(max_length=30,
        choices=StateOfOrigin,
        blank=True,
        default='ABUJA (FCT)'
    )
    dateofbirth = models.DateField(auto_now_add=False)
    occupation = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
