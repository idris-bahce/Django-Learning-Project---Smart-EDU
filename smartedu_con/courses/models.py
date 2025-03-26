from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name="Course Name", help_text="Write the name of the course")
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="courses/%Y/%m/%d", default="courses/default_course_image.png")
    date = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)


    def __str__(self):
        return self.name
