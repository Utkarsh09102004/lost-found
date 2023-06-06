
# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# class Category(models.Model):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name

class Item(models.Model):
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='item_images/')
    location = models.CharField(max_length=255)
    date_lost_or_found = models.DateField()
    is_found = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    contact_email = models.EmailField()

    def __str__(self):
        return self.title

class Claim(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    claimant_name = models.CharField(max_length=255)
    claimant_email = models.EmailField()
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"Claim for {self.item.title}"

class Match(models.Model):
    lost_item = models.ForeignKey(Item, related_name='lost_item', on_delete=models.CASCADE)
    found_item = models.ForeignKey(Item, related_name='found_item', on_delete=models.CASCADE)
    matched_by = models.ForeignKey(User, on_delete=models.CASCADE)
    match_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Match between {self.lost_item} and {self.found_item}"

class Report(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)
    report_date = models.DateField(auto_now_add=True)
    description = models.TextField()
    image = models.ImageField(upload_to='report_images/')

    def __str__(self):
        return f"Report for {self.item}"

# class Notification(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     message = models.TextField()
#     is_read = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.message
