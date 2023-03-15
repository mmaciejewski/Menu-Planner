from django.db import models

class User(models.Model):
    UserID = models.IntegerField(primary_key=True)
    Username = models.CharField(max_length=255)
    Password = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    RoleID = models.IntegerField()
    FridgeID = models.IntegerField()
    Avatar = models.CharField(max_length=255)

class Role(models.Model):
    RoleID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=255)
    CanAddRecipe = models.BooleanField()
    CanAddItem = models.BooleanField()
    CanEditFridge = models.BooleanField()
    CanAddComment = models.BooleanField()
    CanSeeUsersDetails = models.BooleanField()

class Comment(models.Model):
    CommentID = models.IntegerField(primary_key=True)
    RecipeID = models.IntegerField()
    Author = models.CharField(max_length=255)
    Description = models.TextField()
    Rating = models.IntegerField()
    Photos = models.CharField(max_length=255)

class Photo(models.Model):
    PhotoID = models.IntegerField(primary_key=True)
    URL = models.CharField(max_length=255)
    IsItHeader = models.BooleanField()

class Recipe(models.Model):
    RecipeID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=255)
    Servings = models.IntegerField()
    Author = models.CharField(max_length=255)
    Description = models.TextField()
    Photos = models.CharField(max_length=255)

class Product(models.Model):
    ProductID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=255)
    GramPerItem = models.IntegerField()
    Kcal = models.FloatField()
    Carbs = models.FloatField()
    Fats = models.FloatField()
    Protein = models.FloatField()
    Fibre = models.FloatField()

class Fridge(models.Model):
    FridgeID = models.IntegerField(primary_key=True)
    UserID = models.IntegerField()

class RecipeProducts(models.Model):
    RecipeID = models.IntegerField()
    ProductID = models.IntegerField()
    Quantity = models.FloatField()
    Unit = models.CharField(max_length=255)

class Unit(models.Model):
    UnitID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=255)
    InGrams = models.FloatField()

class FridgeStock(models.Model):
    ProductID = models.IntegerField()
    FridgeID = models.IntegerField()
    Quantity = models.FloatField()
    Unit = models.CharField(max_length=255)

class RecipeMealType(models.Model):
    RecipeID = models.IntegerField()
    MealTypeID = models.IntegerField()

class MealType(models.Model):
    MealTypeID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=255)