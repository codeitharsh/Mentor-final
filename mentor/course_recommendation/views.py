from django.views.generic import TemplateView

class Course_recommendation(TemplateView):
    template_name = 'course_recommendation/course_rec.html'
