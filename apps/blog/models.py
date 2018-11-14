from django.db import models
from django.utils import timezone
from django.core.validators import EmailValidator
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Post(models.Model):
	'''
	Modelo para almacenar los posts
	'''
	autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)	
	titulo = models.CharField(max_length=200)
	texto = models.TextField()

	fechaCreacion = models.DateTimeField(default = timezone.now)
	fechaPublicacion = models.DateTimeField(blank = True, null = True)

	def publicar(self):
		'''
		Función para obtener la fecha de publicación
		cuando se publique algún Post
		'''	
		self.fechaPublicacion = timezone.now()
		self.save()

	def __str__(self):
		return self.titulo

class Curso(models.Model):
	id_curso = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=200)
	cupo = models.IntegerField(
		default=1,
		validators=[MaxValueValidator(30), MinValueValidator(1)]
		)
	num_asistentes = models.IntegerField(
		default=1,
		validators=[MaxValueValidator(30), MinValueValidator(1)]
    )
	def __str__(self):
		return self.nombre

class Becario(models.Model):
	GENERACION = (
	('25','25'),
	('26','26'),
	('27','27'),
	('28','28'),
	('29','29'),
	('30','30'),
	('31','31'),
	('32','32'),
	('33','33'),
	('34','34'),
	('35','35'),
	('36','36'),
	('37','37'),
	)
	emailvalidator = EmailValidator(message="Email inválido")
	id_becario = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=100)
	ap_pat = models.CharField(max_length=100)
	ap_mat = models.CharField(max_length=100,blank=True,null=True)
	generacion_proteco = models.CharField(max_length=2,choices=GENERACION) 
	correo = models.CharField(max_length=255,validators=[emailvalidator])
	curso = models.ManyToManyField(Curso)

	def __str__(self):
		return self.nombre+" generación: "+self.generacion_proteco


class Opinion(models.Model):
	id_opinion = models.AutoField(primary_key=True)
	calif_claridad = models.IntegerField(
		default=1,
		validators=[MaxValueValidator(10), MinValueValidator(1)]
        )
	calif_material = models.IntegerField(
		default=1,
		validators=[MaxValueValidator(10), MinValueValidator(1)]
		)
	calif_general = models.IntegerField(
		default=1,
		validators=[MaxValueValidator(10), MinValueValidator(1)]
		)
	comentario = models.TextField()
	curso = models.ManyToManyField(Curso)
	becario = models.ForeignKey(Becario,on_delete=models.CASCADE,null=True) 

	def __str__(self):
		return str(self.id_opinion)

