from django.db import models

from Gender.models import Gender

# Create your models here.
class Serie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, default="Lorem, ipsum dolor sit amet consectetur adipisicing elit. Magni consequuntur, dicta corporis quisquam consequatur quia ullam labore, in optio dolorem eius similique quibusdam? Necessitatibus id iste eos adipisci hic nesciunt vel, repellendus quam consequatur ex placeat reprehenderit, itaque nam odit accusamus obcaecati dignissimos. Architecto deleniti rem ducimus. Id, placeat. Adipisci voluptas accusantium repellendus nemo necessitatibus? Dignissimos, voluptatum?")
    release_date = models.DateField()
    poster = models.ImageField(upload_to='serie/')
    number_of_seasons = models.PositiveIntegerField()
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, related_name='series')

    def __str__(self):
        return f"{self.title} / {self.release_date} / {self.number_of_seasons} / {self.gender}"