# Generated by Django 4.2.11 on 2024-05-11 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movie', '0002_alter_movie_description_alter_movie_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(blank=True, default='Lorem, ipsum dolor sit amet consectetur adipisicing elit. Magni consequuntur, dicta corporis quisquam consequatur quia ullam labore, in optio dolorem eius similique quibusdam? Necessitatibus id iste eos adipisci hic nesciunt vel, repellendus quam consequatur ex placeat reprehenderit, itaque nam odit accusamus obcaecati dignissimos. Architecto deleniti rem ducimus. Id, placeat. Adipisci voluptas accusantium repellendus nemo necessitatibus? Dignissimos, voluptatum?'),
        ),
    ]
