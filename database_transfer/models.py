from django.db import models


class Job(models.Model):
    id = models.BigIntegerField(primary_key=True)
    title = models.TextField()
    created_time = models.DateTimeField(auto_now=True)
    currency_unit = models.TextField()
    salary = models.TextField()
    salary_normalize = models.FloatField()
    url = models.TextField()
    company = models.TextField()
    location = models.TextField()
    info = models.TextField()
    degree_requirements = models.TextField()
    deadline_submit = models.DateField(auto_now=False)
    experience = models.TextField()
    no_of_opening = models.IntegerField()
    formality = models.TextField()
    position = models.TextField()
    gender_requirements = models.TextField()
    career = models.TextField()
    description = models.TextField()
    benefit = models.TextField()
    job_requirements = models.TextField()
    profile_requirements = models.TextField()
    contact = models.TextField()
    other_info = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
        db_table = 'job'
