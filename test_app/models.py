from django.db import models


class Complaint(models.Model):
    message         = models.TextField(blank=True)
    email           = models.CharField(max_length=255)

    def __unicode__(self):
        return self.email

    def get_latest_response(self):
        return ResponseLetter.objects.filter(complaint=self)[:1][0]


class ResponseLetter(models.Model):
    date_response       = models.DateField(db_index=True)
    response_content    = models.TextField()
    response_from       = models.CharField(max_length=255)

    complaint           = models.ForeignKey(Complaint)

    def __unicode__(self):
        return self.response_from

    class Meta:
        ordering = ["-date_response"]

