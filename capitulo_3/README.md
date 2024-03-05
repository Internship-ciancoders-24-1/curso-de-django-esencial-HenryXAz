### Ejemplo de clase de modelo

```python
class  User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    is_admin = models.BooleanField(default = False)

    bio = models.TextField(blank=True)

    birthdate = models.DateField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
```



### Métodos del ORM de django

```python
# crear
User.objects.create(params)

# get by attribute
User.objects.get(param='some content')

# get by filter
User.objects.filter(param__endswith='some content')

#  get all objects
User.objects.all()

#  update multiple objects
User.objects.filter(email__endswith='@someemail.com').update(is_admin=True)

```

### Crear superusuario
```bash
python3 manage.py createsuperuser
```