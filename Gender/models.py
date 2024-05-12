from django.db import models

# Create your models here.
class Gender(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True, default="Lorem, ipsum dolor sit amet consectetur adipisicing elit. Magni consequuntur, dicta corporis quisquam consequatur quia ullam labore, in optio dolorem eius similique quibusdam? Necessitatibus id iste eos adipisci hic nesciunt vel, repellendus quam consequatur ex placeat reprehenderit, itaque nam odit accusamus obcaecati dignissimos. Architecto deleniti rem ducimus. Id, placeat. Adipisci voluptas accusantium repellendus nemo necessitatibus? Dignissimos, voluptatum?")
    
    def __str__(self) -> str:
        return self.name