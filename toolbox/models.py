import datetime
from django.utils import timezone
from django.db import models


class ToolBox(models.Model):
    language = models.CharField(max_length=100)

    def __str__(self):
        return self.language

    class Meta:
        verbose_name = "Tool Box"
        verbose_name_plural = "Tool Boxes"


class Tool(models.Model):
    toolbox = models.ForeignKey(ToolBox, on_delete=models.CASCADE, related_name="tools")
    title = models.CharField(max_length=100)
    tool_type = models.CharField(max_length=100)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
