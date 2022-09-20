from django.db import models

# Create your models here.

class Products(models.Model):
  # // Diccionario de marcas
  HP = "hp"
  ALIENWARE = "aw"
  RAZER = "rz"
  OMEN = "om"
  LENOVO = "lv"
  DELL = "dl"
  # // Diccionario de tipo de productos
  HEADPHONES = "heph"
  LAPTOP = "lpto"
  MOUSE = "mous"
  KEYBOARD = "keyb"
  DISPLAY = "dipy"
  BRAND_PRODUCT = [
    (HP, "HP"),
    (ALIENWARE, "Alienware"),
    (RAZER, "Razer"),
    (OMEN, "Omen"),
    (LENOVO, "Lenovo"),
    (DELL, "Dell")
  ]

  TYPE_PRODUCT = [
    (HEADPHONES, "HeadPhones"),
    (LAPTOP, "Laptop"),
    (MOUSE, "Mouse"),
    (KEYBOARD, "KeyBoard"),
    (DISPLAY, "Display")
  ]

  precio = models.IntegerField()
  tipo = models.CharField(max_length=4,
                          choices=TYPE_PRODUCT,
                          default="Choise a product")
  marca = models.CharField(max_length=2,
                          choices=BRAND_PRODUCT,
                          default="Choice a brand")
  nombre = models.CharField(max_length=200)
  creacion = models.DateTimeField(auto_now_add=True)
