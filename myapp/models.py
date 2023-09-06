from django.db import models

class Project(models.Model):
    '''
    Modelo que representa un proyecto
    '''
    name = models.CharField(max_length=50, help_text='ingrese el nombre del proyecto')
    def __str__(self):
        return self.name

class Task(models.Model):
    '''
    Modelo que representan una tarea de un proyecto
    '''
    title = models.CharField(max_length=200, help_text='ingrese el título de la tarea.')
    descrption = models.TextField(help_text='ingrese la descripción de la tarea')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title + ' - ' + str(self.project.name)
    
class Blibliotecas(models.Model):
    '''modelo para las bibliotecas'''
    name = models.CharField(max_length=50, help_text='ingrese el nombre de la biblioteca.')
    direction = models.CharField(max_length=100, help_text='ingrese la direccion de la biblioteca')

class Coleccion(models.Model):
    '''modelo de las colecciones de libro'''
    coleccion = models.CharField(max_length=100, help_text='ingrese a que coleccion pertenece el libro')
    biblioteca = models.ForeignKey(Blibliotecas, on_delete=models.CASCADE)

class Libro(models.Model):
    '''modelo de los libros'''
    coleccion = models.ForeignKey(Coleccion, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, help_text='ingrese el nombre del libro')
    isbn = models.CharField(max_length=100, help_text='ingrese el isbn del libro')
    autor = models.CharField(max_length=100, help_text='ingrese el autor del libro')
    done = models.BooleanField(default=False)

    