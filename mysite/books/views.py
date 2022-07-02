from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.mail import send_mail
from django.db.models.query_utils import Q
from django.template import TemplateDoesNotExist
from django.views.generic import ListView
from books.models import Book, Publisher
from books.forms import ContactForm

def search (request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(title__contains=query) |
            Q(authors__first_name__contains=query) |
            Q(authors__last_name__contains=query)
        )
        results = Book.objects.filter(qset).distinct()
    else:
        results = []

    return render(request, 'books/search.html', {
        'results': results,
        'query': query
    })


def contact (request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            topic = form.cleaned_data['topic']
            message = form.cleaned_data['message']
            sender = form.cleaned_data.get('sender', 'noreply@example.com')
            send_mail(
                'Feedback from your site Mysite, topic: ' + topic,
                message, sender,
                ['admin@example.com']
            )
            print(topic + '--' + message + '--' + sender)
            return HttpResponseRedirect('<html><body>Thanks</body><html>')
    else:
        form = ContactForm()
    return render(request, 'books/contact.html', { 'form': form })


def about_pages(request):
    try:
        return render(request, 'books/about.html')
    except TemplateDoesNotExist:
        raise Http404()


class PulisherListView(ListView):
    model = Publisher
    context_object_name: str = 'pub_list'

def get_publisher(request, pub_id):
    publisher = get_object_or_404(Publisher, pk=pub_id)
    books = Book.objects.filter(publisher_id=publisher.id)
    return render(request, 'books/publisher_detail.html', {'publisher': publisher, 'books': books})

