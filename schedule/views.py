from django.views import generic

from schedule.forms import SearchForm
from schedule.models import Course


class CourseListView(generic.ListView):
    model = Course
    template_name = 'schedule/main.html'

    def get_queryset(self):
        form = SearchForm(self.request.GET)

        if form.is_valid():
            q = form.cleaned_data["q"]
            # print("Search request for query:", q)
            return Course.objects.filter(title__icontains=q)

        # Reset and show all
        return Course.objects.all()

    def get_context_data(self, **kwargs):
        context = super(CourseListView, self).get_context_data(**kwargs)
        context["num_courses"] = context["course_list"].count()
        return context


class CourseDetailView(generic.DetailView):
    model = Course
