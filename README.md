# Question

http://stackoverflow.com/questions/13494681/django-order-queryset-by-model-method-without-converting-to-list/13494818#comment18467120_13494818

# Answer

    from django.db.models import Max

    Complaint.objects.annotate(max=Max('responseletter__date_response')).order_by('-max')
