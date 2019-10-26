from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Topping(models.Model):
    name = models.CharField(max_length=12)

    def __str__(self):
        return self.name




class Pizza(models.Model):
    toppings = models.ManyToManyField(Topping)
    cost = models.IntegerField(default=8.00)
    amount_of_pizzas = models.IntegerField(default=1)
    pizza_size = models.IntegerField(default=8)
    pizza = models.CharField(max_length=12)
    def __str__(self):
        return self.toppings
