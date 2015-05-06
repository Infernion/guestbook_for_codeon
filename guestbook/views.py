from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from guestbook.models import GuestBookModel
from guestbook.forms import GuestBookForm


class GuestBookView(FormView):
    template_name = 'index.html'
    form_class = GuestBookForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(GuestBookView, self).get_context_data(**kwargs)
        context.update({
            'guest_book_list': GuestBookModel.objects.all().order_by('-created')
        })
        return context

    def form_valid(self, form):
        form.save()
        return super(GuestBookView, self).form_valid(form)